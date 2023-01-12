from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    ForeignKey,
    Float,
    Boolean,
)
from sqlalchemy.orm import relationship

from app.database import Base


"""class Company(Base):
    __tablename__ = "company"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    cnpj = Column(String(14), index=True)
    nome = Column(String, index=True)
    razao_social = Column(String, index=True)
    endereco = Column(Text, index=True)
    email = Column(String, index=True)
    telefone = Column(String(14), index=True)"""


class Aluno(Base):
    __tablename__ = "aluno"

    id_aluno = Column(
        Integer, primary_key=True, autoincrement=True, index=True
    )
    tx_nome = Column(String, index=True)
    tx_sexo = Column(String, index=True)
    dt_nascimento = Column(String, index=True)

    class Config:
        orm_mode = True


class Professor(Base):
    __tablename__ = "professor"

    id_professor = Column(
        Integer, primary_key=True, autoincrement=True, index=True
    )
    id_titulo = Column(Integer, ForeignKey("titulo.id_titulo"))
    tx_nome = Column(String, index=True)
    tx_sexo = Column(String, index=True)
    tx_estado_civil = Column(String, index=True)
    dt_nascimento = Column(String, index=True)
    tx_telefone = Column(String, index=True)

    fk_titulo_to_professor = relationship("Titulo")

    class Config:
        orm_mode = True


class Titulo(Base):
    __tablename__ = "titulo"

    id_titulo = Column(
        Integer, primary_key=True, autoincrement=True, index=True
    )
    tx_descricao = Column(String, index=True)

    class Config:
        orm_mode = True


"""class Cursa(Base):
    __tablename__ = "cursa"

    id_aluno = Column(Integer, ForeignKey("aluno.id_aluno"))
    id_disciplina = Column(Integer, ForeignKey("disciplina.id_disciplina"))
    in_ano = Column(Integer)
    in_semestre = Column(Integer)
    in_faltas = Column(Integer)
    nm_nota1 = Column(Float)
    nm_nota2 = Column(Float)
    nm_nota3 = Column(Float)
    bl_aprovado = Column(Boolean)

    fk_aluno_to_cursa = relationship("Disciplina")
    fk_disciplina_to_cursa = relationship("Disciplina")

    class Config:
        orm_mode = True


class Curso(Base):
    __tablename__ = "curso"

    id_curso = Column(Integer, primary_key=True, autoincrement=True, index=True)
    id_instituicao = Column(Integer, ForeignKey("instituicao.id_instituicao"))
    id_tipo_curso = Column(Integer, ForeignKey("tipo_curso.id_tipo_curso"))
    tx_descricao = Column(String, index=True)

    fk_instituicao_to_curso = relationship("Instituicao")
    fk_tipo_curso_to_curso = relationship("Instituicao")

    class Config:
        orm_mode = True


class Disciplina(Base):
    __tablename__ = "disciplina"

    id_disciplina = Column(
        Integer, primary_key=True, autoincrement=True, index=True
    )
    id_curso = Column(Integer, ForeignKey("curso.id_curso"))
    id_tipo_disciplina = Column(
        Integer, ForeignKey("tipo_disciplina.id_tipo_disciplina")
    )
    tx_sigla = Column(String, index=True)
    tx_descricao = Column(String, index=True)
    in_periodo = Column(Integer)
    in_carga_horaria = Column(Integer)

    fk_tipo_disciplina_to_disciplina = relationship("TipoDisciplina")
    fk_curso_to_disciplina = relationship("Curso")

    class Config:
        orm_mode = True


class Instituicao(Base):
    __tablename__ = "instituicao"

    id_instituicao = Column(
        Integer, primary_key=True, autoincrement=True, index=True
    )
    tx_sigla = Column(String, index=True)
    tx_descricao = Column(String, index=True)

    class Config:
        orm_mode = True


class Leciona(Base):
    __tablename__ = "leciona"

    id_professor = Column(Integer, ForeignKey("professor.id_professor"))
    id_disciplina = Column(Integer, ForeignKey("disciplina.id_disciplina"))

    fk_professor_to_leciona = relationship("Professor")
    fk_disciplina_to_cursa = relationship("Disciplina")

    class Config:
        orm_mode = True

class TipoCurso(Base):
    __tablename__ = "tipo_curso"

    id_tipo_curso = Column(
        Integer, primary_key=True, autoincrement=True, index=True
    )
    tx_descricao = Column(String, index=True)

    class Config:
        orm_mode = True


class TipoDisciplina(Base):
    __tablename__ = "tipo_disciplina"

    id_tipo_disciplina = Column(
        Integer, primary_key=True, autoincrement=True, index=True
    )
    tx_descricao = Column(String, index=True)

    class Config:
        orm_mode = True



"""
