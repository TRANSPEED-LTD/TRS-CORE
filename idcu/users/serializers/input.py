"""Module with input serializers for `users/*` endpoints."""

from rest_framework import serializers
from base_idcu.serializers.base import BasicSerializer


class UserToCreate(BasicSerializer):
    """Serializer to input `User` details to create."""

    first_name = serializers.CharField(max_length=55, allow_null=False, required=True)
    last_name = serializers.CharField(max_length=55, allow_null=False, required=True)
    email = serializers.EmailField(allow_null=False, required=True)
    phone_number = serializers.CharField(max_length=15, allow_null=False, required=True)
    password = serializers.CharField(write_only=True, allow_null=False, required=True)


class UserToLogin(BasicSerializer):
    """Serializer to input `User` details to login."""

    email = serializers.EmailField(allow_null=False, required=True)
    password = serializers.CharField(write_only=True, allow_null=False, required=True)


class Ping(BasicSerializer):
    """Serializer to input for ping view."""

    ping = serializers.CharField(required=True)
