"""Module defining types related to `users` package."""

from typing import TypedDict, NotRequired
from companies.lib.types import Company


class User(TypedDict):
    """User details."""

    first_name: str
    last_name: str
    email: str
    phone_number: str
    token: str
    attached_company: NotRequired[Company]
