"""Repositories module for `Company` model."""

from typing import Sequence
from companies.models import Company, Iban


class CompanyRepository:

    def create_company(
            self,
            name: str,
            party_type: str,
            address: str,
            vat_number: str,
            ibans: Sequence[Iban],
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
        :param ibans: Ibans associated with company.
        :param contact_name: Company contact name.
        :param contact_number: Company contact number.
        :param contact_email: Company contact email.
        :return: Created company instance.

        :raises ValidationError: If creation fails with db constraints.
        """
        raise NotImplementedError("create_company not implemented.")
