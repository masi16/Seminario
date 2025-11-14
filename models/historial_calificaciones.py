from sqlmodel import Field, SQLModel, Relationship
from typing import Optional
from sqlalchemy import Column, Integer, Numeric
from datetime import datetime, timezone

class HistorialCalificacion(SQLModel, table=True):
    estudiante_id: Relationship[Optional[int]] = Field(
        default=None,
        primary_key=True,
        nullable=False,
        back_populates="estudiantes",
        sa_column=Column(Integer, autoincrement=False)
    )
    recursos_id: Relationship[Optional[int]] = Field(
        default=None,
        primary_key=True,
        nullable=False,
        back_populates="recursos",
        sa_column=Column(Integer, autoincrement=False)
    )
    nota: Numeric = Field(scale=2, precision=5, nullable=False, sa_column=Column(Numeric(5, 2)))
    completado_a: datetime = Field(default_factory=lambda: datetime.now(timezone.utc), nullable=True)