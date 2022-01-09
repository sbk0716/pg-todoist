from fastapi import FastAPI
import logging
from api.routers import task
from api.db.connection import connect_to_db, close_db_connection

# Set the logging level of this logger for uvicorn.
logger = logging.getLogger("uvicorn")
logger.setLevel(logging.INFO)

app = FastAPI()
@app.on_event("startup")
async def startup():
    """
    startup function
    """
    logger.info("[startup]database.connect")
    await connect_to_db(app)

@app.on_event("shutdown")
async def shutdown():
    """
    shutdown function
    """
    logger.info("[shutdown]database.disconnect")
    await close_db_connection(app)


app.include_router(task.router)
# app.include_router(done.router)