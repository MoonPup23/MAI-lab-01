from toolkit.errors import UnknownCharError


def tokenization(text: str) -> list[str]:
    tokens = []
    buffer = ""  # число которое мы собираем посимвольно
    sign = ""  # знак перед числом

    for char in text:

        if char.isspace():
            continue

        if char.isdigit() or char == ".":
            buffer += char
            continue

        if char == "-" or char == "+":

            if buffer:  # если буфер не пустой
                tokens.append(sign + buffer)
                buffer = ""
                sign = ""
                tokens.append(char)

            else:  # если буфер пустой
                sign = char

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
