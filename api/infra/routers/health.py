from fastapi import APIRouter, status
from typing import Dict

router = APIRouter()


@router.get(
    "/",
    response_model=Dict[str, str],
    name="health:health_check",
    status_code=status.HTTP_200_OK,
)
async def health_check() -> Dict[str, str]:
    return {"message": "Container health check was successful!"}
