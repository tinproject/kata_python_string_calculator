# Solution to http://www.solveet.com/exercises/Kata-String-Calculator/8


class StringCalculator:
    def add(self, numbers: str) -> int:
        if not numbers:
            return 0

        number_list = (int(n) for line in numbers.splitlines() for n in line.split(","))
        return sum(number_list)
