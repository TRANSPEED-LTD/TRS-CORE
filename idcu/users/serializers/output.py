"""Module with output serializers for `users/*` endpoints."""

from rest_framework import serializers
from base_idcu.serializers.base import BasicSerializer


class UserCompanyEntry(BasicSerializer):
    """Serializer for user attached company details."""

    name = serializers.CharField()


class UserResponse(BasicSerializer):
    """Serializer to output `User` details."""

    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    phone_number = serializers.CharField()
    token = serializers.CharField()
    attached_company = UserCompanyEntry(required=False, allow_null=True)


class PongResponse(BasicSerializer):
    """Serializer to output ping."""

    pong = serializers.CharField(default="PONG")
