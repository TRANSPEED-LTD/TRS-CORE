"""Module with input serializers for `company/*` endpoints."""

from typing import Any
from rest_framework import serializers
from abstract_idcu.serializers.base import BasicSerializer
from companies.lib.enum import CompanyParty
from rest_framework.exceptions import ValidationError


class IbanToCreate(BasicSerializer):
    """Serializer for Iban input details to create."""

    bank_name = serializers.CharField(required=True)
    currency = serializers.CharField(required=True)
    account_number = serializers.CharField(required=True)


class CompanyToCreateRequest(BasicSerializer):
    """Serializer to input Company details to create."""

    name = serializers.CharField(allow_null=False, required=True)
    party_type = serializers.ChoiceField(choices=CompanyParty.choices(), required=True)
    address = serializers.CharField(allow_null=False, required=True)
    vat_number = serializers.CharField(allow_null=False, required=True)
    ibans = serializers.ListField(child=IbanToCreate(), required=False)

    def validate(self, data):
        """Custom validation method for fields."""

        party_type = data['party_type']
        ibans = data.get('ibans')

        if (party_type == CompanyParty.SHIPPER.value or CompanyParty.CAREER.value) and ibans is None:
            raise ValidationError("At least one IBAN should be provided for company.")

        return data


class CompanyToUpdateRequest(BasicSerializer):
    """Serializer to input Company details to create."""

    name = serializers.CharField(allow_null=False, required=True)
    party_type = serializers.ChoiceField(choices=CompanyParty.choices(), required=True)
    address = serializers.CharField(allow_null=False, required=True)
    vat_number = serializers.CharField(allow_null=False, required=True)
    ibans = serializers.ListField(child=IbanToCreate(), required=False)

    def validate(self, data):
        """Custom validation method for fields."""

        party_type = data['party_type']
        ibans = data.get('ibans')

        if (party_type == CompanyParty.SHIPPER.value or CompanyParty.CAREER.value) and ibans is None:
            raise ValidationError("At least one IBAN should be provided for company.")

        return data

    def to_representation(self, instance: Any) -> Any:
        """
        Custom representation for validated data.

        Clean unuseful data, we don't need for next processes.

        :param instance: `CompanyToUpdateRequest` instance.
        :return:
        """
        data = super().to_representation(instance)
        data.pop("party_type")
        return data


class CompanyToFetchRequest(BasicSerializer):
    """Serializer to input Company identifier details to fetch."""

    name = serializers.CharField(allow_null=True, required=False)
    vat_number = serializers.CharField(allow_null=True, required=False)
