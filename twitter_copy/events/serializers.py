from rest_framework import serializers
from events.models import Event, Invited, Confirmed

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class InvitedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invited
        fields = '__all__'

class ConfirmedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Confirmed
        fields = '__all__'