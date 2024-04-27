"""Module with output serializers for `company/*` endpoints."""
from rest_framework import serializers
from abstract_icd.serializers.base import BasicSerializer


class Iban(BasicSerializer):
    """Serializer for Iban details."""

    bank_name: serializers.CharField()
    company_name: serializers.CharField()
    currency: serializers.CharField()
    account_number: serializers.CharField()
    recipient: serializers.CharField()


class CompanyResponse(BasicSerializer):
    """Serializer to output Company details."""

    name = serializers.CharField()
    party_type = serializers.CharField()
    address = serializers.CharField()
    vat_number = serializers.CharField()
    ibans = serializers.ListField(child=Iban())
    contact_name = serializers.CharField(allow_null=True)
    contact_number = serializers.CharField(allow_null=True)
    contact_email = serializers.CharField(allow_null=True)
    # active_orders = serializers.ListField(allow_null=True)


class CompaniesResponse(BasicSerializer):
    """Serializer to output companies details."""

    companies = serializers.ListField(child=CompanyResponse(), allow_empty=True)
