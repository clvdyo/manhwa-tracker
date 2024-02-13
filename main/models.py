from django.db import models

# Create your models here.
class Manhwa(models.Model):
    title = models.CharField(max_length=255)
    chapter = models.IntegerField()
    genre = models.CharField(max_length=255)
    sinopsis = models.TextField()
    rating = models.FloatField()