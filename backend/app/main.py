from fastapi import FastAPI

from app.api.routes.health import router as health_router


app = FastAPI(
    title="Solar Panel Defect & Output Degradation Forecaster",
    description="API for solar panel defect analysis and power degradation forecasting.",
    version="0.1.0"
)


app.include_router(health_router)