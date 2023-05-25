import pint
from pint.errors import UndefinedUnitError
from django.core.exceptions import ValidationError


# def valid_unit_of_measure(value):
#     if value not in valid_unit_measurements:
#         raise ValidationError(f"{value} is not a valid unit of measure")


def valid_unit_of_measure(value):
    ureg = pint.UnitRegistry()
    try:
        single_unit = ureg[value]
    except UndefinedUnitError as e:
        raise ValidationError(f"{value} is not a valid unit of measure")
    except:
        raise ValidationError(f"{value} is invalid. Unknown error.")
