"""Services module for `companies` package."""

from django.db import transaction
from django.core.exceptions import ValidationError

from users.models import TRSUser

from companies.repositories import CompanyRepository
from users.repositories import UserRepository
from companies.lib import types
from companies.lib.utils import check_iban_validity
from companies import models, exceptions


class CompanyServices:
    """Class containing service methods for `companies` package."""

    def __init__(self):
        self.company_repository = CompanyRepository()
        self.user_repository = UserRepository()

    def fetch_company_by_vat(self, vat: str) -> types.Company:
        """
        Fetch company by code.

        :param vat: Company vat identifier.
        :return: `models.Company` instance.

        :raises CompanyNotFoundError: If company doesn't exist by requested vat.
        """
        company = self.company_repository.get_company_by_name_or_vat(vat=vat)

        if company is None:
            raise exceptions.CompanyNotFoundError(f"Company not found by VAT `{vat}`")

        return self._serialize_company(company=company)

    def fetch_company_by_name(self, name: str) -> types.Company:
        """
        Fetch company by name.

        :param name: Company name.
        :return: `models.Company` instance.

        :raises CompanyNotFoundError: If company doesn't exist by requested name.
        """
        company = self.company_repository.get_company_by_name_or_vat(name=name)
        if company is None:
            raise exceptions.CompanyNotFoundError(f"Company not found by name `{name}`")

        return self._serialize_company(company=company)

    @transaction.atomic
    def create_iban(
        self,
        company: models.Company,
        bank_name: str,
        currency: str,
        account_number: str,
    ) -> types.Iban:
        """
        Create IBAN instance.

        :param bank_name: Bank name.
        :param company: `models.Company` instance.
        :param currency: Currency for iban.
        :param account_number: Account number for iban.
        :return: Serialized `models.Iban` instance.

        :raises IbanAlreadyExistError: If IBAN already exists.
        :raises BankNotFoundError: If bank doesn't exist.
        """
        bank = self.company_repository.get_bank_by_name(bank_name=bank_name)
        if bank is None:
            raise exceptions.BankNotFoundError()

        check_iban_validity(account_number=account_number, bank_code=bank.bank_code)
        try:
            iban = self.company_repository.create_iban(
                bank=bank,
                company=company,
                account_number=account_number,
                currency=currency,
            )
            return self._serialize_iban(iban=iban)

        except ValidationError as e:
            raise exceptions.IbanAlreadyExistError(e.message)

    @transaction.atomic
    def create_company(
        self,
        name: str,
        party_type: str,
        address: str,
        vat_number: str,
        ibans: list[types.Iban],
        user: TRSUser,
        contact_name: str | None = None,
        contact_number: str | None = None,
        contact_email: str | None = None,
    ) -> types.Company:
        """
        Create company instance.

        :param name: Company's name.
        :param party_type: Type of company.
        :param address: Jurisdiction address for company.
        :param vat_number: VAT number for company.
        :param ibans: List of company's IBANs.
        :param user: `models.User` instance (Company's main user).
        :param contact_name: Company contact name.
        :param contact_number: Company contact number.
        :param contact_email: Company contact email.
        :return: Serialized `models.Company` instance.

        :raises CompanyAlreadyExists: If company already exists with requested name.
        :raises CompanyContactInformationNotProvidedError: If no contact info provided for company.
        """
        if self.company_repository.get_company_by_name_or_vat(vat=vat_number, name=name):
            raise exceptions.CompanyAlreadyExistError(
                f"Company already exists by provided VAT `{vat_number}` or NAME `{name}`"
            )

        if not any([contact_name, contact_email, contact_number]):
            raise exceptions.CompanyContactInformationNotProvidedError()

        company = self.company_repository.create_company(
            name=name,
            party_type=party_type,
            address=address,
            vat_number=vat_number,
            contact_email=user.email,
            contact_number=user.phone_number,
        )

        for iban in ibans:
            self.create_iban(
                company=company,
                bank_name=iban["bank_name"],
                currency=iban["currency"],
                account_number=iban["account_number"],
            )

        self.user_repository.add_company_to_user(user=user, company=company)

        return self._serialize_company(company=company)

    def _serialize_company(self, company: models.Company) -> types.Company:
        """
        Serialize `models.Company` instance.

        :param company: `models.Company` instance to serialize.
        :return: Serialized `models.Company` instance.
        """
        ibans = [self._serialize_iban(iban) for iban in company.ibans]

        return types.Company(
            name=company.name,
            party_type=company.party_type,
            address=company.address,
            vat_number=company.vat_number,
            contact_name=company.contact_name,
            contact_number=company.contact_number,
            contact_email=company.contact_email,
            ibans=ibans,
            # active_orders=None,
        )

    def _serialize_iban(self, iban: models.Iban) -> types.Iban:
        """
        Serialize `models.Iban` instance.

        :param iban: `models.Iban` instance to serialize.
        :return: Serialized `models.Iban` instance.
        """

        return types.Iban(
            bank_name=iban.bank_name,
            account_number=iban.account_number,
            currency=iban.currency,
        )


