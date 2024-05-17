"""Repositories module for `Company` model."""

from companies import models, exceptions
from django.db.models import Q


class CompanyRepository:
    """Repository class for `Company` and related models."""

    def create_company(
        self,
        name: str,
        party_type: str,
        address: str,
        vat_number: str,
        contact_name: str | None = None,
        contact_number: str | None = None,
        contact_email: str | None = None,
    ):
        """
        Create company instance.
        :param name: Company's name.
        :param party_type: Type of company.
        :param address: Jurisdiction address for company.
        :param vat_number: VAT number for company.
        :param contact_name: Company contact name.
        :param contact_number: Company contact number.
        :param contact_email: Company contact email.
        :return: Created `models.Company` instance.

        :raises ValidationError: If creation fails with db constraints.
        """
        company = models.Company.objects.create(
            name=name,
            party_type=party_type,
            address=address,
            vat_number=vat_number,
            contact_name=contact_name,
            contact_number=contact_number,
            contact_email=contact_email,
        )

        return company

    def update_company(
        self,
        company: models.Company,
        name: str,
        address: str,
    ) -> models.Company:
        """
        Update company instance.

        :param company: Company to update.
        :param name: Company's name.
        :param address: Company's address.
        :return: Updated `models.Company` instance.
        """
        company.name = name
        company.address = address
        company.save()

        return company

    def get_company_by_name_or_vat(self, name: str | None = None, vat: str | None = None) -> models.Company | None:
        """
        Get company by name.

        :param name: Company's name.
        :param vat: Company's vat identifier.
        :return: `models.Company` instance if exists.`

        :raises CompanyIdentifiersNotProvidedError: If none of name and vat are provided.
        """
        if not name and not vat:
            raise exceptions.CompanyIdentifiersNotProvidedError()

        try:
            return models.Company.objects.get(Q(name=name) | Q(vat_number=vat))

        except models.Company.DoesNotExist:
            return None

    def get_company_by_vat(self, vat_number: str) -> models.Company | None:
        """
        Get company by vat code.

        :param vat_number: Company's VAT number.
        :return: `models.Company` instance if exists, else None.
        """
        try:
            return models.Company.objects.get(vat_number=vat_number)
        except models.Company.DoesNotExist:
            return None

    def create_ibans_for_company(
        self,
        bank: models.Bank,
        company: models.Company,
        currency: str,
        account_number: str,
    ) -> models.Iban:
        """
        Create IBAN instance.

        :param bank: `models.Bank` instance.
        :param company: `models.Company` instance.
        :param currency: Currency for iban.
        :param account_number: Account number for iban.
        :return: Created `models.Iban` instance.

        :raises ValidationError: If creation fails with db constraints.
        """
        return models.Iban.objects.create(
            bank=bank,
            company=company,
            currency=currency,
            account_number=account_number,
        )

    def delete_ibans_for_company(self, company: models.Company) -> None:
        """
        Delete IBAN instances.

        :param company: `models.Company` instance.
        """
        models.Iban.objects.filter(company=company).delete()


    def get_bank_by_name(self, bank_name: str) -> models.Bank | None:
        """
        Get bank by name.

        :param bank_name: Bank name.
        :return: `models.Bank` instance if exists or None.`
        """

        try:
            return models.Bank.objects.get(bank_name=bank_name)

        except models.Bank.DoesNotExist:
            return None

    def get_iban_by_bank_and_account_number(self, account_number: str, bank: models.Bank) -> models.Iban | None:
        """
        Get iban by account number.

        :param account_number: Iban's unique account number.
        :param bank: `models.Bank` instance.
        :return: `models.Iban` instance if exists or None.
        """
        try:
            return models.Iban.objects.get(account_number=account_number, bank=bank)

        except models.Iban.DoesNotExist:
            return None

