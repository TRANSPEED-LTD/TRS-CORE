"""Base views for `users` view."""

from rest_framework.views import APIView
from users.services import UserService


class BaseUserView(APIView):
    """Base user view."""

    service_class = UserService()
