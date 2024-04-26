from accounts.models import User
from rest_framework import serializers


class BaseUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
        ]


class CreateUserSerializer(BaseUserSerializer):

    class Meta:
        model = User
        fields = BaseUserSerializer.Meta.fields + ["password"]


class UpdateUserSerializer(BaseUserSerializer):
    class Meta:
        model = User
        fields = BaseUserSerializer.Meta.fields
