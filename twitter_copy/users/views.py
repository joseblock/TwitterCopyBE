from rest_framework import viewsets
from users.models import TwitterUserInfo
from django.contrib.auth.models import User
from users.serializers import UserSerializer, TwitterUserInfoSerializer
from permissions.services import APIPermissionClassFactory

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (
    APIPermissionClassFactory(
        name='UserPermission',
        permission_configuration={
            'base': {
                'create': True,
                'list': True,
            },
            'instance': {
                'retrieve': True,
                'update': True,
                'partial_update': True,
                'destroy': True,
            }
        }
    ),
)

class TwitterUserInfoViewSet(viewsets.ModelViewSet):
    queryset = TwitterUserInfo.objects.all()
    serializer_class = TwitterUserInfoSerializer
    #TODO Permissons...
