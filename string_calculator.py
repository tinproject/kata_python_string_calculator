# Solution to http://www.solveet.com/exercises/Kata-String-Calculator/8
from typing import List, Union, Tuple


def extract_delimiters(lines: List[str]) -> Tuple[List[str], Union[str, List[str]]]:
    DEFAULT_DELIMITER = ","
    if not lines[0].startswith('//'):
        return lines, [DEFAULT_DELIMITER]

    first_line = lines[0]
    lines = lines[1:]

    delimiter_line = first_line[2:]  # Remove delimiter line mark

    # only one delmiter
    if "[" not in delimiter_line and "]" not in delimiter_line:
        delimiters = [delimiter_line]
        return lines, delimiters

    # Multiple character delimiters
    if delimiter_line.startswith("[") and delimiter_line.endswith("]"):
        delimiters = [str.lstrip(d, "[") for d in delimiter_line.split("]") if d]
        return lines, delimiters

    raise ValueError("This is not a valid delimiter line")


class StringCalculator:
    def add(self, numbers: str) -> int:
        if not numbers:
            return 0

        lines = numbers.splitlines()

        # Split numbers by line
        numbers_str, delimiters = extract_delimiters(lines)

        # Split numbers by delimiters
        for delimiter in delimiters:
            numbers_str = [s for line in numbers_str for s in line.split(delimiter)]

        # Transform string numbers to integers
        number_list = [int(n) for n in numbers_str]

        negative_numbers = list(filter(lambda x: x < 0, number_list))
        if len(negative_numbers) > 0:
            raise ValueError("negativos no soportados {}".format(",".join(map(str, negative_numbers))))

        number_list = filter(lambda n: n <= 1000, number_list)

        return sum(number_list)
