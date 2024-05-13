"""Module for API views for `company` package."""

from typing import Any

from abstract_idcu.views.base import IDCUView
from abstract_idcu.base_permissions import HasSpecificCompanyPermission
from companies.views.base import BaseCompanyView
from companies.serializers.output import CompanyResponse
from companies.serializers.input import CompanyToCreateRequest, CompanyToFetchRequest
from companies.exceptions import CompanyIdentifiersNotProvidedError

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated


@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
class CompanyCreateView(BaseCompanyView, IDCUView):
    """Handles request to the `company/<str:create-company>/` endpoint."""

    http_method_names = ['post']
    in_serializer_cls = CompanyToCreateRequest

    def process_request(self, request_params: Any) -> CompanyResponse:
        """
        process request for `company/create-company/` endpoint.

        :param request_params: Request parameters.
        :return: Serialized response.
        """
        user = self.request.user
        response_data = self.service_class.create_company(**request_params, user=user)

        return CompanyResponse(response_data).data


@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated, HasSpecificCompanyPermission])
class CompanyView(BaseCompanyView, IDCUView):
    """Handles request to the `company/<str:get-company>/` endpoint."""

    http_method_names = ['get']
    in_serializer_cls = CompanyToFetchRequest

    def process_request(self, request_params: Any) -> CompanyResponse:
        """
        process request for `company/get-company/` endpoint.

        :param request_params: Request parameters.
        :return: Serialized response.

        :raises CompanyIdentifiersNotProvidedError: If company identifiers not provided.
        """
        if "vat_number" in request_params:
            response_data = self.service_class.fetch_company_by_vat(vat=request_params["vat_number"])

        elif "name" in request_params:
            response_data = self.service_class.fetch_company_by_name(name=request_params["name"])

        else:
            raise CompanyIdentifiersNotProvidedError()

        return CompanyResponse(response_data).data
