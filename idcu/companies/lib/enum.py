"""Module containing enums for `companies` package."""
from base_idcu.lib.enum import ModelChoice


class CompanyParty(ModelChoice):
    """Company party types."""
    SHIPPER = "SHIPPER"
    FORWARDER = "FORWARDER"
    CAREER = "CAREER"


class PaymentDetails(ModelChoice):
    """Payment details types."""
    INTERNATION_SEA_SHIPPING = "INTERNATION SEA SHIPPING"


class Currency(ModelChoice):
    AMD = "AMD"  # Armenian Dram
    AUD = "AUD"  # Australian Dollar
    AZN = "AZN"  # Azerbaijani Manat
    CAD = "CAD"  # Canadian Dollar
    CHF = "CHF"  # Swiss Franc
    CNY = "CNY"  # Chinese Yuan
    EUR = "EUR"  # Euro
    GBP = "GBP"  # British Pound Sterling
    GEL = "GEL"  # Georgian Lari
    JPY = "JPY"  # Japanese Yen
    NZD = "NZD"  # New Zealand Dollar
    SEK = "SEK"  # Swedish Króna
    USD = "USD"  # United States Dollar
