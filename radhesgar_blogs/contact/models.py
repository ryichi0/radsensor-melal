from django.db import models

class ContactMessage(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField()
    company = models.CharField(max_length=250)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    class Meta:
        verbose_name_plural = "Contact Messages"

    def __str__(self):
        return self.email