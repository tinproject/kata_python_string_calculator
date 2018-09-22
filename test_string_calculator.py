import pytest

from string_calculator import StringCalculator


@pytest.fixture
def sc():
    return StringCalculator()


def test_add_no_numbers(sc):
    numbers = ""

    result = sc.add(numbers)

    assert result == 0


def test_add_one_numbers(sc):
    numbers = "1"

    result = sc.add(numbers)

    assert result == 1


def test_add_two_numbers(sc):
    numbers = "1,2"

    result = sc.add(numbers)

    assert result == 3
