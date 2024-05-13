"""Package containing utility functions."""

from schwifty import IBAN
from schwifty.exceptions import SchwiftyException
from companies.exceptions import InvalidIbanRequestedError

__all__ = [
    "check_iban_validity",
]


def check_iban_validity(account_number: str, bank_code: str) -> None:
    """
    Check iban validity.

    :param account_number: Account number.
    :param bank_code: Bank code.
    :return: None.
    """
    try:
        iban = IBAN(account_number)

    except SchwiftyException as exc:
        raise InvalidIbanRequestedError() from exc

    if iban.bank_code != bank_code:
        raise InvalidIbanRequestedError(f"Requested account number `{account_number}` is not valid for bank.")
