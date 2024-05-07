"""Service module for `users`."""

from django.db import IntegrityError, transaction
from rest_framework.authtoken.models import Token

from users import exceptions, models, repositories
from users.lib import types


class UserService:
    """Service class for `users`."""

    def __init__(self):
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

        token = self.user_repository.get_or_create_token(user=user)

        return self._serialize_user(user, token)

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
            exceptions.UserDoesntExistError("Invalid credentials provided.")

        token = self.user_repository.get_or_create_token(user)

        return self._serialize_user(user=user, token=token)

    def _serialize_user(self, user: models.TRSUser, token: Token) -> types.User:
        """
        Serialize `models.User` instance.

        :param user: `models.User` instance.
        :return: Serialized `models.User` instance.
        """
        return {
            "first_name": user.username,
            "last_name": user.last_name,
            "phone_number": user.phone_number,
            "email": user.email,
            "token": token.key,
        }
