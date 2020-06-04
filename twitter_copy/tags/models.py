from django.db import models

class Tag(models.Model):
    tagname = models.CharField(
        max_length=50,
        unique= True
    )
    color = models.CharField(
        max_length=10,
    )
    description = models.CharField(
        max_length=50,
        null= True
    )
