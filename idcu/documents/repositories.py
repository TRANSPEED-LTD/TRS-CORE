"""Repositories module for `documents` models."""

from decimal import Decimal

from django.db.models import QuerySet

from companies.models import Company
from documents.models import Order, OrderFile


class DocumentRepository:
    """Repository class for `documents` related models."""

    def create_order_file(self, file, order: Order) -> OrderFile:
        """
        Create a file attached to order.

        :param file: File to create.
        :param order: The order file to be attached.
        """
        return OrderFile.objects.create(file=file, order=order)


    def create_order(
        self,
        forwarder_company: Company,
        shipper_company: Company,
        career_company: Company,
        start_location: str,
        end_location: str,
        transportation_type: str,
        container_type: str,
        loading_type: str,
        cargo_type: str,
        cargo_category: str,
        cargo_name: str,
        weight: Decimal,
        price: Decimal,
        currency: str,
        dimension: str,
        insurance: bool,
        comments: str | None = None,
    ) -> Order:
        """
        Create an order.

        :param forwarder_company: The owner company for this order.
        :param shipper_company: Shipper company for this order.
        :param career_company: Career company for this order.
        :param start_location: Start location for order.
        :param end_location: End/final location for order.
        :param transportation_type: Transportation type.
        :param container_type: Container type.
        :param loading_type: Loading type.
        :param cargo_type: Cargo type.
        :param cargo_category: Cargo category.
        :param cargo_name: Cargo name.
        :param weight: Weight of order.
        :param price: Price of order.
        :param currency: The currency.
        :param dimension: Order dimensions (X, Y, Z).
        :param insurance: If order is insured or not.
        :param comments: Additional comments for the order.

        :return: Created `Order` instance.
        """

        return Order.objects.create(
            forwarder=forwarder_company,
            shipper=shipper_company,
            career=career_company,
            start_location=start_location,
            end_location=end_location,
            transportation_type=transportation_type,
            container_type=container_type,
            loading_type=loading_type,
            cargo_type=cargo_type,
            cargo_category=cargo_category,
            cargo_name=cargo_name,
            weight=weight,
            price=price,
            currency=currency,
            dimension=dimension,
            insurance=insurance,
            comments=comments,
        )

    def get_orders_for_company(self, company: Company) -> QuerySet:
        """
        Get orders for company.

        :param company: `models.Company` instance to fetch orders.
        :return: `models.Order` instances.
        """
        return Order.objects.filter(forwarder=company)
