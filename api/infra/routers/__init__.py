# Import APIRouter
# https://fastapi.tiangolo.com/tutorial/bigger-applications/?h=apirouter#apirouter
from fastapi import APIRouter

# Import task router with all routes configured.
from api.infra.routers.health import router as health_router

# Import task router with all routes configured.
from api.infra.routers.tasks import router as tasks_router

# Import done router with all routes configured.
from api.infra.routers.dones import router as dones_router

# Create an "instance" the same way you would with the class FastAPI
# You can think of APIRouter as a "mini FastAPI" class.
# All the same options are supported.
router = APIRouter()
# Add task router to the main router of the FastAPI application.
router.include_router(health_router, prefix="/healthcheck", tags=["Container Health Check"])
# Add task router to the main router of the FastAPI application.
router.include_router(tasks_router, prefix="/tasks", tags=["Task CRUD Operations"])
# Add done router to the main router of the FastAPI application.
router.include_router(dones_router, prefix="/tasks", tags=["Change Task Status"])
