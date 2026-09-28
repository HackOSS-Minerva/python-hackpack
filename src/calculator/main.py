"""Entry point for the calculator package"""

from calculator.utils import add, divide, multiply, subtract


def main() -> None:
    """Run a small demo of the calculator utilities."""
    a, b = 10, 5
    print(f"{a} + {b} = {add(a, b)}")
    print(f"{a} - {b} = {subtract(a, b)}")
    print(f"{a} * {b} = {multiply(a, b)}")
    print(f"{a} / {b} = {divide(a, b)}")
