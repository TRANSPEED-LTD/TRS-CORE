"""Script to load test data"""

from django.core.management import BaseCommand
from companies.models import Bank
from users.models import TRSUser


class Command(BaseCommand):
    """Creates Test Data."""

    def handle(self, *args, **options):
        """Load test data"""

        self.create_banks()
        self.create_superuser()

    def create_banks(self) -> None:
        """Create banks for test data."""

        Bank.objects.all().delete()

        Bank.objects.create(bank_name="BOG", bank_code="BG")
        Bank.objects.create(bank_name="TBC", bank_code="TB")

        print("BANKS CREATED")
        print("---------------------------------------------")

    def create_superuser(self):
        """Create superuser"""

        user_info = "testuser@gmail.com"
        TRSUser.objects.create_superuser(
            username=user_info,
            email=user_info,
            password="123"
        )

        print("SUPERUSER CREATED")
        print("---------------------------------------------")
