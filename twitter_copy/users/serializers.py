from rest_framework import serializers
from users.models import TwitterUserInfo
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only= True
    )
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
        )
    def create(self,validated_data):
        return User.objects.create_user(**validated_data)

class TwitterUserInfoSerializer(serializers.ModelSerializer):
    model = TwitterUserInfo
    fields = '__all__'

