from http import HTTPStatus

from fastapi import APIRouter

router: APIRouter = APIRouter(prefix="/health", tags=["health"])


@router.get("", status_code=HTTPStatus.OK)
async def health_check() -> dict[str, str]:
    return {"status": "ok"}
