"""Module with output serializers for `document/*` endpoints."""

from rest_framework import serializers
from base_idcu.serializers.base import BasicSerializer


class OrderResponse(BasicSerializer):
    """Serializer for order response."""

    order_id = serializers.IntegerField()
    start_location = serializers.CharField()
    end_location = serializers.CharField()
    transportation_type = serializers.CharField()
    cargo_type = serializers.CharField()
    cargo_category = serializers.CharField()
    cargo_name = serializers.CharField()
    weight = serializers.DecimalField(max_digits=19, decimal_places=2)
    dimension = serializers.CharField()
    created_datetime = serializers.DateTimeField()

    # Extra details for order
    price = serializers.DecimalField(required=False, max_digits=19, decimal_places=2)
    comments = serializers.CharField(required=False)
    container_type = serializers.CharField(required=False)
    loading_type = serializers.CharField(required=False)
    currency = serializers.CharField(required=False)
    insurance = serializers.BooleanField(required=False)
    shipper_company_name = serializers.CharField(required=False)
    carrier_company_name = serializers.CharField(required=False)
    shipper_company_vat = serializers.CharField(required=False)
    carrier_company_vat = serializers.CharField(required=False)
    files = serializers.ListField(child=serializers.CharField(allow_null=True), required=False)
