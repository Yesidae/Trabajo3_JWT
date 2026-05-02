from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id_usuario = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    correo = Column(String, unique=True, index=True)
    password_hash = Column(String)
    rol = Column(String)
    activo = Column(Boolean, default=True)