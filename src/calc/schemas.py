from pydantic import BaseModel


class CalcIput(BaseModel):
    numbers: list[int] = []

    class Config:
        from_attributes = True


class CalcOutput(BaseModel):
    sum: int
    average: float

    class Config:
        from_attributes = True
