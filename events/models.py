from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=255)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='organized_events', default=1)
    attendees = models.ManyToManyField(User, related_name='registered_events', blank=True)

    def __str__(self):
        return self.title
