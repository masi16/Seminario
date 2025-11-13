from enum import Enum as PyEnum
from typing import Optional
from sqlmodel import Field, SQLModel
from sqlalchemy import Column, Enum as SQLEnum, Integer

class Motivacion(PyEnum, str):
    ALTA = "alta"
    MEDIA  = "media"
    BAJA = "baja"

class Estudiante(SQLModel, table=True):
    id: Optional[int] = Field(
        default=None,
        primary_key=True,
        nullable=False,
        sa_column=Column(Integer, autoincrement=True)
    )
    nombre_completo: str = Field(index=True, nullable=False)
    motivacion: Motivacion = Field(
        default=Motivacion.MEDIA,
        sa_column=Column(SQLEnum(Motivacion, native_enum=True, name="motivacion_enum"), nullable=False)
    )

