import pytest

from toolkit.calculator import calculation
from toolkit.errors import (
    DivisionByZero,
    EmptyList,
    IncorrectCharacter,
    UnknownCharError,
)
from toolkit.tokenization import tokenization
from toolkit.validation import validation


def test_tokenization_1() -> None:
    assert tokenization("6 + 7") == ["6", "+", "7"]


def test_tokenization_float() -> None:
    assert tokenization("0.42- 2.25") == ["0.42", "-", "2.25"]


def test_tokenization_unar() -> None:
    assert tokenization("-4 * 7") == ["-4", "*", "7"]


def test_tokenization_unar2() -> None:
    assert tokenization("99 / -9") == ["99", "/", "-9"]


def test_tokenization_invalid_character() -> None:
    with pytest.raises(UnknownCharError):
        tokenization("2!3")


def test_validation_empty() -> None:
    with pytest.raises(EmptyList):
        validation([])


def test_validation_incorrect_number() -> None:
    with pytest.raises(IncorrectCharacter):
        validation(["2.6.7"])


def test_validation_incorrect_number_end() -> None:
    with pytest.raises(IncorrectCharacter):
        validation(["2 +"])


def test_validation_operators() -> None:
    with pytest.raises(IncorrectCharacter):
        validation(["2 ** 3"])


def test_calculator_plus() -> None:
    assert calculation(["6", "+", "7"]) == 13


def test_calculator_minus() -> None:
    assert calculation(["6", "-", "7"]) == -1


def test_calculator_multiplication() -> None:
    assert calculation(["6", "*", "7"]) == 42


def test_calculator_division() -> None:
    assert calculation(["25", "/", "5"]) == 5


def test_calculation_priority() -> None:
    assert calculation(["4", "+", "4", "*", "4"]) == 20


def test_calculation_errors_by_zero() -> None:
    with pytest.raises(DivisionByZero):
        calculation(["50", "/", "0"])
