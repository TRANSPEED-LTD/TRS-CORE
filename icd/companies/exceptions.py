"""Module defining custom exceptions for `companies` package."""


class WebHttpException(Exception):
    """
    Base class for web http exceptions.

    Subclasses should provide `status_code` and `default_detail` properties.
    """

    status_code = 500
    default_detail = "A server error occurred."
    default_code = "error"

    def __init__(self, detail: str | None = None, code: str | None = None) -> None:
        self.detail: str = self.default_detail if detail is None else detail
        self.error_code: str = self.default_code if code is None else code

        super().__init__(self.detail, self.error_code)


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
