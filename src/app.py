from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from calc.controllers import CalcController


def create_app():

    app = FastAPI(
        title="Calc",
        description="A simple calculator API",
        version="0.1.0",
    )
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(
        CalcController().router,
        tags=["calc"],
        prefix="/api/v1",
    )

    @app.get("/", status_code=200, include_in_schema=False)
    async def health_check():
        return {"status": "ok"}

    return app
