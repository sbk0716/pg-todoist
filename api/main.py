from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.core import environ
from api.infra.routers import router as api_router
from api.infra.db.connection import connect_to_db, close_db_connection

# An instance of the class FastAPI will be the main point of interaction to create all your API.
# https://fastapi.tiangolo.com/tutorial/first-steps/#step-2-create-a-fastapi-instance
app = FastAPI(
    title=environ.PROJECT_NAME,
    description=environ.DESCRIPTION,
    version=environ.VERSION,
    docs_url="/docs",
    redoc_url="/redoc",
)

# Create a list of allowed origins (as strings).
origins = [
    # "http://grasswood.tk",
    # "https://grasswood.tk",
    "http://localhost"
]

# Add the parameter as a "middleware" to your FastAPI application.
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # A list of origins that should be permitted to make cross-origin requests.
    allow_credentials=True,  # Indicate that cookies should be supported for cross-origin requests.
    allow_methods=["*"],  # A list of HTTP methods that should be allowed for cross-origin requests.
    allow_headers=[
        "*"
    ],  # A list of HTTP request headers that should be supported for cross-origin requests.
)

# Add api router with all routes configured to your FastAPI application.
app.include_router(api_router, prefix=environ.API_PREFIX)


# Add a function that should be run before the application starts.
@app.on_event("startup")
async def startup():
    """
    startup function
    """
    await connect_to_db(app)


# Add a function that should be run when the application is shutting down.
@app.on_event("shutdown")
async def shutdown():
    """
    shutdown function
    """
    await close_db_connection(app)
