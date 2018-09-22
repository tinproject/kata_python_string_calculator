import pytest

from string_calculator import add, extract_delimiters


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
def test_add_numbers(numbers, output):
    result = add(numbers)

    assert result == output


@pytest.mark.parametrize("numbers,output", [
    ("//;\n1;2", 3),
    ("//j\n1\n2j3", 6),
    ("//j\n1\n2\n3j5\n5", 16),
    ("//j\n5j1\n2\n3\n5", 16)
])
def test_add_numbers_step4(numbers, output):
    result = add(numbers)

    assert result == output


@pytest.mark.parametrize("numbers,negative_numbers", [
    ("1\n2,-2", "-2"),
    ("1,2,-3,4,-5,-6,7,8", "-3,-5,-6"),
    ("//j\n1\n-2\n3j5\n5", "-2"),
    ("//j\n5j1\n-2\n3\n5", "-2")
])
def test_add_numbers_step5(numbers, negative_numbers):

    with pytest.raises(ValueError) as excinfo:
        add(numbers)

    assert "negativos no soportados" in str(excinfo.value)
    assert negative_numbers in str(excinfo.value)


@pytest.mark.parametrize("numbers,output", [
    ("2000", 0),
    ("1,2000", 1),
    ("1,2,3,4,1001,5,6,7,8", 36),
    ("5,556,321, 1000,21,7,78", 1988),
])
def test_add_numbers_step6(numbers, output):
    result = add(numbers)

    assert result == output


@pytest.mark.parametrize("numbers,output", [
    ("//[***]\n1***2***3", 6),
])
def test_add_numbers_step7(numbers, output):
    result = add(numbers)

    assert result == output


@pytest.mark.parametrize("numbers,out_lines,delimiters", [
    ("//[*][%]\n1*2%3", ["1*2%3"], ["*", "%"]),
    ("//[jer]\n1\n2jer3", ["1", "2jer3"], ["jer"]),
    ("//d\n5d1\n2\n3", ["5d1", "2", "3"], ["d"])
])
def test_extract_delimiters(numbers, out_lines, delimiters):

    assert out_lines, delimiters == extract_delimiters(numbers)


@pytest.mark.parametrize("numbers,output", [
    ("//[*][%]\n1*2%3", 6),
    ("//[jer]\n1\n2jer3", 6),
    ("//[delimiter][f]\n5delimiter1\n2f5\n3\n5", 21)
])
def test_add_numbers_step8(numbers, output):
    result = add(numbers)

    assert result == output


@pytest.mark.parametrize("numbers,output", [
    ("//;\n1;2", 3),
    ("//je\n1\n2je3", 6),
    ("//delim\n1\n2\n3delim5\n5", 16),
])
def test_add_numbers_step9(numbers, output):
    result = add(numbers)

    assert result == output