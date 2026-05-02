from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base

class Laboratorio(Base):
    __tablename__ = "laboratorios"

    id_laboratorio = Column(Integer, primary_key=True)
    nombre = Column(String)
    ubicacion = Column(String)
    activo = Column(Boolean, default=True)