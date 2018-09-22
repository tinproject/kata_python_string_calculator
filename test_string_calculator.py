import pytest

from string_calculator import StringCalculator


@pytest.fixture
def sc():
    return StringCalculator()


@pytest.mark.parametrize("numbers,output", [
    ("", 0),
    ("1", 1),
    ("1,2", 3),
])
def test_add_numbers(sc, numbers, output):
    result = sc.add(numbers)

    assert result == output
