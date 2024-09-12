from calc.services import NumberService, NumbersService


class TestNumberService:
    async def test_sum(self):
        a = 1
        b = 2
        service = NumberService()
        result = await service._sum(a=a, b=b)
        assert result == 3

    async def test_divide(self):
        a = 1
        b = 2
        service = NumberService()
        result = await service._divide(a=a, b=b)
        assert result == 0.5


class TestNumbersService:
    async def test_sum(self):
        numbers = [1, 2, 3, 4, 5]
        service = NumbersService()
        result = await service._sum(numbers=numbers)
        assert result == 15

    async def test_sum_with_result_zero(self):
        numbers = []
        service = NumbersService()
        result = await service._sum(numbers=numbers)
        assert result == 0

    async def test_average(self):
        numbers = [1, 2, 3, 4, 5]
        service = NumbersService()
        result = await service._average(numbers=numbers)
        assert result == 3.0

    async def test_average_with_result_zero(self):
        numbers = []
        service = NumbersService()
        result = await service._average(numbers=numbers)
        assert result == 0.0

    async def test_average_with_sum_zero(self):
        numbers = [0, 0, 0]
        service = NumbersService()
        result = await service._average(numbers=numbers)
        assert result == 0.0
