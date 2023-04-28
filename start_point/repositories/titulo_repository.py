import logging

from fastapi import status, HTTPException
from sqlalchemy import asc

from sqlmodel import Session
from start_point import schemas
from start_point.models import models


def create_titulo(db: Session, titulo: schemas.Titulo):
    try:
        data_titulo = models.Titulo(
            tx_descricao=titulo.tx_descricao,
        )
        response = db.add(data_titulo)
        db.commit()
        db.refresh(data_titulo)
        return response
    except Exception as error:
        logging.error(error)
        raise error


def get_all_titulos(db: SessionLocal, search: str = ""):
    try:
        titulos = (
            db.query(models.Titulo)
            .filter(models.Titulo.tx_descricao.contains(search))
            .order_by(asc(models.Titulo.id_titulo))
            .all()
        )
        return titulos
    except Exception as error:
        logging.error(error)
        raise error


def query_titulo_by_id(db: SessionLocal, titulo_id: int):
    try:
        titulo = (
            db.query(models.Titulo)
            .filter(models.Titulo.id_titulo == titulo_id)
            .first()
        )
        if not titulo:
            response = HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={
                    "status_code": status.HTTP_404_NOT_FOUND,
                    "message": f"Nenhum titulo com este id: {titulo_id} foi encontrado.",
                },
            )
            raise response
        return titulo
    except Exception as error:
        logging.error(error)
        raise error


def update_titulo_by_id(
    db: SessionLocal, titulo_id: int, payload: schemas.Titulo
):
    try:
        titulo_query = db.query(models.Titulo).filter(
            models.Titulo.id_titulo == titulo_id
        )
        db_titulo = titulo_query.first()
        if not db_titulo:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={
                    "status_code": status.HTTP_404_NOT_FOUND,
                    "message": f"Nenhum titulo com este id: {titulo_id} foi encontrado.",
                },
            )
        update_data = payload.dict(exclude_unset=True)
        titulo_query.filter(models.Titulo.id_titulo == titulo_id).update(
            update_data, synchronize_session=False
        )
        db.commit()
        db.refresh(db_titulo)
        return {
            "id_titulo": db_titulo.id_titulo,
            "tx_descricao": db_titulo.tx_descricao,
        }
    except Exception as error:
        logging.error(error)
        raise error


def delete_titulo_by_id(titulo_id: str, db: SessionLocal):
    titulo_query = db.query(models.Titulo).filter(
        models.Titulo.id_titulo == titulo_id
    )
    titulo = titulo_query.first()
    if not titulo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                "status_code": status.HTTP_404_NOT_FOUND,
                "message": f"Nenhum titulo com este id: {titulo_id} foi encontrado.",
            },
        )
    titulo_query.delete(synchronize_session=False)
    db.commit()
    return titulo
