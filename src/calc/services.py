class NumberService:
    @staticmethod
    async def _sum(a: int, b: int) -> int:
        """
        Sum two numbers and return the result
        :param a: int
        :param b: int
        :return: int
        """
        return a + b

    @staticmethod
    async def _divide(a: int, b: int) -> float:
        """
        Divide two numbers and return the result
        :param a: int
        :param b: int
        :return: float
        """
        return a / b


class NumbersService:
    def __init__(self) -> None:
        self.number_service = NumberService()

    async def _sum(self, numbers: list[int] = []) -> int:
        """
        Sum a list of numbers and return the result
        :param numbers: list[int]
        :return: int
        """
        if not numbers:
            return 0

        result = numbers[0]
        for i in range(1, len(numbers)):
            result = await self.number_service._sum(result, numbers[i])

        return result

    async def _average(self, numbers: list[int] = []) -> float:
        """
        Calculate the average of a list of numbers and return the result
        :param numbers: list[int]
        :return: float
        """
        if not numbers:
            return 0.0

        sum_numbers = await self._sum(numbers)
        quantity_numbers = len(numbers)

        if sum_numbers == 0:
            return 0.0

        return await self.number_service._divide(sum_numbers, quantity_numbers)
