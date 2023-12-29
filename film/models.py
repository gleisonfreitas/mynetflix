from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.


LIST_CATEGORY = (
    ('ACTION', 'Action'),
    ('DRAMA', 'Drama'),
    ('COMEDY', 'Comedy')
)

#criar o filme
class Film(models.Model):
    title = models.CharField(max_length=100)
    thumb = models.ImageField(upload_to='thumb_film')
    description = models.TextField(max_length=1000)
    category = models.CharField(max_length=15, choices=LIST_CATEGORY)
    visualization = models.IntegerField(default=0)
    creation_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Chapter(models.Model):
    film = models.ForeignKey("Film", related_name="chapters", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    video = models.URLField()

    def __str__(self):
        return self.title


class User(AbstractUser):
    movies_watched = models.ManyToManyField("Film")

