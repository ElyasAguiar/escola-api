from pydantic import BaseModel


"""class Company(BaseModel):
    # id: int
    cnpj: str
    nome: str
    razao_social: str
    endereco: str
    email: str
    telefone: str

    @validator("email")
    def validate_email(cls, email):
        regex = r"[^ @]+@[^ @]+\.[^ @]+"
        if not re.match(regex, email):
            raise ValueError("Email inválido!")

        return email

    class Config:
        orm_mode = True"""


class Aluno(BaseModel):
    tx_nome: str
    tx_sexo: str
    dt_nascimento: str

    class Config:
        orm_mode = True


"""class Cursa(BaseModel):
    id_aluno: int
    id_disciplina: int
    in_ano: int
    in_semestre: int
    in_faltas: int
    nm_nota1: float
    nm_nota2: float
    nm_nota3: float
    bl_aprovado: bool

    class Config:
        orm_mode = True


class Curso(BaseModel):
    id_curso: int
    id_instituicao: int
    id_tipo_curso: int
    tx_descricao: str

    class Config:
        orm_mode = True


class Disciplina(BaseModel):
    id_disciplina: int
    id_curso: int
    id_tipo_disciplina: int
    tx_sigla: str
    tx_descricao: str
    in_periodo: int
    in_carga_horaria: int

    class Config:
        orm_mode = True


class Instituicao(BaseModel):
    id_instituicao: int
    tx_sigla: str
    tx_descricao: str

    class Config:
        orm_mode = True


class Leciona(BaseModel):
    id_professor: int
    id_disciplina: int

    class Config:
        orm_mode = True


class Professor(BaseModel):
    id_professor: int
    id_titulo: int
    tx_nome: str
    tx_sexo: str
    tx_estado_civil: str
    dt_nascimento: str
    tx_telefone: str

    class Config:
        orm_mode = True


class TipoCurso(BaseModel):
    id_tipo_curso: int
    tx_descricao: str

    class Config:
        orm_mode = True


class TipoDisciplina(BaseModel):
    id_tipo_disciplina: int
    tx_descricao: str

    class Config:
        orm_mode = True


class Titulo(BaseModel):
    id_titulo: int
    tx_descricao: str

    class Config:
        orm_mode = True
"""
