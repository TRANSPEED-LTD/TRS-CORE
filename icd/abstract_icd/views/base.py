"""Base DRF view."""

from abc import abstractmethod
from typing import cast, OrderedDict, Any

from django.http import QueryDict

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.serializers import BaseSerializer
from rest_framework.exceptions import APIException

from abstract_icd.serializers.base import BasicSerializer
from companies.exceptions import WebHttpException


def get_request_payload(request: Request) -> dict | QueryDict:
    """
    Get the payload from request as a dict.

    :param request: The HTTP request
    :return: Dict.
    """

    request_params = request.query_params if request.method == "GET" else request.data
    url_params = request.parser_context["kwargs"]

    if url_params:
        params = request_params.copy()
        params.update(url_params)
        return params

    return request_params


class ICDView(APIView):
    """Abstract base class API views for `company` `inventory` and `document` apps."""

    # input serializer
    in_serializer_cls: type[BaseSerializer] | None = None
    in_serializer_kwargs: dict = {}

    def post(self, request, *args, **kwargs):
        """
        Handle an incoming POST request.

        :param request: The DRF request.
        :return: DRF response.
        """
        return self._handle_request(request)

    def get(self, request, *args, **kwargs) -> Response:
        """
        Handle an incoming GET request.

        :param request: The DRF request.
        :return: DRF response.
        """
        return self._handle_request(request)

    def deserialize_request(self, request) -> OrderedDict:
        """
        Transform the input parameters to ordered dict.

        :param request: The DRF request.
        :return: The parameters of the request as ordered dict.
        """
        in_cls = self._get_input_serializer_cls()
        if in_cls is None:
            raise TypeError(f"Cannot deserialize the request, no input serializer provided.")

        request_payload = get_request_payload(request)
        in_serializer = in_cls(data=request_payload, **self.in_serializer_kwargs)
        in_serializer.is_valid(raise_exception=True)

        return cast(OrderedDict, in_serializer.validated_data)

    def _handle_request(self, request: Request, *args, **kwargs) -> Response:
        """
        Handle request.

        :param request: The DRF request.
        :return: Serialized response.
        """
        try:
            params = self.deserialize_request(request)
            serialized_response = self.process_request(params)
        except WebHttpException as exc:
            raise APIException(detail=exc.detail, code=exc.status_code)

        return Response(serialized_response)

    def _get_input_serializer_cls(self) -> type[BaseSerializer]:
        """
        Retrieve the input serializer class.

        :return: DRF serializer class.
        """
        return self.in_serializer_cls

    @abstractmethod
    def process_request(self, request_params: Any) -> BasicSerializer:
        """
        Processes the request and returns the serialized response.

        :param request_params: Serialized request.
        :return: Serialized response.
        """
        raise NotImplementedError("process_request is not implemented")
