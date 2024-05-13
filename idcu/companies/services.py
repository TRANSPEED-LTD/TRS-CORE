"""Services module for `companies` package."""

from django.db import transaction
from django.core.exceptions import ValidationError

from users.models import TRSUser

from companies.repositories import CompanyRepository
from users.repositories import UserRepository
from companies.lib import types
from companies import models, exceptions


class CompanyServices:
    """Class containing service methods for `companies` package."""

    def __init__(self):
        self.company_repository = CompanyRepository()
        self.user_repository = UserRepository()

    def fetch_iban_by_bank_name_and_account_number(self, account_number: str, bank_name: str) -> models.Iban:
        """
        Fetch iban by account number.

        :param account_number: Iban's unique account number.
        :return: `models.Iban` instance.

        :raises IbanNotFoundError: If iban not found.
        """
        bank = self.company_repository.get_bank_by_name(bank_name=bank_name)
        iban = self.company_repository.get_iban_by_bank_and_account_number(account_number=account_number, bank=bank)
        if iban is None:
            raise exceptions.IbanNotFoundError(f"IBAN not found by account number `{account_number}`")

        return iban

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
        bank_name: str,
        company_name: str,
        currency: str,
        account_number: str,
        recipient: str,
    ):
        """
        Create IBAN instance.

        :param bank_name: Bank name.
        :param company_name: Company name.
        :param currency: Currency for iban.
        :param account_number: Account number for iban.
        :param recipient: Recipient's juridical name for iban.
        :return: Created `models.Iban` instance.

        :raises IbanAlreadyExistError: If IBAN already exists.
        :raises BankNotFoundError: If bank doesn't exist.
        :raises CompanyNotFoundError: If company doesn't exist.''
        """
        company = self.company_repository.get_company_by_name_or_vat(name=company_name)
        if company is None:
            raise exceptions.CompanyNotFoundError(f"Company `{company_name}` not exists for requested Iban")

        bank = self.company_repository.get_bank_by_name(bank_name=bank_name)
        if bank is None:
            raise exceptions.BankNotFoundError()

        try:
            return self.company_repository.create_iban(
                bank=bank,
                company=company,
                account_number=account_number,
                recipient=recipient,
                currency=currency,
            )
        except ValidationError as e:
            raise exceptions.IbanAlreadyExistError(e.message)

    @transaction.atomic
    def create_company(
        self,
        name: str,
        party_type: str,
        address: str,
        vat_number: str,
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
            contact_name=contact_name,
            contact_email=contact_email,
            contact_number=contact_number,
        )

        self.user_repository.add_company_to_user(user=user, company=company)

        return self._serialize_company(company=company)

    def _serialize_company(self, company: models.Company) -> types.Company:
        """
        Serialize `models.Company` instance.

        :param company: `models.Company` instance to serialize.
        :return: Serialized `models.Company` instance.
        """

        return types.Company(
            name=company.name,
            party_type=company.party_type,
            address=company.address,
            vat_number=company.vat_number,
            contact_name=company.contact_name,
            contact_number=company.contact_number,
            contact_email=company.contact_email,
            ibans=[],
            # active_orders=None,
        )


