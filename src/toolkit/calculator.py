from decimal import Decimal

from toolkit.errors import DivisionByZero


def calculation(tokens: list[str]) -> Decimal:
    """ Функция для финального вычисления и определения порядка выполнения операций"""
    new_tokens: list[str | Decimal] = []
    i = 0

    while i < len(tokens):
        if tokens[i] == "*" or tokens[i] == "/":
            if tokens[i] == "/" and Decimal(tokens[i + 1]) == 0:
                raise DivisionByZero(
                    "Division by zero is impossible"
                )
            left_sign = new_tokens[-1]
            right_sign = tokens[i + 1]
            if tokens[i] == "*":
                result = Decimal(left_sign) * Decimal(right_sign)


            else:

                result = Decimal(left_sign) / Decimal(right_sign)

            new_tokens[-1] = result

            i += 2

        else:
            new_tokens.append(tokens[i])
            i += 1

    result = Decimal(new_tokens[0])
    i = 1

    while i < len(new_tokens):
        if new_tokens[i] == "+":
            result += Decimal(new_tokens[i + 1])

        if new_tokens[i] == "-":
            result -= Decimal(new_tokens[i + 1])

        i += 2

    return result
