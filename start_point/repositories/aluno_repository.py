import logging
from sqlmodel import Session

from start_point import schemas
from start_point.models import models


def create_aluno(db: Session, aluno: schemas.Aluno):
    try:
        data_aluno = models.Aluno(
            tx_nome=aluno.tx_nome,
            tx_sexo=aluno.tx_sexo,
            dt_nascimento=aluno.dt_nascimento,
        )
        response = db.add(data_aluno)
        db.commit()
        db.refresh(data_aluno)
        return response
    except Exception as error:
        logging.error(error)
        raise error
