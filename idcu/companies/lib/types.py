"""Module representing data types for `companies` package."""

from typing import TypedDict


class Iban(TypedDict):
    """Iban details."""
    bank_name: str
    currency: str
    account_number: str


class Company(TypedDict):
    """Company details."""
    name: str
    party_type: str
    address: str
    vat_number: str
    contact_name: str | None
    contact_number: str | None
    contact_email: str | None
    ibans: list[Iban]

