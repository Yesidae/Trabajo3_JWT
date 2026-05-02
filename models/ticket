from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from app.database import Base
from datetime import datetime

class Ticket(Base):
    __tablename__ = "tickets"

    id_ticket = Column(Integer, primary_key=True)

    id_solicitante = Column(Integer, ForeignKey("usuarios.id_usuario"))
    id_laboratorio = Column(Integer, ForeignKey("laboratorios.id_laboratorio"))
    id_servicio = Column(Integer, ForeignKey("servicios.id_servicio"))

    id_responsable = Column(Integer, ForeignKey("usuarios.id_usuario"), nullable=True)
    id_asignado = Column(Integer, ForeignKey("usuarios.id_usuario"), nullable=True)

    titulo = Column(String)
    descripcion = Column(String)
    estado = Column(String, default="solicitado")
    prioridad = Column(String)

    observacion_responsable = Column(String, nullable=True)
    observacion_tecnico = Column(String, nullable=True)

    fecha_creacion = Column(DateTime, default=datetime.utcnow)
    fecha_actualizacion = Column(DateTime, default=datetime.utcnow)
    fecha_finalizacion = Column(DateTime, nullable=True)