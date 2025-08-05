from http import HTTPStatus

from fastapi import APIRouter

from src.models.REST import GetHealthResponse

router: APIRouter = APIRouter(prefix="/health", tags=["health"])


@router.get("", status_code=HTTPStatus.OK, response_model=GetHealthResponse)
async def get_health() -> GetHealthResponse:
    return GetHealthResponse(status="ok")
