import re

from toolkit.errors import EmptyList, IncorrectCharacter


def validation(tokens: list[str]) -> list[str]:
    """ Функиця для валидации токенов и проверки их на корректность"""

    character_flag = True

    if len(tokens) == 0:
        raise EmptyList(
            f"This list is empty: {tokens} "
        )
    else:
        for i in range(len(tokens)):
            token = tokens[i]
            if character_flag:
                if re.fullmatch(r"[+-]?\d+(?:\.\d+)?", token) is not None:
                    character_flag = False
                else:
                    if token == "-" or token == "+":
                        if i + 1 < len(tokens):
                            if re.fullmatch(r"[+-]?\d+(?:\.\d+)?", tokens[i + 1]) is not None:
                                continue
                            else:
                                raise IncorrectCharacter(
                                    f" Miss Correct sign after {token}"
                                )
                        else:
                            raise IncorrectCharacter(
                                f" Miss Correct sign after {token}"
                            )
                    else:
                        raise IncorrectCharacter(
                            f"Incorrect token: {token}"
                        )

            else:

                if token in "+-/*":
                    character_flag = True
                else:
                    raise IncorrectCharacter(
                        f"Incorrect character: {token}"
                    )

    if character_flag:
        raise IncorrectCharacter(
            " This line ending incorrect character"
        )
    return tokens
