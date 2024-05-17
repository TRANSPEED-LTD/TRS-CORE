"""Services module for `documents` package."""

from decimal import Decimal
from django.db import transaction
from django.core.files.uploadedfile import InMemoryUploadedFile

from documents.lib import types
from documents.lib.utils import get_full_url_for_media_files
from documents.models import Order
from documents.repositories import DocumentRepository
from companies.repositories import CompanyRepository
from companies import exceptions as company_exceptions
from companies.models import Company


class DocumentsService:
    """Service class for `documents` package."""

    def __init__(self):
        self.company_repository = CompanyRepository()
        self.document_repository = DocumentRepository()

    @transaction.atomic
    def create_order(
        self,
        forwarder_company: Company,
        shipper_company_vat: str,
        career_company_vat: str,
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
        files: list[InMemoryUploadedFile],
        comments: str | None = None,
    ) -> types.Order:
        """
        Create an order.

        :param forwarder_company: The owner company of this order.
        :param shipper_company_vat: Shipper company's VAT code.
        :param career_company_vat: Career company's VAT code.
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
        :param files: Files to attach to the order.
        :param comments: Additional comments for the order.

        :raises CompanyNotFoundError: If company not found for requested shipper and career VAT codes.
        """
        shipper_company = self.company_repository.get_company_by_vat(vat_number=shipper_company_vat)
        if not shipper_company:
            raise company_exceptions.CompanyNotFoundError("Shipper company not found.")

        career_company = self.company_repository.get_company_by_vat(vat_number=career_company_vat)
        if not career_company:
            raise company_exceptions.CompanyNotFoundError("Career company not found.")

        order = self.document_repository.create_order(
            forwarder_company=forwarder_company,
            shipper_company=shipper_company,
            career_company=career_company,
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

        for file in files:
            self.document_repository.create_order_file(file=file, order=order)

        return self._serialize_order(order=order)

    def fetch_orders_for_company(self, company: Company) -> list[types.Order]:
        """
        Fetch orders for company.

        :param company: `models.Company` instance to fetch orders.
        :return: Serialized `models.Order` instances.
        """
        orders = self.document_repository.get_orders_for_company(company=company)
        return [self._serialize_order(order) for order in orders]


    def _serialize_order(self, order: Order) -> types.Order:
        """
        Serialize order.

        :param order: `models.Order` instance to serialized.
        :return: Serialized `models.Order` instance.
        """

        order_files = [get_full_url_for_media_files(file) for file in order.files]

        return types.Order(
            order_id=order.id,
            shipper_company_vat=order.shipper.vat_number,
            career_company_vat=order.career.vat_number,
            start_location=order.start_location,
            end_location=order.end_location,
            transportation_type=order.transportation_type,
            container_type=order.container_type,
            loading_type=order.loading_type,
            cargo_type=order.cargo_type,
            cargo_category=order.cargo_category,
            cargo_name=order.cargo_name,
            weight=order.weight,
            price=order.price,
            currency=order.currency,
            dimension=order.dimension,
            insurance=order.insurance,
            comments=order.comments,
            files=order_files,
        )
