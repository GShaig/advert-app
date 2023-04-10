from django.db import models

from .utils import create_shortened_url

class Short(models.Model):

    created = models.DateTimeField(auto_now_add=True)

    times_followed = models.PositiveIntegerField(default=0)

    long_url = models.URLField()

    short_url = models.CharField(max_length=15, unique=True, blank=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return f'{self.long_url} to {self.short_url}'

    def save(self, *args, **kwargs):
        if not self.short_url:
            self.short_url = create_shortened_url(self)

        super().save(*args, **kwargs)

class Dom(models.Model):

    domain = models.CharField(max_length=100)

class News(models.Model):

    email = models.EmailField(max_length=100)

class FCMDevice(models.Model):
    registration_id = models.CharField(max_length=500)