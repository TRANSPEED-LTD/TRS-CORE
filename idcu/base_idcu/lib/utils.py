"""Base utils for `idcu`"""

from enum import Enum
from typing import Any


def combine_enums(name: str, *enum_classes: Any):
    """
    Combine multiple enum classes.

    :param name: Combined enum name.
    :param enum_classes: Enum classes to combine.
    :return: Combined enum class.
    """

    combined = {}
    for enum_class in enum_classes:
        combined.update(enum_class.__members__)

    combined_enum = Enum(name, combined)

    def choices(cls):
        return [(item.name, item.value) for item in cls]

    combined_enum.choices = classmethod(choices)
    return combined_enum
