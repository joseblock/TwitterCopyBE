from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    user = models.ForeignKey(
        User,
        null = False,
        on_delete = models.CASCADE,
    )
    date = models.DateField(
        auto_now_add= True,
    )
    eventDate = models.DateField(
        null= True,
    )
    ubication = models.CharField(
        max_length= 120,
    )
    description = models.CharField(
        null = False,
        max_length= 400,
    )
class Invited(models.Model):
    event = models.ForeignKey(
        Event,
        null = False,
        on_delete = models.CASCADE,
    )
    user = models.ForeignKey(
        User,
        null = False,
        on_delete = models.CASCADE,
    )
class Confirmed(models.Model):
    event = models.ForeignKey(
        Event,
        null = False,
        on_delete = models.CASCADE,
    )
    user = models.ForeignKey(
        User,
        null = False,
        on_delete = models.CASCADE,
    )
