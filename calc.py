"""A tiny calculator — the demo target for a signed SCPE contribution."""


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    """Divide a by b.

    Raises ValueError rather than letting ZeroDivisionError escape, so callers of this
    module only have to handle one error type for bad input.
    """
    if b == 0:
        raise ValueError("cannot divide by zero")
    return a / b
