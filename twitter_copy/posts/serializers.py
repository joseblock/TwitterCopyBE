from rest_framework import serializers
from posts.models import Post, MeGusta, Comentario
from django.contrib.auth.models import User


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class MeGustaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeGusta
        fields = '__all__'

class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = '__all__'

