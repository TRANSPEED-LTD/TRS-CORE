"""Module defining custom exceptions for `companies` package."""

from abstract_idcu.base_exceptions import WebHttpException


class CompanyIdentifiersNotProvidedError(WebHttpException):
    """Raised when identifiers not provided while fetching companies."""

    status_code = 400
    default_detail = "Company identifiers not provided."
    default_code = "company_identifiers_not_provided"


class CompanyNotFoundError(WebHttpException):
    """Raised when company not found by requested identifiers."""

    status_code = 400
    default_detail = "Company not found."
    default_code = "company_not_found"


class CompanyContactInformationNotProvidedError(WebHttpException):
    """Raised if no company contact information provided."""

    status_code = 403
    default_detail = "At least provide `email`, `phone number` or `contact name`."
    default_code = "company_contact_not_provided"


class CompanyAlreadyExistError(WebHttpException):
    """Raised if company already exists with requested data."""

    status_code = 403
    default_detail = "Company already exists."
    default_code = "company_already_exists"


class IbanAlreadyExistError(WebHttpException):
    """Raised if Iban already exists with requested data."""

    status_code = 403
    default_detail = "Iban already exists."
    default_code = "iban_already_exists"


class IbanNotFoundError(WebHttpException):
    """Raised if Iban not found with requested data."""

    status_code = 400
    default_detail = "Iban not found."
    default_code = "iban_not_found"


class BankNotFoundError(WebHttpException):
    """Raised if Bank not found."""

    status_code = 400
    default_detail = "Bank not found."
    default_code = "bank_not_found"
