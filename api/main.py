from fastapi import FastAPI

# Import logging | Logging package for Python.
import logging

from api.routers import task, done
from api.session import connect_to_db, close_db_connection

# Set the logging level of this logger for uvicorn.
logger = logging.getLogger("uvicorn")
logger.setLevel(logging.INFO)

app = FastAPI()
@app.on_event("startup")
async def startup():
    logger.info("[startup]database.connect")
    await connect_to_db(app)


@app.on_event("shutdown")
async def shutdown():
    logger.info("[shutdown]database.disconnect")
    logger.info("app.state._db")
    logger.info(app.state._db)
    await close_db_connection(app)

# task router インスタンスを、FastAPIインスタンスに取り込む
app.include_router(task.router)
# done router インスタンスを、FastAPIインスタンスに取り込む
app.include_router(done.router)