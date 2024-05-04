# Generated by Django 5.0.4 on 2024-05-04 15:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True, db_index=True)),
                ('bank_name', models.CharField(max_length=30, unique=True)),
                ('bank_code', models.CharField(max_length=10, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True, db_index=True)),
                ('name', models.CharField(max_length=155, unique=True)),
                ('party_type', models.CharField(choices=[('SHIPPER', 'SHIPPER'), ('FORWARDER', 'FORWARDER')], default=None, max_length=30, null=True)),
                ('address', models.CharField(default=None, max_length=155, null=True)),
                ('vat_number', models.CharField(default=None, max_length=15, null=True)),
                ('contact_name', models.CharField(default=None, max_length=155, null=True)),
                ('contact_number', models.CharField(default=None, max_length=15, null=True)),
                ('contact_email', models.CharField(default=None, max_length=155, null=True)),
            ],
            options={
                'indexes': [models.Index(fields=['name', 'vat_number'], name='companies_c_name_bf4283_idx')],
                'unique_together': {('name',)},
            },
        ),
        migrations.CreateModel(
            name='Iban',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True, db_index=True)),
                ('currency', models.CharField(choices=[('AMD', 'AMD'), ('AUD', 'AUD'), ('AZN', 'AZN'), ('CAD', 'CAD'), ('CHF', 'CHF'), ('CNY', 'CNY'), ('EUR', 'EUR'), ('GBP', 'GBP'), ('GEL', 'GEL'), ('JPY', 'JPY'), ('NZD', 'NZD'), ('SEK', 'SEK'), ('USD', 'USD')], default=None, max_length=10, null=True)),
                ('account_number', models.CharField(max_length=50, null=True)),
                ('recipient', models.CharField(default=None, max_length=50, null=True)),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.bank')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.company')),
            ],
            options={
                'unique_together': {('company', 'account_number')},
            },
        ),
        migrations.CreateModel(
            name='PaymentDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True, db_index=True)),
                ('type', models.CharField(choices=[('INTERNATION_SEA_SHIPPING', 'INTERNATION_SEA_SHIPPING')], default=None, max_length=30, null=True)),
                ('payment_date', models.DateField(db_index=True)),
                ('agreement', models.CharField(default=None, help_text='This will be auto generated text field, based on what is payment date and record creation date for `PaymentDetail` instance.', max_length=155, null=True)),
                ('quantity', models.IntegerField(default=0, null=True)),
                ('price', models.DecimalField(decimal_places=2, default=None, max_digits=10, null=True)),
                ('vat', models.DecimalField(decimal_places=2, default=None, max_digits=10, null=True)),
                ('total', models.DecimalField(decimal_places=2, default=None, max_digits=10, null=True)),
                ('currency', models.CharField(choices=[('AMD', 'AMD'), ('AUD', 'AUD'), ('AZN', 'AZN'), ('CAD', 'CAD'), ('CHF', 'CHF'), ('CNY', 'CNY'), ('EUR', 'EUR'), ('GBP', 'GBP'), ('GEL', 'GEL'), ('JPY', 'JPY'), ('NZD', 'NZD'), ('SEK', 'SEK'), ('USD', 'USD')], default=None, max_length=10, null=True)),
                ('receiver_company', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='received_payment', to='companies.company')),
                ('sender_company', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sent_payment', to='companies.company')),
            ],
            options={
                'indexes': [models.Index(fields=['receiver_company', 'sender_company', 'payment_date'], name='companies_p_receive_bfcdb4_idx')],
            },
        ),
    ]
