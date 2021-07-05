from django.db import models
from django.utils import timezone


# Create your models here.
class Movie(models.Model):
    def __str__(self):
        return self.title
    title = models.CharField(max_length=255)
    release_year = models.IntegerField()
    genre = models.CharField(max_length=255)
    date_created = models.DateTimeField(default=timezone.now)
    story_line = models.TextField(max_length=1024, default="NOT AVAILABLE")
    img = models.ImageField(upload_to="images/", default="/images/default.jpg")
