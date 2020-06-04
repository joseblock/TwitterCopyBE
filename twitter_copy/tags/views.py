from rest_framework import viewsets
from tags.models import Tag
from tags.serializers import TagSerializer
from permissions.services import APIPermissionClassFactory


class TagViewSet (viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    #TODO Permissons...