from sqlmodel import Field, SQLModel, Relationship
from typing import Optional
from sqlalchemy import Column, Integer

class Materia(SQLModel, table=True):
    id: Optional[int] = Field(
        default=None,
        primary_key=True,
        nullable=False,
        sa_column=Column(Integer, autoincrement=True)
    )
    recursos = Relationship(back_populates="materias")
    nombre: str = Field(index=True, nullable=False)
