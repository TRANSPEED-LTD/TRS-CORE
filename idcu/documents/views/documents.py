from typing import Any

from base_idcu.views.base import IDCUView
from documents.views.base import BaseDocumentView
from documents.serializers.output import OrderResponse
from documents.serializers.input import OrderToCreate, OrdersToFetch, OrderToFetch

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated


@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
class OrderCreateView(BaseDocumentView, IDCUView):
    """Handles request to the `company/<str:create-order>/` endpoint."""

    http_method_names = ['post']
    in_serializer_cls = OrderToCreate

    def process_request(self, request_params: Any) -> OrderResponse:
        """
        process request for `company/create-order/` endpoint.

        :param request_params: Request parameters.
        :return: Serialized response.
        """
        user = self.request.user
        response_data = self.service_class.create_order(**request_params, forwarder_company=user.company)

        return OrderResponse(response_data).data


@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
class OrdersView(BaseDocumentView, IDCUView):
    """Handles request to the `company/<str:get-orders>/` endpoint."""

    http_method_names = ['get']
    in_serializer_cls = OrdersToFetch

    def process_request(self, request_params: Any) -> OrderResponse:
        """
        process request for `company/get-orders/` endpoint.

        Fetches all orders for request user company.

        :param request_params: Request parameters.
        :return: Serialized response.
        """
        user = self.request.user
        response_data = self.service_class.fetch_orders_for_company(company=user.company)

        return OrderResponse(response_data, many=True).data


@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
class OrderView(BaseDocumentView, IDCUView):
    """Handles request to the `company/<str:get-orders>/` endpoint."""

    http_method_names = ['get']
    in_serializer_cls = OrderToFetch

    def process_request(self, request_params: Any) -> OrderResponse:
        """
        process request for `company/get-order/` endpoint.

        Fetches specific order for requested order id.

        :param request_params: Request parameters.
        :return: Serialized response.
        """
        response_data = self.service_class.fetch_order_by_id(order_id=request_params["order_id"])

        return OrderResponse(response_data, many=True).data
