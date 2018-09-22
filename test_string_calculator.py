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
    ("1\n2,3", 6),
    ("1\n2\n3,5\n5", 16),
    ("5,1\n2\n3\n5", 16),
])
def test_add_numbers(sc, numbers, output):
    result = sc.add(numbers)

    assert result == output


@pytest.mark.parametrize("numbers,output", [
    ("//;\n1;2", 3),
    ("//j\n1\n2j3", 6),
    ("//j\n1\n2\n3j5\n5", 16),
    ("//j\n5j1\n2\n3\n5", 16)
])
def test_add_numbers_step4(sc, numbers, output):
    result = sc.add(numbers)

    assert result == output


@pytest.mark.parametrize("numbers,negative_numbers", [
    ("1\n2,-2", "-2"),
    ("1,2,-3,4,-5,-6,7,8", "-3,-5,-6"),
    ("//j\n1\n-2\n3j5\n5", "-2"),
    ("//j\n5j1\n-2\n3\n5", "-2")
])
def test_add_numbers_step5(sc, numbers, negative_numbers):

    with pytest.raises(ValueError) as excinfo:
        sc.add(numbers)

    assert "negativos no soportados" in str(excinfo.value)
    assert negative_numbers in str(excinfo.value)
