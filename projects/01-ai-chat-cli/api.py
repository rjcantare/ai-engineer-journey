from fastapi import FastAPI
from pydantic import BaseModel

from main import run_classification_pipeline

app = FastAPI()


class ClassificationRequest(BaseModel):
    income: int
    dependents: int
    savings: int


@app.post("/classify")
def classify(request: ClassificationRequest):
    result = run_classification_pipeline(
        monthly_income=request.income,
        dependents=request.dependents,
        current_savings=request.savings
    )

    return result