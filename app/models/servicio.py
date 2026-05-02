from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base

class Servicio(Base):
    __tablename__ = "servicios"

    id_servicio = Column(Integer, primary_key=True)
    nombre = Column(String)
    descripcion = Column(String)
    activo = Column(Boolean, default=True)