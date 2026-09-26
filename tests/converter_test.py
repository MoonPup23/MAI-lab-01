from decimal import Decimal

import pytest

from toolkit.converter import final_convert
from toolkit.errors import AbsoluteZero, IncompatibleUnits, IncorrectUnit


def test_length_m_to_cm() -> None:
    assert final_convert(Decimal(5), "m", "cm") == Decimal("500.0")


def test_length_mm_to_km() -> None:
    assert final_convert(Decimal(5), "mm", "km") == Decimal("0.000005")


def test_length_m_to_km() -> None:
    assert final_convert(Decimal(7), "M", "KM") == Decimal("0.007")


def test_weight_g_to_kg() -> None:
    assert final_convert(Decimal(67), "g", "kg") == Decimal("0.067")


def test_weight_kg_to_g() -> None:
    assert final_convert(Decimal(3), "kg", "G") == Decimal(3000)


def test_temperature_c_to_f() -> None:
    assert final_convert(Decimal(0), "c", "f") ==  Decimal("32.0")


def test_temperature_c_to_k() -> None:
    assert final_convert(Decimal(0), "c", "k") == Decimal("273.15")


def test_converter_unknown_unit() -> None:
    with pytest.raises(IncorrectUnit):
        final_convert(Decimal(10), "gm", "m")

def test_converter_incompatible_units() -> None:
    with pytest.raises(IncompatibleUnits):
        final_convert(Decimal(30), "cm", "f")

def test_converter_zero() -> None:
    with pytest.raises(AbsoluteZero):
        final_convert(Decimal(-300), "c", "k")
