"""Module with output serializers for `document/*` endpoints."""

from rest_framework import serializers
from base_idcu.serializers.base import BasicSerializer


class OrderResponse(BasicSerializer):
    """Serializer for order response."""

    order_id = serializers.IntegerField()
    shipper_company_vat = serializers.CharField()
    carrier_company_vat = serializers.CharField()
    start_location = serializers.CharField()
    end_location = serializers.CharField()
    transportation_type = serializers.CharField()
    container_type = serializers.CharField()
    loading_type = serializers.CharField()
    cargo_type = serializers.CharField()
    cargo_category = serializers.CharField()
    cargo_name = serializers.CharField()
    weight = serializers.DecimalField(max_digits=19, decimal_places=2)
    price = serializers.DecimalField(max_digits=19, decimal_places=2)
    currency = serializers.CharField()
    dimension = serializers.CharField()
    insurance = serializers.BooleanField()
    comments = serializers.CharField()

    files = serializers.ListField(child=serializers.CharField(allow_null=True), required=False)
