from django.contrib import admin

from companies.models import Company, PaymentDetail, Iban, Bank

admin.site.register(Company)
admin.site.register(PaymentDetail)
admin.site.register(Iban)
admin.site.register(Bank)
