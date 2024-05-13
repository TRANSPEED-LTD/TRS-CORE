"""Models module for `companies` package."""
from functools import cached_property

from django.db import models
from django.db.models import QuerySet
from companies.lib.enum import CompanyParty, PaymentDetails, Currency


class TimestampMixin(models.Model):
    """Adds timestamp fields to models."""
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True, db_index=True)

    class Meta:
        abstract = True


class Bank(TimestampMixin):
    """Model defining available banks in our system."""

    bank_name = models.CharField(max_length=30, unique=True, null=False)
    bank_code = models.CharField(max_length=10, unique=True, null=False)

    def __str__(self):
        return f"{self.bank_name} | {self.bank_code}"


class Company(TimestampMixin):
    """Model defining companies data."""

    name = models.CharField(max_length=155, unique=True, null=False)
    party_type = models.CharField(max_length=30, choices=CompanyParty.choices(), null=True, default=None)
    address = models.CharField(max_length=155, null=True, default=None)
    vat_number = models.CharField(max_length=15, null=True, default=None)
    contact_name = models.CharField(max_length=155, null=True, default=None)
    contact_number = models.CharField(max_length=15, null=True, default=None)
    contact_email = models.CharField(max_length=155, null=True, default=None)

    class Meta:
        unique_together = ["name"]
        indexes = [
            models.Index(fields=["name", "vat_number"]),
        ]

    @cached_property
    def ibans(self) -> QuerySet:
        return self.iban_set.all()

    def __str__(self):
        return f"{self.name} | {self.party_type} | {self.address}"


class Iban(TimestampMixin):
    """Model defining iban data."""

    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, null=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=False)
    currency = models.CharField(max_length=10, choices=Currency.choices(), null=True, default=None)
    account_number = models.CharField(max_length=50, null=True)

    class Meta:
        unique_together = ["company", "account_number"]

    @cached_property
    def recipient(self) -> str:
        """Get recipient company name."""
        return self.company.name

    @cached_property
    def bank_name(self) -> str:
        """Get bank name."""
        return self.bank.bank_name

    def __str__(self):
        return f"{self.bank.bank_name} | {self.recipient}"


class PaymentDetail(TimestampMixin):
    """Model defining payment details."""

    type = models.CharField(max_length=30, choices=PaymentDetails.choices(), null=True, default=None)
    receiver_company = models.ForeignKey(
        Company,
        on_delete=models.SET_NULL,
        null=True,
        default=None,
        related_name="received_payment",
    )
    sender_company = models.ForeignKey(
        Company,
        on_delete=models.SET_NULL,
        null=True,
        default=None,
        related_name="sent_payment",
    )
    payment_date = models.DateField(db_index=True)
    agreement = models.CharField(
        max_length=155,
        null=True,
        default=None,
        help_text="This will be auto generated text field, "
                  "based on what is payment date and record creation date for `PaymentDetail` instance."
    )
    quantity = models.IntegerField(null=True, default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=None)
    vat = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=None)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=None)
    currency = models.CharField(max_length=10, choices=Currency.choices(), null=True, default=None)

    class Meta:
        indexes = [
            models.Index(fields=["receiver_company", "sender_company", "payment_date"]),
        ]

    def __str__(self):
        return f"{self.receiver_company} | {self.sender_company} | {self.payment_date}"
