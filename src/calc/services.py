class NumberService:
    @staticmethod
    def _sum(a: int, b: int) -> int:
        """
        Sum two numbers and return the result
        :param a: int
        :param b: int
        :return: int
        """
        return a + b

    @staticmethod
    def _divide(a: int, b: int) -> float:
        """
        Divide two numbers and return the result
        :param a: int
        :param b: int
        :return: float
        """
        return a / b


class NumbersService:
    @staticmethod
    def _sum(numbers: list[int] = []) -> int:
        """
        Sum a list of numbers and return the result
        :param numbers: list[int]
        :return: int
        """
        result = 0
        number_service = Number()
        for number in numbers:
            result += number_service._sum(result, number)
        return result

    def _average(self, numbers: list[int] = []) -> float:
        """
        Calculate the average of a list of numbers and return the result
        :param numbers: list[int]
        :return: float
        """
        number_service = Number()
        sum_numbers = self._sum(numbers)
        quantity_numbers = len(numbers)
        return number_service._divide(sum_numbers, quantity_numbers)
