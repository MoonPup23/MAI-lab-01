from toolkit.errors import UnknownCharError


def tokenization(text: str) -> list[str]:
    """ Функция для разделения выражения на токены через буфер"""
    tokens = []
    buffer = ""
    sign = ""

    for char in text:

        if char.isspace():
            continue

        if char.isdigit() or char == ".":
            buffer += char
            continue

        if char == "-" or char == "+":

            if buffer:
                tokens.append(sign + buffer)
                buffer = ""
                sign = ""
                tokens.append(char)

            else:
                if sign == "-":
                    sign = ""
                else:
                    sign = "-"
            continue

        if char in "*/":
            if buffer:
                tokens.append(sign + buffer)
                buffer = ""
                sign = ""

            tokens.append(char)
            continue

        raise UnknownCharError(
            f"Invalid Character: {char}"
        )
    if buffer:
        tokens.append(sign + buffer)

    return tokens
