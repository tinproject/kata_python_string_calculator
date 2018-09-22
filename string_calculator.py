# Solution to http://www.solveet.com/exercises/Kata-String-Calculator/8
from typing import List, Union, Tuple


def extract_delimiters(delimiter_line: str) -> List[str]:
    """
    Extract the delimiters from a delimiter line
    :param delimiter_line: the line that define the delimiters
    :return: a list of delimiters
    """
    DEFAULT_DELIMITER = ","
    if not delimiter_line.startswith('//'):
        return [DEFAULT_DELIMITER]

    delimiter_line = delimiter_line[2:]  # Remove delimiter line mark

    # only one delmiter
    if "[" not in delimiter_line and "]" not in delimiter_line:
        delimiters = [delimiter_line]
        return delimiters

    # Multiple character delimiters
    if delimiter_line.startswith("[") and delimiter_line.endswith("]"):
        delimiters = [str.lstrip(d, "[") for d in delimiter_line.split("]") if d]
        return delimiters

    raise ValueError("This is not a valid delimiter line")


def get_numbers_from_string(numbers_string: str) -> List[int]:
    """
    This function extract a list of numbers from a string according to kata text
    :param numbers_string: the numbers string
    :return: list of integer numbers
    """

    lines = numbers_string.splitlines()

    has_delimiters = lines[0].startswith('//')

    delimiters = extract_delimiters(lines[0]) if has_delimiters else [',']  # Default delimiter
    numbers_str = lines[1:] if has_delimiters else lines

    # Split numbers by delimiters
    for delimiter in delimiters:
        numbers_str = [s for line in numbers_str for s in line.split(delimiter)]

    # Transform string numbers to integers
    number_list = [int(n) for n in numbers_str]
    return number_list


def add(numbers: str) -> int:
    if not numbers:
        return 0

    number_list = get_numbers_from_string(numbers)

    negative_numbers = list(filter(lambda x: x < 0, number_list))
    if len(negative_numbers) > 0:
        raise ValueError("negativos no soportados {}".format(",".join(map(str, negative_numbers))))

    number_list = filter(lambda n: n <= 1000, number_list)

    return sum(number_list)
