"""Base DRF serializer."""

from typing import Any
from rest_framework import serializers


class BasicSerializer(serializers.Serializer):
    """Basic serializer for all serializers."""

    def update(self, instance: "BasicSerializer", validated_data: Any) -> None:
        """The method is called to save field for an instance that already exists."""
        super().update(instance, validated_data)

    def create(self, validated_data: Any) -> None:
        """The method is called to save field for an instance that already exists."""
        super().create(validated_data)