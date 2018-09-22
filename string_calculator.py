# Solution to http://www.solveet.com/exercises/Kata-String-Calculator/8


class StringCalculator:
    def add(self, numbers: str) -> int:
        if not numbers:
            return 0

        lines = numbers.splitlines()
        delimiter = ","

        if lines[0].startswith("//"):
            delimiter = lines[0][2:]
            lines = lines[1:]

        number_list = [int(n) for line in lines for n in line.split(delimiter)]

        negative_numbers = list(filter(lambda x: x < 0, number_list))
        if len(negative_numbers) > 0:
            raise ValueError("negativos no soportados {}".format(",".join(map(str, negative_numbers))))

        return sum(number_list)
