from typing import Optional
from sqlmodel import SQLModel
from models.recursos import Tipo, Dificultad
from models.estudiante import Motivacion
from datetime import datetime, timezone
from sqlalchemy import Numeric

class HistorialCalificacionBase(SQLModel):
    nota: Numeric
    completado_a: Optional[datetime] = None

class HistorialCalificacionCreate(HistorialCalificacionBase):
    estudiante_id: int
    recursos_id: int

class EstudianteRead(SQLModel):
    id: int
    nombre_completo: str
    motivacion: Motivacion

    class Config:
        orm_mode = True

class RecursoRead(SQLModel):
    id: int
    titulo: str
    tipo: Tipo
    dificultad: Dificultad
    url: Optional[str] = None
    materias_id: int

    class Config:
        orm_mode = True

class HistorialCalificacionRead(HistorialCalificacionBase):
    estudiante: EstudianteRead
    recurso: RecursoRead
    class Config:
        orm_mode = True

class HistorialCalificacionUpdate(HistorialCalificacionBase):
    nota: Optional[Numeric] = None
    completado_a: Optional[datetime] = None
    estudiante_id: Optional[int] = None
    recursos_id: Optional[int] = None
    