from django.db import models

# Create your models here.
class Anteiku(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technology = models.CharField(max_length=200)
    created_at = models.DateField(auto_now=True)
