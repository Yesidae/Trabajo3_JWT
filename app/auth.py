from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
import os

SECRET_KEY = "supersecretkey"  # luego lo pasas a .env
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# 🔐 Hash
def hash_password(password: str):
    return pwd_context.hash(password)

# 🔐 Verificar password
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# 🎟 Crear token
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def get_scopes_by_role(rol: str):
    scopes = {
        "solicitante": ["tickets:crear", "tickets:ver_propios"],
        "responsable_tecnico": [
            "tickets:recibir",
            "tickets:asignar",
            "tickets:finalizar",
            "tickets:ver_propios"
        ],
        "auxiliar": ["tickets:atender", "tickets:ver_propios"],
        "tecnico_especializado": ["tickets:atender", "tickets:ver_propios"],
        "admin": [
            "tickets:crear",
            "tickets:ver_propios",
            "tickets:recibir",
            "tickets:asignar",
            "tickets:atender",
            "tickets:finalizar",
            "tickets:ver_todos",
            "usuarios:gestionar"
        ]
    }
    return scopes.get(rol, [])