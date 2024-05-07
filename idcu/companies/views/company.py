"""Module for API views for `company` package."""

from typing import Any

from abstract_idcu.views.base import IDCUView
from companies.views.base import BaseCompanyView
from companies.serializers.output import CompanyResponse


class CompanyCreateView(BaseCompanyView, IDCUView):
    """Handles request to the `company/<str:create-company>/` endpoint."""

    http_method_names = ['post']

    def process_request(self, request_params: Any) -> CompanyResponse:
        """
        process request for `company/create-company/` endpoint.

        :param request_params: Request parameters.
        :return: Serialized response.
        """
        response_data = self.service_class.create_company(**request_params)

        return CompanyResponse(response_data).data
