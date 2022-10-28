from fastapi import APIRouter

router = APIRouter()


@router.get("/start_point/")
def get_start_point():
    return {"health": "check!"}
