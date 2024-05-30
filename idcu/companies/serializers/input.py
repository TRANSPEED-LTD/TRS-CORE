"""Module with input serializers for `company/*` endpoints."""

from rest_framework import serializers
from base_idcu.serializers.base import BasicSerializer
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
    contact_name = serializers.CharField(allow_null=False, required=True)
    contact_number = serializers.CharField(allow_null=False, required=True)
    contact_email = serializers.CharField(allow_null=False, required=True)

    def validate(self, data):
        """Custom validation method for fields."""

        party_type = data['party_type']
        ibans = data.get('ibans')

        if (party_type == CompanyParty.FORWARDER.value or CompanyParty.CARRIER.value) and ibans is None:
            raise ValidationError("At least one IBAN should be provided for company.")

        return data


class CompanyToUpdateRequest(BasicSerializer):
    """
    Serializer to input Company details to update.

    Clean unuseful data, we don't need for next processes.
    """

    name = serializers.CharField(allow_null=False, required=True)
    party_type = serializers.ChoiceField(choices=CompanyParty.choices(), required=True)
    address = serializers.CharField(allow_null=False, required=True)
    vat_number = serializers.CharField(allow_null=False, required=True)
    ibans = serializers.ListField(child=IbanToCreate(), required=False)
    contact_name = serializers.CharField(allow_null=False, required=True)
    contact_number = serializers.CharField(allow_null=False, required=True)
    contact_email = serializers.CharField(allow_null=False, required=True)

    def validate(self, data):
        """Custom validation method for fields."""

        party_type = data.pop('party_type')
        ibans = data.get('ibans')

        if (party_type == CompanyParty.FORWARDER.value or CompanyParty.CARRIER.value) and ibans is None:
            raise ValidationError("At least one IBAN should be provided for company.")

        return data


class CompanyToDeleteRequest(BasicSerializer):  ### NEEDS WORK OUT
    """
    Serializer to input Company details to delete.

    Clean unuseful data, we don't need for next processes.
    """

    name = serializers.CharField(allow_null=False, required=True)
    party_type = serializers.ChoiceField(choices=CompanyParty.choices(), required=True)
    # address = serializers.CharField(allow_null=False, required=True)
    vat_number = serializers.CharField(allow_null=False, required=True)
    ibans = serializers.ListField(child=IbanToCreate(), required=False)
    # contact_name = serializers.CharField(allow_null=False, required=True)
    # contact_number = serializers.CharField(allow_null=False, required=True)
    # contact_email = serializers.CharField(allow_null=False, required=True)

    def validate(self, data):
        """Custom validation method for fields."""

        party_type = data.pop('party_type')
        ibans = data.get('ibans')

        if (party_type == CompanyParty.FORWARDER.value or CompanyParty.CARRIER.value) and ibans is None:
            raise ValidationError("At least one IBAN should be provided for company.")

        return data


class CompanyToFetchRequest(BasicSerializer):
    """Serializer to input identifier details to fetch companies."""

    search_keyword = serializers.CharField(allow_null=False)
    company_type = serializers.ChoiceField(
        choices=(
            ("CAREER", "CAREER"),
            ("SHIPPER", "SHIPPER")
        )
    )
