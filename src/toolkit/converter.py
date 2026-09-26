from decimal import ROUND_HALF_UP, Decimal, getcontext

from toolkit.constant import (
    length_units,
    length_values,
    temperature_units,
    weight_units,
    weight_values,
)
from toolkit.errors import AbsoluteZero, IncompatibleUnits, IncorrectUnit

getcontext().rounding = ROUND_HALF_UP

def length_convert(value: Decimal, from_unit: str, to_unit: str) -> Decimal:
    """Функция для конвертации длин через базовую единицу"""

    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    if from_unit not in length_units:
        raise IncorrectUnit(
            f" IncorrectUnit: {from_unit} "
        )
    if to_unit not in length_units:
        raise IncorrectUnit(
            f" IncorrectUnit: {to_unit} "
        )

    convert_mm = Decimal(str(value)) * length_values[from_unit]
    result = convert_mm / length_values[to_unit]

    return result


def weight_convert(value: Decimal, from_unit: str, to_unit: str) -> Decimal:
    """Функция для конвертации массы через базовую единицу"""
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    if from_unit not in weight_units:
        raise IncorrectUnit(
            f" IncorrectUnit: {from_unit} "
        )
    if to_unit not in weight_units:
        raise IncorrectUnit(
            f" IncorrectUnit: {to_unit} "
        )

    convert_g = Decimal(str(value)) * weight_values[from_unit]
    result = convert_g / weight_values[to_unit]

    return result


def temperature_convert(value: Decimal, from_unit: str, to_unit: str) -> Decimal:
    """ Функция для конвертации температур. За основу формул берутся данные для перевода из открытых источников. Также учитывается абсолютный ноль """
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    if from_unit not in temperature_units:
        raise IncorrectUnit(
            f" IncorrectUnit: {from_unit} "
        )
    if to_unit not in temperature_units:
        raise IncorrectUnit(
            f" IncorrectUnit: {to_unit} "
        )

    if from_unit == "k":
        value = value - Decimal("273.15")

    elif from_unit == "f":
        value = (value - Decimal(32)) * Decimal(5) / Decimal(9)

    if value < Decimal("-273.15"):
        raise AbsoluteZero(
            " Temperature is lower absolute zero "
        )
    if to_unit == "k":
        value = value + Decimal("273.15")

    if to_unit == "f":
        value = value * Decimal(9) / Decimal(5) + Decimal(32)

    return value


def final_convert(value: Decimal, from_unit: str, to_unit: str) -> Decimal:
    """ Финальная функция,которая  """
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    if from_unit not in length_units and from_unit not in weight_units and from_unit not in temperature_units:
        raise IncorrectUnit(
            f" IncorrectUnit: {from_unit} "
        )

    if to_unit not in length_units and to_unit not in weight_units and to_unit not in temperature_units:
        raise IncorrectUnit(
            f" IncorrectUnit: {to_unit} "
        )

    if from_unit in length_units and to_unit in length_units:
        return length_convert(value, from_unit, to_unit)

    if from_unit in weight_units and to_unit in weight_units:
        return weight_convert(value, from_unit, to_unit)

    if from_unit in temperature_units and to_unit in temperature_units:
        return temperature_convert(value, from_unit, to_unit)

    raise IncompatibleUnits(
        "Incompatible units"
    )
