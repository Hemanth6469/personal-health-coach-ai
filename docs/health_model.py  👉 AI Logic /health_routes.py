from fastapi import APIRouter
from app.schemas.health_schema import HealthData
from app.models.health_model import analyze_health
from app.database.db import save_health_data

router = APIRouter()

@router.get("/")
def home():
    return {"message": "Personal Health Coach AI Running"}

@router.post("/analyze")
def analyze(data: HealthData):

    recommendations, score = analyze_health(
        data.age,
        data.steps,
        data.sleep_hours,
        data.water_intake
    )

    # Save Data
    save_health_data(data.dict())

    return {
        "health_score": score,
        "recommendations": recommendations
    }
