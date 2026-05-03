from fastapi import Depends, HTTPException, Security
from fastapi.security import HTTPBearer, SecurityScopes
from jose import JWTError, jwt
from app.auth import SECRET_KEY, ALGORITHM


security = HTTPBearer()


def get_current_user(
    security_scopes: SecurityScopes,
    credentials=Depends(security)
):
    token = credentials.credentials

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        token_scopes = payload.get("scopes", [])

        for scope in security_scopes.scopes:
            if scope not in token_scopes:
                raise HTTPException(
                    status_code=403,
                    detail="No tienes permisos suficientes"
                )

        return payload

    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido")