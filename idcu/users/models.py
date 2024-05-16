"""Models module for `users` package."""
from functools import cached_property

from companies.models import Company

from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.db import models


class TRSUser(AbstractUser):
    """TRSUser model for custom usages."""

    phone_number = models.CharField(unique=True, max_length=20, blank=True)
    email = models.EmailField(_("email address"), blank=True, unique=True)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True)

    @cached_property
    def get_phone_number(self) -> str:
        """Get user phone number."""
        return self.phone_number
