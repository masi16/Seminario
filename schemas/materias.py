from typing import Optional, List
from sqlmodel import SQLModel
from models.recursos import Tipo, Dificultad

class MateriaBase(SQLModel):
    nombre: str 

class MateriaCreate(MateriaBase):
    pass

# esquema de lectura para Recurso, usado dentro de MateriaRead
class RecursoRead(SQLModel):
    id: int
    titulo: str
    tipo: Tipo
    dificultad: Dificultad
    url: Optional[str] = None
    materias_id: int

    class Config:
        orm_mode = True

class MateriaRead(MateriaBase):
    id: int
    recursos: List[RecursoRead] = []

    class Config:
        orm_mode = True

class MateriaUpdate(SQLModel):
    nombre: Optional[str] = None