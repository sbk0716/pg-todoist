# Import APIRouter
# https://fastapi.tiangolo.com/tutorial/bigger-applications/?h=apirouter#apirouter
from fastapi import APIRouter

# Import task router with all routes configured.
from api.infra.routers.task import router as task_router

# Import done router with all routes configured.
# from api.infra.routers.done import router as done_router

# Create an "instance" the same way you would with the class FastAPI
# You can think of APIRouter as a "mini FastAPI" class.
# All the same options are supported.
router = APIRouter()
# Add task router to the main router of the FastAPI application.
router.include_router(task_router, prefix="/tasks", tags=["Task CRUD Operations"])
# Add done router to the main router of the FastAPI application.
# router.include_router(done_router, prefix="/tasks", tags=["Change Task Status"])
