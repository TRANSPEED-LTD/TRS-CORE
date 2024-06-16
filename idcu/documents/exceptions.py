"""Module defining custom exceptions for `documents` package."""

from base_idcu.base_exceptions import WebHttpException


class OrderNotFound(WebHttpException):
    """Raised when order not found."""

    status_code = 404
    default_detail = "Order not found."
    default_code = "order_not_found"
