from fastapi import APIRouter
from starlette.responses import RedirectResponse

router = APIRouter()


@router.get("/", include_in_schema=False)
def get_swagger():
    return RedirectResponse(url="/docs")


@router.get("/start_point/health", name="health")
def get_start_point():
    return {"health": "check!"}
