from pydantic import BaseModel


class CalcIput(BaseModel):
    numbers: list[int] = []

    class Config:
        from_attributes = True


class CalcOutput(BaseModel):
    sum: int = 0
    average: float = 0.0

    class Config:
        from_attributes = True
