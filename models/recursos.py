from enum import Enum as PyEnum
from sqlmodel import Field, SQLModel, Relationship
from typing import Optional
from sqlalchemy import Column, Integer, Enum
from models.materias import Materia

class Tipo(str, PyEnum): 
    VIDEO = "video"
    CURSO = "curso"
    LECTURA = "lectura"
    EJERCICIO = "ejercicio"

class Dificultad(str, PyEnum):
    FACIL = "facil"
    INTERMEDIO = "intermedio"
    AVANZADO = "avanzado"

class Recurso(SQLModel, table=True):
    id: Optional[int] = Field(
        default=None,
        primary_key=True,
        nullable=False,
        sa_column=Column(Integer, autoincrement=True)
    )
    materias_id: Optional[int] = Field(
        default=None,
        foreign_key="materia.id",
        index=True,
        nullable=False
    )
    materias: Optional["Materia"] = Relationship(back_populates="recursos")
    titulo: str = Field(index=True, nullable=False)
    tipo: Tipo = Field(index=True, nullable=False, sa_column=Column(Enum(Tipo, native_enum=True, name="tipo_enum")))
    dificultad: Dificultad = Field(index=True, nullable=False, sa_column=Column(Enum(Dificultad, native_enum=True, name="dificultad_enum")) )
    url: str = Field(default=None, nullable=False)