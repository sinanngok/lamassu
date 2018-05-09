from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    posted_in = models.ForeignKey('City', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class City(models.Model):
    city_name = models.CharField(max_length=200)
    population = models.IntegerField

    def __str__(self):
        return self.city_name