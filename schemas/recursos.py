from typing import Optional, List
from sqlmodel import SQLModel
from models.recursos import Tipo, Dificultad

class RecursoBase(SQLModel):
    titulo: str
    tipo: Tipo
    dificultad: Dificultad
    url: Optional[str] = None
    materias_id: int

class RecursoCreate(RecursoBase):
    pass

class MateriaRead(SQLModel):
    id: int
    nombre: str

    class Config:
        orm_mode = True

class RecursoRead(RecursoBase):
    id: int
    materias_id: List[MateriaRead] = None

    class Config:
        orm_mode = True

class RecursoUpdate(SQLModel):
    titulo: Optional[str] = None
    tipo: Optional[Tipo] = None
    dificultad: Optional[Dificultad] = None
    url: Optional[str] = None
    materias_id: Optional[int] = None