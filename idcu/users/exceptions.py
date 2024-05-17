"""Exceptions raised from `users` package."""

from base_idcu.base_exceptions import WebHttpException


class UserCreationError(WebHttpException):
    """Raised when user creation fails."""

    status_code = 500
    default_detail = "User creation failed"
    default_code = "user_creation_failed"


class UserDoesntExistError(WebHttpException):
    """Raised when user creation fails."""

    status_code = 404
    default_detail = "User doesn't exist."
    default_code = "user_doesnt_exist"

