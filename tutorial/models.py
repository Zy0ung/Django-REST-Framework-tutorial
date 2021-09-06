from django.db import models

# Create your models here.
class blog(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    author = models.CharField(max_length=20, blank=True, default='')
    content = models.TextField()

    class Meta:
        ordering = ('created',)