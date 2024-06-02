"""Services module for `companies` package."""

from django.db import transaction
from django.core.exceptions import ValidationError

from users.models import TRSUser

from companies.repositories import CompanyRepository
from users.repositories import UserRepository
from companies.lib import types
from companies.lib.utils import check_iban_validity
from companies.lib.enum import CompanyParty
from companies import models, exceptions


class CompanyServices:
    """Class containing service methods for `companies` package."""

    def __init__(self):
        self.company_repository = CompanyRepository()
        self.user_repository = UserRepository()

    def fetch_forwarder_company_for_user(self, user: TRSUser) -> types.Company:
        """
        Fetch forwarder company for given user.

        :param user: `models.TRSUser` instance for fetch forwarder company.
        :return: Serialized `models.Company` instance for given user.

        :raises CompanyNotFoundError: If user is not attached to any forwarder companies.
        """
        forwarder_company = user.company
        if not forwarder_company:
            raise exceptions.CompanyNotFoundError(f"{user.username} is not attached to any forwarder companies.")

        return self._serialize_company(user.company)

    def fetch_company_by_keyword(self, search_keyword: str, company_type: str) -> list[types.Company]:
        """
        Fetch companies by provided keyword.

        :param search_keyword: The keyword to filter companies.
        :param company_type: Company party types to filter.
        :return: Serialized list `models.Company` instances.
        """
        companies = self.company_repository.get_companies_by_keyword(search_keyword=search_keyword, company_type=company_type)
        return [self._serialize_company(company) for company in companies]

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
    def create_ibans_for_company(
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
            iban = self.company_repository.create_ibans_for_company(
                bank=bank,
                company=company,
                account_number=account_number,
                currency=currency,
            )
            return self._serialize_iban(iban=iban)

        except ValidationError as e:
            raise exceptions.IbanAlreadyExistError(e.message)

    @transaction.atomic
    def update_ibans_for_company(
        self,
        company: models.Company,
        bank_name: str,
        currency: str,
        account_number: str,
    ) -> None:
        """
        Update IBAN instances for company.

        :param bank_name: Bank name.
        :param company: `models.Company` instance.
        :param currency: Currency for iban.
        :param account_number: Account number for iban.
        :return: Serialized `models.Iban` instance.

        :raises IbanAlreadyExistError: If IBAN already exists.
        :raises BankNotFoundError: If bank doesn't exist.
        """
        self.delete_ibans_for_company(company=company, bank_name=bank_name, currency=currency, account_number=account_number)
        self.create_ibans_for_company(
            company=company,
            bank_name=bank_name,
            currency=currency,
            account_number=account_number,
        )

    @transaction.atomic
    def delete_ibans_for_company(self, company: models.Company, bank_name: str, currency: str, account_number: str) -> None:
        """
        Delete IBAN instances for company.

        :param company: `models.Company` instance.
        :return: None.
        """
        self.company_repository.delete_ibans_for_company(
            company=company, 
            bank_name=bank_name, 
            currency= currency,
            account_number=account_number
            )

    @transaction.atomic
    def create_company(
        self,
        name: str,
        party_type: str,
        address: str,
        vat_number: str,
        ibans: list[types.Iban],
        contact_name: str,
        contact_number: str,
        contact_email: str,
        user: TRSUser,
    ) -> types.Company:
        """
        Create company instance.

        :param name: Company's name.
        :param party_type: Type of company.
        :param address: Jurisdiction address for company.
        :param vat_number: VAT number for company.
        :param ibans: List of company's IBANs.
        :param contact_name: Name of the contact person.
        :param contact_number: Number of the contact person.
        :param contact_email: Email of the contact person.
        :param user: `models.User` instance (Company's main user).
        :return: Serialized `models.Company` instance.

        :raises CompanyAlreadyExists: If company already exists with requested name.
        """
        if user.company and party_type == CompanyParty.FORWARDER.value:
            raise exceptions.CompanyAlreadyExistError(f"User already has attached to forwarder company {user.company.name}")

        if self.company_repository.get_company_by_name_or_vat(vat=vat_number, name=name):
            raise exceptions.CompanyAlreadyExistError(
                f"Company already exists by provided VAT `{vat_number}` or NAME `{name}`"
            )

        company = self.company_repository.create_company(  ### ??? contacts ???
            name=name,
            party_type=party_type,
            address=address,
            vat_number=vat_number,
            contact_name= contact_name,
            contact_number= contact_number,
            contact_email=contact_email,
        )

        for iban in ibans:
            self.create_ibans_for_company(
                company=company,
                bank_name=iban["bank_name"],
                currency=iban["currency"],
                account_number=iban["account_number"],
            )

        if party_type == CompanyParty.FORWARDER.value:
            self.user_repository.add_company_to_user(user=user, company=company)

        return self._serialize_company(company=company)

    @transaction.atomic
    def update_company(
        self,
        name: str,
        address: str,
        vat_number: str,
        ibans: list[types.Iban],
        contact_name: str,
        contact_number: str,
        contact_email: str,
        user: TRSUser,
    ) -> types.Company:
        """
        Update company instance.

        :param name: Company's name.
        :param address: Jurisdiction address for company.
        :param vat_number: VAT number for company.
        :param ibans: List of company's IBANs.
        :param contact_name: Name of the contact person.
        :param contact_number: NUmber of the contact person.
        :param contact_email: Email of the contact person.
        :return: Serialized updated `models.Company` instance.
        :param user: `models.User` instance (Company's main user).
        """
        company = self.company_repository.get_company_by_name_or_vat(vat=vat_number)
        if company is None:
            raise exceptions.CompanyNotFoundError(
                f"Company not found by provided VAT `{vat_number}`"
            )

        company = self.company_repository.update_company(
            company=company,
            name=name,
            address=address,
            contact_name = contact_name,
            contact_number = contact_number,
            contact_email = contact_email,
        )

        for iban in ibans:
            self.update_ibans_for_company(
                company=company,
                bank_name=iban["bank_name"],
                currency=iban["currency"],
                account_number=iban["account_number"],
            )

        return self._serialize_company(company)
    # NEEDS WORK ON
    @transaction.atomic
    def delete_company(
        self,
        # name: str,
        # address: str,
        vat_number: str,
        # ibans: list[types.Iban],
        # contact_name: str,
        # contact_number: str,
        # contact_email: str,
        user: TRSUser,
    ) -> types.Company:
        """
        Delete company instance.

        :param name: Company's name.
        :param address: Jurisdiction address for company.
        :param vat_number: VAT number for company.
        :param ibans: List of company's IBANs.
        :param contact_name: Name of the contact person.
        :param contact_number: NUmber of the contact person.
        :param contact_email: Email of the contact person.
        :return: Serialized deleted `models.Company` instance.
        """
        company = self.company_repository.get_company_by_name_or_vat(vat=vat_number)
        if company is None:
            raise exceptions.CompanyNotFoundError(
                f"Company not found by provided VAT: `{vat_number}`"
            )
        print(company.ibans[0].bank)
        for iban in company.ibans:
            self.delete_ibans_for_company(
                company=company,
                # bank_name = iban.get("bank"),
                bank_name = iban.bank,
                currency=iban.currency,
                account_number=iban.account_number,
            )

        company = self.company_repository.delete_company(
            company=company,
            # name=name,
            vat_number=vat_number,
        )

        # return self._serialize_company(company)
        return None

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
