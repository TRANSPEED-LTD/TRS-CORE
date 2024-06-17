"""Service module for `users`."""

from django.db import IntegrityError, transaction
from rest_framework.authtoken.models import Token

from users import exceptions, models, repositories
from companies.services import CompanyServices
from users.lib import types


class UserService:
    """Service class for `users`."""

    def __init__(self):
        self.company_service = CompanyServices()
        self.user_repository = repositories.UserRepository()

    @transaction.atomic
    def create_user(
        self,
        first_name: str,
        last_name: str,
        email: str,
        phone_number: str,
        password: str,
    ) -> types.User:
        """
        Create a new user.

        :param first_name: First name of the user.
        :param last_name: Last name of the user.
        :param email: Email address of the user.
        :param phone_number: Phone number of the user.
        :param password: <PASSWORD>.
        :return: Serialized `models.TRSUser` instance.

        :raises UserCreationError: If user creation fails.
        """
        try:
            user = self.user_repository.create_trs_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone_number=phone_number,
                password=password,
            )
        except IntegrityError as exc:
            raise exceptions.UserCreationError(f"User with `{email}` or `{phone_number}` already exists!") from exc

        return self._serialize_user(user)

    @transaction.atomic
    def fetch_user_with_company(self, user: models.TRSUser) -> types.User:
        """
        Fetch user.

        :return: Serialized `models.TRSUser` instance.
        """
        return self._serialize_user(user=user, fetch_company_details=True)

    def login_user(self, email: str, password: str):
        """
        Fetch user by email.

        :param email: User's email.
        :param password: User's password.
        :return: Serialized user.

        :raises UserDoesntExistError: If user doesn't exist.
        """
        user = self.user_repository.get_user_by_credentials(email=email, password=password)
        if user is None:
            raise exceptions.UserDoesntExistError("Invalid credentials provided.")

        return self._serialize_user(user=user)

    def _serialize_user(self, user: models.TRSUser, fetch_company_details: bool = False) -> types.User:
        """
        Serialize `models.User` instance.

        :param user: `models.User` instance.
        :return: Serialized `models.User` instance.
        """
        token = self.user_repository.get_or_create_token(user=user)

        if fetch_company_details:
            company = self.company_service.fetch_forwarder_company_for_user(user=user)
            return {
                "first_name": user.first_name,
                "last_name": user.last_name,
                "phone_number": user.phone_number,
                "email": user.email,
                "token": token.key,
                "attached_company": company,
            }

        return {
            "first_name": user.first_name,
            "last_name": user.last_name,
            "phone_number": user.phone_number,
            "email": user.email,
            "token": token.key,
        }
