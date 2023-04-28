import logging

from fastapi import HTTPException, status
from sqlalchemy import asc
from sqlmodel import Session

from start_point import schemas
from start_point.models import models


def create_professor(db: Session, professor: schemas.Professor):
    try:
        data_professor = models.Professor(
            id_titulo=professor.id_titulo,
            tx_nome=professor.tx_nome,
            tx_sexo=professor.tx_sexo,
            tx_estado_civil=professor.tx_estado_civil,
            dt_nascimento=professor.dt_nascimento,
            tx_telefone=professor.tx_telefone,
        )
        response = db.add(data_professor)
        db.commit()
        db.refresh(data_professor)
        return response
    except Exception as error:
        logging.error(error)
        raise error


def get_all_professor(db: Session, search: str = ""):
    try:
        professor = (
            db.query(models.Professor)
            .filter(models.Professor.tx_nome.contains(search))
            .order_by(asc(models.Professor.id_professor))
            .all()
        )
        return professor
    except Exception as error:
        logging.error(error)
        raise error


def query_professor_by_id(db: Session, professor_id: int):
    try:
        professor = (
            db.query(models.Professor)
            .filter(models.Professor.id_professor == professor_id)
            .first()
        )
        if not professor:
            response = HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={
                    "status_code": status.HTTP_404_NOT_FOUND,
                    "message": f"Nenhum professor com este id: {professor_id} foi encontrado.",
                },
            )
            raise response
        return professor
    except Exception as error:
        logging.error(error)
        raise error


def update_professor_by_id(
    db: Session, professor_id: int, payload: schemas.Professor
):
    try:
        professor_query = db.query(models.Professor).filter(
            models.Professor.id_professor == professor_id
        )
        db_professor = professor_query.first()
        if not db_professor:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={
                    "status_code": status.HTTP_404_NOT_FOUND,
                    "message": f"Nenhum professor com este id: {professor_id} foi encontrado.",
                },
            )
        update_data = payload.dict(exclude_unset=True)
        professor_query.filter(
            models.Professor.id_professor == professor_id
        ).update(update_data, synchronize_session=False)
        db.commit()
        db.refresh(db_professor)
        return {
            "id_professor": db_professor.id_professor,
            "nome": db_professor.tx_nome,
        }
    except Exception as error:
        logging.error(error)
        raise error


def delete_professor_by_id(professor_id: str, db: Session):
    professor_query = db.query(models.Professor).filter(
        models.Professor.id_professor == professor_id
    )
    professor = professor_query.first()
    if not professor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                "status_code": status.HTTP_404_NOT_FOUND,
                "message": f"Nenhum professor com este id: {professor_id} foi encontrado.",
            },
        )
    professor_query.delete(synchronize_session=False)
    db.commit()
    return professor
