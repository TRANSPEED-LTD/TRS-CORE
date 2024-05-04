"""Module with output serializers for `company/*` endpoints."""
from rest_framework import serializers
from abstract_icd.serializers.base import BasicSerializer
from companies.lib.enum import CompanyParty


class Iban(BasicSerializer):
    """Serializer for output details."""

    bank_name: serializers.CharField()
    company_name: serializers.CharField()
    currency: serializers.CharField()
    account_number: serializers.CharField()
    recipient: serializers.CharField()


class IbansToCreateRequest(BasicSerializer):
    """Serializer to input Ibans details to create."""

    ibans = serializers.ListField(child=Iban())


class CompanyToCreateRequest(BasicSerializer):
    """Serializer to input Company details to create."""

    name = serializers.CharField(allow_null=False)
    party_type = serializers.ChoiceField(choices=CompanyParty.choices())
    address = serializers.CharField(allow_null=False)
    vat_number = serializers.CharField(allow_null=False)
    contact_name = serializers.CharField(allow_null=True, required=False)
    contact_number = serializers.CharField(allow_null=True, required=False)
    contact_email = serializers.CharField(allow_null=True, required=False)


class CompanyToFetchRequest(BasicSerializer):
    """Serializer to input Company identifier details to fetch."""

    name = serializers.CharField(allow_null=True)
    vat_number = serializers.CharField(allow_null=True)
