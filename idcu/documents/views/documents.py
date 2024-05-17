from typing import Any

from base_idcu.views.base import IDCUView
from documents.views.base import BaseDocumentView
from documents.serializers.output import OrderResponse
from documents.serializers.input import OrderToCreate

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated


@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
class OrderCreateView(BaseDocumentView, IDCUView):
    """Handles request to the `company/<str:create-order>/` endpoint."""

    http_method_names = ['post']
    in_serializer_cls = OrderToCreate

    def process_request(self, request_params: Any) -> "OrderResponse":
        """
        process request for `company/create-order/` endpoint.

        :param request_params: Request parameters.
        :return: Serialized response.
        """
        user = self.request.user
        response_data = self.service_class.create_order(**request_params, forwarder_company=user.company)

        return OrderResponse(response_data).data
