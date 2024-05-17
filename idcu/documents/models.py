"""Models for `documents` package."""
from functools import cached_property

from django.db import models
from django.db.models import QuerySet

from documents.lib.enum import (
    Transport,
    Container,
    Cargo,
    CargoCategory,
    TentLoadingType,
    OrderStatus,
)
from companies.lib.enum import Currency
from companies.models import Company



class TimestampMixin(models.Model):
    """Adds timestamp fields to models."""
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True, db_index=True)

    class Meta:
        abstract = True


class Order(TimestampMixin):
    """Order model."""
    forwarder = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        help_text="The owner of this order.",
        related_name="forwarder_orders",
    )
    shipper = models.ForeignKey(
        Company,
        on_delete=models.SET_NULL,
        null=True,
        related_name="shipper_orders",
    )
    career = models.ForeignKey(
        Company,
        on_delete=models.SET_NULL,
        null=True,
        related_name="career_orders"
    )

    start_location = models.CharField(max_length=55)
    end_location = models.CharField(max_length=55)
    transportation_type = models.CharField(max_length=10, choices=Transport.choices())
    container_type = models.CharField(max_length=55, choices=Container.choices())
    loading_type = models.CharField(
        max_length=55,
        choices=TentLoadingType.choices(),
        null=True,
        help_text="This option can only set to Tent transport type."
    )
    cargo_type = models.CharField(max_length=55, choices=Cargo.choices())
    cargo_category = models.CharField(max_length=55, choices=CargoCategory.choices())
    cargo_name = models.CharField(max_length=55)
    weight = models.DecimalField(decimal_places=2, max_digits=19)
    price = models.DecimalField(decimal_places=2, max_digits=19)
    currency = models.CharField(max_length=55, choices=Currency.choices())
    dimension = models.CharField(max_length=55)
    insurance = models.BooleanField(default=False)
    comments = models.CharField(max_length=255, null=True)
    status = models.CharField(max_length=25, choices=OrderStatus.choices())

    @cached_property
    def files(self) -> QuerySet:
        return self.orderfile_set.all()

    def __str__(self):
        return f"FORWARDER: {self.forwarder} | SHIPPER: {self.shipper} | CAREER: {self.career}"


class OrderFile(TimestampMixin):
    """Order files."""
    file = models.FileField(upload_to="order_files/")
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __repr__(self):
        return f"{self.file.name} | {self.order}"
