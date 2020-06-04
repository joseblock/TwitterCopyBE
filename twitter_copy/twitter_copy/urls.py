"""twitter_copy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from rest_framework import routers

from users.views import UserViewSet, TwitterUserInfoViewSet
from posts.views import PostViewSet, MeGustaViewSet, ComentarioViewSet
from events.views import EventViewSet, InvitedViewSet, ConfirmedViewSet
from citations.views import CitaViewSet
from conversation.views import ConversationViewSet , MessageViewSet
from tags.views import TagViewSet

from rest_framework_jwt.views import (
    obtain_jwt_token,
    refresh_jwt_token,
    verify_jwt_token,
)
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'twitteruser', TwitterUserInfoViewSet)
router.register(r'posts', PostViewSet)
router.register(r'megusta', MeGustaViewSet)
router.register(r'comentarios', ComentarioViewSet)
router.register(r'citation', CitaViewSet)
router.register(r'tags', TagViewSet)
router.register(r'conversations', ConversationViewSet)
router.register(r'messages', MessageViewSet)
router.register(r'events', EventViewSet)
router.register(r'invited', InvitedViewSet)
router.register(r'confirmed', ConfirmedViewSet)


urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace = 'rest_framework')),
    url(r'^api/', include(router.urls)),    
    url(r'^api-token/auth/', obtain_jwt_token),
    url(r'^api-token/refresh/', refresh_jwt_token),
    url(r'^api-token/verify/', verify_jwt_token),
]
