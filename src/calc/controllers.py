from logging import getLogger

from fastapi import APIRouter, HTTPException, status

from .schemas import CalcIput, CalcOutput
from .services import NumbersService

logger = getLogger(__name__)


class CalcController:
    def __init__(self) -> None:
        self.router = APIRouter()
        self.service = NumbersService()
        self.router.add_api_route(
            path="/calc/operations/",
            endpoint=self.operations,
            methods=["POST"],
            response_model=CalcOutput,
        )

    async def operations(self, request: CalcIput) -> CalcOutput:
        try:
            payload = request.model_dump_json()
            sum_numbers = await self.service._sum(payload["numbers"])
            average = await self.service._average(payload["numbers"])
            return CalcOutput(sum=sum_numbers, average=average)

        except Exception as exc:
            logger.error(f"Error to create or update vehicle in orchestrator: {exc}")
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail=str(exc)
            ) from exc
