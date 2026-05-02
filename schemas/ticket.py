from pydantic import BaseModel
from typing import Optional

class TicketBase(BaseModel):
    id_solicitante: int
    id_laboratorio: int
    id_servicio: int
    titulo: str
    descripcion: str
    prioridad: str

class TicketCreate(TicketBase):
    pass

class TicketResponse(TicketBase):
    id_ticket: int
    estado: str

    class Config:
        from_attributes = True


class TicketEstadoUpdate(BaseModel):
    estado: str