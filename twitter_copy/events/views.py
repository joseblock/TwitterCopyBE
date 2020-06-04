from rest_framework import viewsets
from events.models import Event, Invited, Confirmed
from events.serializers import EventSerializer, InvitedSerializer, ConfirmedSerializer
from permissions.services import APIPermissionClassFactory


class EventViewSet (viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    #TODO Permissons...

class InvitedViewSet (viewsets.ModelViewSet):
    queryset = Invited.objects.all()
    serializer_class = InvitedSerializer
    #TODO Permissons...

class ConfirmedViewSet (viewsets.ModelViewSet):
    queryset = Confirmed.objects.all()
    serializer_class = ConfirmedSerializer
    #TODO Permissons...