from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, allow_unicode=True)
    objects = models.Manager()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)
    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, allow_unicode=True)
    content = models.TextField( blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="posts")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)

    objects = models.Manager()

    def __str__(self):
        return self.title

class BlogSection(models.Model):
    blog_post = models.ForeignKey(BlogPost, related_name='sections', on_delete=models.CASCADE)
    heading = models.CharField(max_length=255)
    content = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.blog_post.title} - {self.heading}"

class BlogImage(models.Model):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    caption = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Image for {self.blog_post.title if self.blog_post else 'Unknown'}"


# Create your models here.
