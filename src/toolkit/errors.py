class CalculatorErrors(Exception):
    pass


class UnknownCharError(CalculatorErrors):
    pass


class EmptyList(CalculatorErrors):
    pass


class IncorrectCharacter(CalculatorErrors):
    pass


class DivisionByZero(CalculatorErrors):
    pass


class IncorrectUnit(CalculatorErrors):
    pass


class AbsoluteZero(CalculatorErrors):
    pass


class IncompatibleUnits(CalculatorErrors):
    pass
