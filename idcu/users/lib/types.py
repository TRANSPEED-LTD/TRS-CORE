"""Module defining types related to `users` package."""

from typing import TypedDict


class User(TypedDict):
    """User details."""

    first_name: str
    last_name: str
    email: str
    phone_number: str
    token: str
