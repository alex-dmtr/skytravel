import datetime
from django.db import models
from django.utils.text import slugify


class City(models.Model):
    name = models.CharField(max_length=500)
    image = models.CharField(max_length=500)
    subtitle = models.CharField(max_length=500) 

    def get_absolute_url(self):
        return '/cities/%s' % self.to_slug()

    def __str__(self):
        return self.name

    def to_slug(self):
        return slugify(self.name)

    class Meta:
        ordering = ('pk',)

class Location(models.Model):
    name = models.CharField(max_length=500)
    image = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    link = models.URLField(default="/")
    city = models.ForeignKey(City, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.name

    def to_slug(self):
        return slugify(self.name)

    def get_absolute_url(self):
        return '/cities/%s/locations/%s' % (self.city.to_slug(), self.to_slug())

class Event(models.Model):
    name = models.CharField(max_length=500)
    image = models.CharField(max_length=500)
    link = models.URLField(default="/")
    description = models.CharField(max_length=500)
    date = models.DateTimeField(default=datetime.datetime.now())
    city = models.ForeignKey(City, on_delete=models.CASCADE )

    def __str__(self):
        return self.name
