from django.db import models
from django.utils import timezone


# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_year = models.IntegerField()
    genre = models.CharField(max_length=255)
    date_created = models.DateTimeField(default=timezone.now)
