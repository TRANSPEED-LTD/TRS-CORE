"""Base enum classes for all packages under `idcu`."""

from enum import Enum


class ModelChoice(Enum):
    """Enum used to create choice field in models."""

    @classmethod
    def choices(cls):
        """Creates tuple from the class name and value fields."""
        return tuple((x.name, x.value) for x in cls)

    @classmethod
    def has_value(cls, field):
        """Check if requested field exists in Enum class."""
        return field in [field.name for field in cls._value2member_map_.values()]
