from fastapi import FastAPI
from routes.store import drinks
from config.openapi import tags_metadata

app = FastAPI(
    title="Store API",
    description="a REST API using python and mysql",
    version="0.0.1",
    openapi_tags=tags_metadata,
)

app.include_router(drinks)

