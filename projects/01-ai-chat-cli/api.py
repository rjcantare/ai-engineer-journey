from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from main import run_classification_pipeline

app = FastAPI()


class ClassificationRequest(BaseModel):
    income: int
    dependents: int
    savings: int


@app.post("/classify")
def classify(request: ClassificationRequest):
    try:
        result = run_classification_pipeline(
            monthly_income=request.income,
            dependents=request.dependents,
            current_savings=request.savings
        )
        return result

    except ValueError as e:
        error_message = str(e).lower()

        # 🔹 OpenAI/config related ValueError
        if "openai" in error_message or "api key" in error_message:
            return JSONResponse(
                status_code=503,
                content={
                    "error": "ServiceUnavailable",
                    "message": "AI service temporarily unavailable."
                }
            )

        # 🔹 Validation error
        return JSONResponse(
            status_code=422,
            content={
                "error": "ValidationError",
                "message": str(e)
            }
        )

    except Exception:
        return JSONResponse(
            status_code=500,
            content={
                "error": "InternalServerError",
                "message": "An unexpected error occurred."
            }
        )