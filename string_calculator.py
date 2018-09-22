# Solution to http://www.solveet.com/exercises/Kata-String-Calculator/8
from typing import List, Optional, Union, Tuple


def extract_delimiter(lines: List[str]) -> Tuple[List[str], Union[str, List[str]]]:
    DEFAULT_DELIMITER = ","
    if not lines[0].startswith('//'):
        return lines, [DEFAULT_DELIMITER]

    first_line = lines[0]
    lines = lines[1:]

    delimiter_line = first_line[2:]  # Remove delimiter line mark

    # normal one character delimiters
    if len(delimiter_line) == 1:
        delimiters = [delimiter_line]
        return lines, delimiters

    # Multiple character delimiters
    if delimiter_line.startswith("[") and delimiter_line.endswith("]"):
        delimiters = [delimiter_line[1:-1]]
        return lines, delimiters

    raise ValueError("This is not a valid delimiter line")


class StringCalculator:
    def add(self, numbers: str) -> int:
        if not numbers:
            return 0

        lines = numbers.splitlines()

        lines, delimiters = extract_delimiter(lines)

        number_list = [int(n) for line in lines for d in delimiters for n in line.split(d)]

        negative_numbers = list(filter(lambda x: x < 0, number_list))
        if len(negative_numbers) > 0:
            raise ValueError("negativos no soportados {}".format(",".join(map(str, negative_numbers))))

        number_list = filter(lambda n: n <= 1000, number_list)

        return sum(number_list)
