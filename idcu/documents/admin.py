"""Admin site for `documents` models."""

from django.contrib import admin

from documents.models import Order

admin.site.register(Order)
