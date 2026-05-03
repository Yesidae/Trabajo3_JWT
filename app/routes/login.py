from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.usuario import Usuario
from app.auth import verify_password, create_access_token, get_scopes_by_role

router = APIRouter(prefix="/auth", tags=["Auth"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/token")
def login(correo: str, password: str, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.correo == correo).first()

    if not usuario:
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")

    if not verify_password(password, usuario.password_hash):
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")

    # 🔥 AQUÍ ESTÁ LA CLAVE DEL TALLER
    token_data = {
        "sub": usuario.correo,
        "id_usuario": usuario.id_usuario,
        "rol": usuario.rol,
        "scopes": get_scopes_by_role(usuario.rol)
    }

    access_token = create_access_token(token_data)

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }