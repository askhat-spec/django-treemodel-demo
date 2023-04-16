from django.db import models
from django.urls import reverse


class Genre(models.Model):
    name = models.CharField(max_length=150)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)

    def get_url(self):
        return reverse('genre', args=[self.id])

    def __str__(self) -> str:
        return self.name

class Game(models.Model):
    name = models.CharField(max_length=150)
    genres = models.ManyToManyField(Genre, related_name='games', blank=True)

    def __str__(self) -> str:
        return self.name