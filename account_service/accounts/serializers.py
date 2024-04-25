from accounts.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "username",
            "password",
            "email",
            "first_name",
            "last_name",
        ]


class CreateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            "username",
            "password",
            "email",
            "first_name",
            "last_name",
        ]
        extra_kwargs = {"password": {"write_only": True}}
