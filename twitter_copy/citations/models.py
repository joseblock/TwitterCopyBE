from django.db import models
from django.contrib.auth.models import User
from posts.models import Post
class Cita(models.Model):
    user = models.ForeignKey(
        User,
        null = False,
        on_delete= models.CASCADE,
    )
    postId = models.ForeignKey(
        Post,
        null = False,
        on_delete= models.CASCADE,
    )
    content = models.CharField(
        max_length = 500,
    )
