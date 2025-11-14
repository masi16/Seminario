from typing import Optional
from sqlmodel import SQLModel
from models.estudiante import Motivacion

class EstudianteBase(SQLModel): 
    nombre_completo: str 
    motivacion: Motivacion = Motivacion.MEDIA

class EstudianteCreate(EstudianteBase):
    pass 

class EstudianteRead(EstudianteBase):
    id: int 

    class Config:
        orm_mode = True

class EstudianteUpdate(SQLModel):
    nombre_completo: Optional[str] = None
    motivacion: Optional[Motivacion] = None

    


