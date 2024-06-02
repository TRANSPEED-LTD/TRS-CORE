"""Module for API views for `company` package."""

from typing import Any

from base_idcu.views.base import IDCUView
from companies.views.base import BaseCompanyView
from companies.serializers.output import CompanyResponse
from companies.serializers.input import CompanyToCreateRequest, CompanyToUpdateRequest, CompanyToDeleteRequest, CompanyToFetchRequest

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated


@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
class ForwarderCompanyView(BaseCompanyView, IDCUView):
    """Handles request to the `company/<str:get-user-company>/` endpoint."""

    http_method_names = ['get']

    def process_request(self, request_params: Any) -> CompanyResponse:
        """
        process request for `company/get-company/` endpoint.

        :param request_params: Request parameters.
        :return: Serialized response.
        """
        response_data = self.service_class.fetch_forwarder_company_for_user(user=self.request.user)
        return CompanyResponse(response_data).data


@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
class CompaniesFilterView(BaseCompanyView, IDCUView):
    """Handles request to the `company/<str:get-companies>/` endpoint."""

    http_method_names = ['get']
    in_serializer_cls = CompanyToFetchRequest

    def process_request(self, request_params: Any) -> CompanyResponse:
        """
        Process request for `company/get-companies/` endpoint.

        Filters companies for requested params.

        :param request_params: Request parameters.
        :return: Serialized response.
        """
        response_data = self.service_class.fetch_company_by_keyword(**request_params)
        return CompanyResponse(response_data, many=True).data


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
@permission_classes([IsAuthenticated])
class CompanyUpdateView(BaseCompanyView, IDCUView):
    """Handles request to the `company/<str:update-company>/` endpoint."""

    http_method_names = ['post']
    in_serializer_cls = CompanyToUpdateRequest

    def process_request(self, request_params: Any) -> CompanyResponse:
        """
        process request for `company/update-company/` endpoint.

        :param request_params: Request parameters.
        :return: Serialized response.
        """
        user = self.request.user
        response_data = self.service_class.update_company(**request_params, user=user)

        return CompanyResponse(response_data).data
    

@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
class CompanyDeleteView(BaseCompanyView, IDCUView):
    """Handles request to the `company/<str:delete-company>/` endpoint."""

    http_method_names = ['post']
    in_serializer_cls = CompanyToDeleteRequest

    def process_request(self, request_params: Any) -> CompanyResponse:
        """
        process request for `company/delete-company/` endpoint.

        :param request_params: Request parameters.
        :return: Serialized response.
        """

        # request_params["name"] = None
        # request_params["ibans"] = None
        print(request_params)
        user = self.request.user
        response_data = self.service_class.delete_company(**request_params, user=user)

        return CompanyResponse(response_data).data
