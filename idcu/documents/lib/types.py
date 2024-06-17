"""Types for `documents` package."""

from decimal import Decimal
from typing import TypedDict
from datetime import datetime


class Order(TypedDict):
    """Order details."""

    order_id: int
    start_location: str
    end_location: str
    created_datetime: datetime
    transportation_type: str
    cargo_type: str
    cargo_category: str
    cargo_name: str
    weight: Decimal
    dimension: str


class FullOrderDetails(Order):
    """Order full details."""
    currency: str
    insurance: bool
    files: list
    comments: str | None
    price: Decimal
    shipper_company_name: str
    shipper_company_vat: str
    carrier_company_name: str
    carrier_company_vat: str
    container_type: str
    loading_type: str
