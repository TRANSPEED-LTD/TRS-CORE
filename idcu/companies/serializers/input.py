"""Module with input serializers for `company/*` endpoints."""
from rest_framework import serializers
from abstract_idcu.serializers.base import BasicSerializer
from companies.lib.enum import CompanyParty


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
    contact_name = serializers.CharField(allow_null=True, required=False)
    contact_number = serializers.CharField(allow_null=True, required=False)
    contact_email = serializers.CharField(allow_null=True, required=False)
    ibans = serializers.ListField(child=IbanToCreate(), required=False)


class CompanyToFetchRequest(BasicSerializer):
    """Serializer to input Company identifier details to fetch."""

    name = serializers.CharField(allow_null=True, required=False)
    vat_number = serializers.CharField(allow_null=True, required=False)
