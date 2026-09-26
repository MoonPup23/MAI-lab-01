from decimal import Decimal

import typer

from toolkit.calculator import calculation
from toolkit.converter import final_convert
from toolkit.errors import CalculatorErrors
from toolkit.tokenization import tokenization
from toolkit.validation import validation

app = typer.Typer()


@app.command()
def calc(expression: str) -> None:
    try:
        tokens = tokenization(expression)
        tokens = validation(tokens)
        result = calculation(tokens)

        typer.echo(result)


    except CalculatorErrors as errors:
        typer.echo(f"Error: {errors}", err=True)
        raise typer.Exit(code=2)


@app.command()
def convert(value: str, from_unit: str = typer.Option(..., "--from"), to_unit: str = typer.Option(..., "--to")):
    try:
        result = final_convert(Decimal(str(value)), from_unit, to_unit)
        typer.echo(result)
    except CalculatorErrors as errors:
        typer.echo(f"Errors: {errors}", err=True)
        raise typer.Exit(code=2)


if __name__ == "__main__":
    app()
