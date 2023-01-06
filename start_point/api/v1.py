import logging
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from starlette.responses import RedirectResponse

from start_point.schemas import Aluno
from start_point.repositories.aluno_repository import create_aluno

from app.database import SessionLocal

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", include_in_schema=False)
def get_swagger():
    return RedirectResponse(url="/docs")


@router.get("/start_point/health", name="health")
def get_start_point():
    return {"health": "check!"}


@router.post("/start_point/create_aluno", name="Cadastrar Aluno")
def post_aluno(aluno: Aluno, db: Session = Depends(get_db)):
    logging.info("Aqui: ", aluno)
    try:
        create_aluno(db, aluno)
        return aluno
    except Exception as error:
        logging.error("Error: ", error)
        return {"message": str(error)}
