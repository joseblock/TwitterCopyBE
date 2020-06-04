from django.db import models
from django.contrib.auth.models import User

class TwitterUserInfo(models.Model):
    user = models.ForeignKey(
        User,
        null = False,
        on_delete= models.CASCADE,
    )
    biografy = models.CharField(
        max_length= 140,
    )
    gender = models.BooleanField()
    birthDate = models.DateField()


