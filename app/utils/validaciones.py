from fastapi import HTTPException

def validar_transicion(actual, nuevo):
    flujos = {
        "solicitado": ["recibido"],
        "recibido": ["asignado"],
        "asignado": ["en_proceso"],
        "en_proceso": ["en_revision"],
        "en_revision": ["terminado"]
    }

    if nuevo not in flujos.get(actual, []):
        raise HTTPException(
            status_code=422,
            detail="Transición de estado no permitida"
        )