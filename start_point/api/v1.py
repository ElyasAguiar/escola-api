import logging, json
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse

from sqlalchemy.orm import Session

from starlette.responses import RedirectResponse

from start_point.schemas import Aluno, Professor, Titulo
from start_point.repositories.aluno_repository import create_aluno
from start_point.repositories.professor_repository import (
    create_professor,
    get_all_professor,
    query_professor_by_id,
    update_professor_by_id,
    delete_professor_by_id,
)
from start_point.repositories.titulo_repository import (
    create_titulo,
    get_all_titulos,
    query_titulo_by_id,
    update_titulo_by_id,
    delete_titulo_by_id,
)

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
    try:
        create_aluno(db, aluno)
        return aluno
    except Exception as error:
        logging.error("Error: ", error)
        raise {"message": error}


@router.post("/start_point/titulo", name="Cadastrar Titulo")
def post_titulo(titulo: Titulo, db: Session = Depends(get_db)):
    try:
        create_titulo(db, titulo)
        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content={"inserted": True, "data": titulo.dict()},
        )
    except Exception as error:
        logging.error("Error: ", error)
        raise {"message": error}


@router.get("/start_point/titulo", name="Listar todos Titulos")
def get_titulo(db: Session = Depends(get_db)):
    try:
        titulos = get_all_titulos(db)
        return {"data": titulos}
    except Exception as error:
        logging.error("Error: ", error)
        raise {"message": error}


@router.get(
    "/start_point/titulo/{titulo_id}",
    name="Listar todos Titulos",
)
def get_titulo_by_id(titulo_id, db: Session = Depends(get_db)):
    try:
        titulos = query_titulo_by_id(db, int(titulo_id))
        return {"data": titulos}
    except Exception as error:
        logging.error(error.detail)
        raise error


@router.put("/start_point/titulo/{titulo_id}/", name="Editar um título")
async def put_titulo_by_id(
    titulo_id: str, payload: Titulo, db: Session = Depends(get_db)
):
    try:
        titulo = update_titulo_by_id(db, int(titulo_id), payload)
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={"updated": True, "data": titulo},
        )
    except Exception as error:
        logging.error(error)
        raise error


@router.delete("/start_point/titulo/{titulo_id}/", name="Excluir um Título")
def del_titulo_by_id(titulo_id: str, db: Session = Depends(get_db)):
    try:
        titulo = delete_titulo_by_id(titulo_id, db)
        return JSONResponse(
            status_code=status.HTTP_204_NO_CONTENT,
            content={"removed": True},
        )
    except Exception as error:
        logging.error(error.detail)
        raise error


@router.post("/start_point/professor", name="Cadastrar Professor")
def post_professor(professor: Professor, db: Session = Depends(get_db)):
    try:
        create_professor(db, professor)
        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content={"inserted": True, "data": professor.dict()},
        )
    except Exception as error:
        logging.error("Error: ", error)
        raise {"message": error}


@router.get("/start_point/professor", name="Listar todos Professores")
def get_professor(db: Session = Depends(get_db)):
    try:
        professores = get_all_professor(db)
        return {"data": professores}
    except Exception as error:
        logging.error("Error: ", error)
        raise {"message": error}


@router.get(
    "/start_point/professor/{professor_id}",
    name="Retorna um Professor pelo ID",
)
def get_titulo_by_id(professor_id, db: Session = Depends(get_db)):
    try:
        professor = query_professor_by_id(db, professor_id)
        return {"data": professor}
    except Exception as error:
        logging.error(error.detail)
        raise error


@router.put(
    "/start_point/professor/{professor_id}/", name="Editar um professor"
)
async def put_professor_by_id(
    professor_id: str, payload: Professor, db: Session = Depends(get_db)
):
    try:
        professor = update_professor_by_id(db, professor_id, payload)
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={"updated": True, "data": professor},
        )
    except Exception as error:
        logging.error(error)
        raise error


@router.delete(
    "/start_point/professor/{professor_id}/", name="Excluir um Professor"
)
def del_professor_by_id(professor_id: str, db: Session = Depends(get_db)):
    try:
        professor = delete_professor_by_id(professor_id, db)
        return JSONResponse(
            status_code=status.HTTP_204_NO_CONTENT,
            content={"removed": True},
        )
    except Exception as error:
        logging.error(error.detail)
        raise error
