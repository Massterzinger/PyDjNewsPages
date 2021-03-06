from django.db import models
from django.contrib import admin

# Create your models here.
class NewsPost(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("-timestamp",)

class NewsPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'timestamp']

