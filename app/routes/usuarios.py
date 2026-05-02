from app.auth.security import hash_password
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.usuario import Usuario
from app.schemas.usuario import UsuarioCreate, UsuarioResponse
from app.auth import hash_password
from app.dependencies import get_current_user

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])


# 🔌 Conexión DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ✅ Crear usuario (NO requiere JWT)
@router.post("/", response_model=UsuarioResponse)
def crear_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    datos = usuario.dict()

    # 🔐 Hash de contraseña
    datos["password"] = hash_password(datos["password"])

    nuevo = Usuario(**datos)

    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)

    return nuevo


# 🔒 Listar usuarios (PROTEGIDO)
@router.get("/", response_model=list[UsuarioResponse])
def listar_usuarios(
    db: Session = Depends(get_db),
    user=Depends(get_current_user)  # 👈 JWT requerido
):
    return db.query(Usuario).all()


# 🔒 Obtener usuario por ID (PROTEGIDO)
@router.get("/{id_usuario}", response_model=UsuarioResponse)
def obtener_usuario(
    id_usuario: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)  # 👈 JWT requerido
):
    usuario = db.query(Usuario).filter(Usuario.id_usuario == id_usuario).first()

    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    return usuario


# 🔒 Endpoint de prueba protegido
@router.get("/protegido/test")
def ruta_protegida(user=Depends(get_current_user)):
    return {
        "mensaje": "Acceso permitido",
        "usuario_token": user
    }