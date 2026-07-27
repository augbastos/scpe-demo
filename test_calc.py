import pytest

from calc import add, div, mul, sub


def test_add():
    assert add(2, 3) == 5


def test_sub():
    assert sub(5, 3) == 2


def test_mul():
    assert mul(4, 3) == 12


def test_div():
    assert div(9, 3) == 3


def test_div_by_zero_raises_value_error():
    with pytest.raises(ValueError):
        div(1, 0)
