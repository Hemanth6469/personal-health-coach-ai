from pydantic import BaseModel

class HealthData(BaseModel):
    age: int
    steps: int
    sleep_hours: float
    water_intake: float
