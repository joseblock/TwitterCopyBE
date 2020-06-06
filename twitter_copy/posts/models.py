from django.db import models
from django.contrib.auth.models import User
from tags.models import Tag


class Post(models.Model):
    user = models.ForeignKey(
        User,
        null = False,
        on_delete = models.CASCADE,
    )
    content = models.CharField(
        max_length = 1000,
        null = False,
    )
    date = models.DateTimeField(
        auto_now_add = True,
        null = False,
    )
    tag = models.ForeignKey(
        Tag,
        null = True,
        on_delete = models.CASCADE,
    )

class MeGusta(models.Model):
    postId = models.ForeignKey(
        Post,
        null = False,
        on_delete = models.CASCADE
    )
    userId = models.ForeignKey(
        User,
        null = False,
        on_delete = models.CASCADE
    )

class Comentario(models.Model): 
    userId = models.ForeignKey(
        User,
        null = False,
        on_delete = models.CASCADE
    )
    postId = models.ForeignKey(
        Post,
        null = False,
        on_delete = models.CASCADE
    )
    comentario = models.CharField(
        blank = False,
        max_length=100,
    )
    comentarioDateTime = models.DateField(
        auto_now_add = True,
    )
