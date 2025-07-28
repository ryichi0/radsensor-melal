from django.contrib import admin
from .models import BlogPost, Category, BlogImage

class BlogImageInline(admin.TabularInline):
    model = BlogImage
    extra = 1
    min_num = 1
    max_num = 10

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at')
    list_filter = ('category', )
    prepopulated_fields = {"slug": ("title",)}
    inlines = [BlogImageInline]

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        obj.save()

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

