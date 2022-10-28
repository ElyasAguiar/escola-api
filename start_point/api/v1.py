from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def get_start_point():
    return "start_point app created!"
