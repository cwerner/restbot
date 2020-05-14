from fastapi import APIRouter, Depends
from starlette.requests import Request

from restbot.core import security
from restbot.models.payload import HousePredictionPayload
from restbot.models.prediction import HousePredictionResult
from restbot.services.models import HousePriceModel

router = APIRouter()


@router.post("/predict", response_model=HousePredictionResult, name="predict")
def post_predict(
    request: Request,
    authenticated: bool = Depends(security.validate_request),
    block_data: HousePredictionPayload = None
) -> HousePredictionResult:

    model: HousePriceModel = request.app.state.model
    prediction: HousePredictionResult = model.predict(block_data)

    return prediction
