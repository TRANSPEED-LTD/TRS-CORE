"""Types for `documents` package."""

from decimal import Decimal
from typing import TypedDict


class Order(TypedDict):
    """Order details."""

    shipper_company_vat: str
    career_company_vat: str
    start_location: str
    end_location: str
    transportation_type: str
    container_type: str
    loading_type: str
    cargo_type: str
    cargo_category: str
    cargo_name: str
    weight: Decimal
    price: Decimal
    currency: str
    dimension: str
    insurance: bool
    files: list
    comments: str | None
