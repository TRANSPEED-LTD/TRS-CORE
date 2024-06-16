"""Repository module for `users`."""

from companies.models import Company
from users.models import TRSUser

from django.db import transaction
from rest_framework.authtoken.models import Token


class UserRepository:
    """Repository class for `users`."""

    @transaction.atomic
    def create_trs_user(
        self,
        first_name: str,
        last_name: str,
        email: str,
        phone_number: str,
        password: str,
    ) -> TRSUser:
        """
        Create a new user.

        :param first_name: First name of the user.
        :param last_name: Last name of the user.
        :param email: Email address of the user.
        :param phone_number: Phone number of the user.
        :param password: <PASSWORD>.
        :return: Created `TRSUser` instance.

        :raises IntegrityError: If the user creation fails with db constraints.
        """
        return TRSUser.objects.create_user(
            username=email,
            email=email,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            password=password,
        )

    def add_company_to_user(self, user: TRSUser, company: Company) -> None:
        """
        Add company to user.

        :param user: `models.TRSUser` instance to add company for.
        :param company: `models.company` instance for user.
        """
        user.company = company
        user.save()

    def get_or_create_token(self, user: TRSUser) -> Token:
        """
        Get or create auth token.

        :param user: `models.TRSUser` instance.
        :return: `Token` instance.
        """
        token, _ = Token.objects.get_or_create(user=user)
        return token

    def get_user_by_credentials(self, email: str, password: str) -> TRSUser | None:
        """
        Get user by credentials.

        :param email: User's email.
        :param password: User's password.
        :return: `models.TRSUser` instance or None if user doesn't exist.
        """
        try:
            user = TRSUser.objects.get(email=email)
            if user.check_password(password):
                return user

        except TRSUser.DoesNotExist:
            return None
