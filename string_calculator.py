# Solution to http://www.solveet.com/exercises/Kata-String-Calculator/8


class StringCalculator:
    def add(self, numbers):
        if not numbers:
            return 0

        number_list = [int(n) for n in numbers.split(",")]
        return sum(number_list)
