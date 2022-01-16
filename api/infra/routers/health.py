from fastapi import APIRouter, Request, status, Header
from typing import Optional, Dict
from api.core.logging import logger

router = APIRouter()


@router.get(
    "/",
    response_model=Dict[str, str],
    name="health:health_check",
    status_code=status.HTTP_200_OK,
)
async def health_check(
    request: Request,
    authorization: Optional[str] = Header(None),
) -> Dict[str, str]:
    logger.info(f"request.headers: {request.headers}")
    logger.info(f"authorization: {authorization}")
    return {"message": "Container health check was successful!"}
