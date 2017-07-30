import datetime
from django.db import models
from django.utils.text import slugify


class City(models.Model):
    name = models.CharField(max_length=500)
    image = models.CharField(max_length=500)
    subtitle = models.CharField(max_length=500)

    def __str__(self):
        return self.name


    def to_slug(self):
        return slugify(self.name)

class Location(models.Model):
    name = models.CharField(max_length=500)
    image = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    link = models.URLField(default="/")

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=500)
    image = models.CharField(max_length=500)
    link = models.URLField(default="/")
    description = models.CharField(max_length=500)
    date = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.name
