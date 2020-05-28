from django.db import models

# Create your models here.
class Articles(models.Model):
    title = models.CharField()
    slug = models.SlugField()
    body = models.TextField()
    date = models.models.DateTimeField(auto_now_add=True)
