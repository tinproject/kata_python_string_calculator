import pytest

from string_calculator import StringCalculator


@pytest.fixture
def sc():
    return StringCalculator()


@pytest.mark.parametrize("numbers,output", [
    ("", 0),
    ("1", 1),
    ("1,2", 3),
    ("1,2,3,4,5,6,7,8", 36),
    ("5,556,321,21,7,78", 988),
])
def test_add_numbers(sc, numbers, output):
    result = sc.add(numbers)

    assert result == output
