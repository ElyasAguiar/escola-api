from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi

from app.core.config import settings
from start_point.api.v1 import router as start_point


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Escola Api",
        version="0.0.1",
        description="Esse é o swagger contendo os schemas da Escola Api.",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


def get_application():
    _app = FastAPI(title=settings.PROJECT_NAME)

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            str(origin) for origin in settings.BACKEND_CORS_ORIGINS
        ],
        allow_credentials=True,
        allow_methods=[
            "POST",
            "GET",
            "PUT",
            "PATCH",
            "DEL",
            "DELETE",
            "OPTIONS",
        ],
        allow_headers=["*"],
    )
    _app.include_router(start_point)
    return _app


app = get_application()
app.openapi = custom_openapi
