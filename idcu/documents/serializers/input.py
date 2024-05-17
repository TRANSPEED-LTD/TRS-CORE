"""Module with input serializers for `document/*` endpoints."""

from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from base_idcu.serializers.base import BasicSerializer

from companies.lib.enum import Currency
from documents.lib.enum import (
    Transport,
    Container,
    TentContainer,
    ReeferContainer,
    FlatBedContainer,
    CargoCategory,
    Cargo,
    TentLoadingType,
)


class OrderToCreate(BasicSerializer):
    """Serializer for order to create."""

    shipper_company_vat = serializers.CharField(max_length=55, required=True)
    career_company_vat = serializers.CharField(max_length=55, required=True)

    start_location = serializers.CharField(max_length=55, required=True)
    end_location = serializers.CharField(max_length=55, required=True)
    transportation_type = serializers.ChoiceField(required=True, choices=Transport.choices())
    container_type = serializers.ChoiceField(required=True, choices=Container.choices())
    loading_type = serializers.ChoiceField(required=False, choices=TentLoadingType.choices())
    cargo_type = serializers.ChoiceField(required=True, choices=Cargo.choices())
    cargo_category = serializers.ChoiceField(required=True, choices=CargoCategory.choices())
    cargo_name = serializers.CharField(max_length=55, required=True)
    weight = serializers.DecimalField(max_digits=19, decimal_places=2)
    price = serializers.DecimalField(max_digits=19, decimal_places=2)
    currency = serializers.ChoiceField(required=True, choices=Currency.choices())
    dimension = serializers.CharField(max_length=55, required=True)
    insurance = serializers.BooleanField(required=True)
    comments = serializers.CharField(max_length=55, required=False)

    files = serializers.ListField(child=serializers.FileField(), required=False)

    def validate(self, data):
        """Custom validation rules for sub choices."""

        container_type = data["container_type"]
        transportation_type = data["transportation_type"]

        if transportation_type == Transport.TENT.value and data["loading_type"] is None:
            raise ValidationError("`loading type` is required for `Tent` type transportation.")

        if transportation_type == Transport.TENT.value and not TentContainer.has_value(container_type):
            raise ValidationError(
                f"`Tent` type transportation doesn't support `{container_type}` container type."
            )

        if transportation_type == Transport.FLAT_BED.value and not FlatBedContainer.has_value(container_type):
            raise ValidationError(
                f"`Flat Bed` type transportation doesn't support `{container_type}` container type."
            )

        if transportation_type == Transport.REEFER.value and not ReeferContainer.has_value(container_type):
            raise ValidationError(
                f"`Reefer` type transportation doesn't support `{container_type}` container type."
            )

        return data


class OrderToFetch(BasicSerializer):
    """Serializer for order to create."""
    pass
