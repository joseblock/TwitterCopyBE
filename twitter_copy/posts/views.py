from rest_framework import viewsets
from posts.models import Post, MeGusta, Comentario
from posts.serializers import PostSerializer, MeGustaSerializer, ComentarioSerializer
from permissions.services import APIPermissionClassFactory


class PostViewSet (viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    #TODO Permissons...

class MeGustaViewSet (viewsets.ModelViewSet):
    queryset = MeGusta.objects.all()
    serializer_class = MeGustaSerializer
    #TODO Permissons...

class ComentarioViewSet (viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
    #TODO Permissons...


