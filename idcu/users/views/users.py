"""Module for API views for `users` package."""

from typing import Any

from abstract_idcu.views.base import IDCUView
from users.views.base import BaseUserView
from users.serializers.output import UserResponse
from users.serializers.input import UserToCreate, UserToLogin


class UserCreateView(BaseUserView, IDCUView):
    """Handles request to the `users/create-user/` endpoint."""

    http_method_names = ['post']
    in_serializer_cls = UserToCreate

    def process_request(self, request_params: Any) -> UserResponse:
        """
        process request for `user/create-user/` endpoint.

        :param request_params: Request parameters.
        :return: Serialized response.
        """
        response_data = self.service_class.create_user(**request_params)

        return UserResponse(response_data).data


class UserLoginView(BaseUserView, IDCUView):
    """Handles request to the `users/login-user/` endpoint."""

    http_method_names = ['post']
    in_serializer_cls = UserToLogin

    def process_request(self, request_params: Any) -> UserResponse:
        """
        process request for `user/login-user/` endpoint.

        :param request_params: Request parameters.
        :return: Serialized response.
        """
        response_data = self.service_class.login_user(**request_params)

        return UserResponse(response_data).data
