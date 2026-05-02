from fastapi import FastAPI
from app.routes import usuario, laboratorio, servicio, ticket
from app.routes import auth

app = FastAPI()

app.include_router(usuario.router)
app.include_router(laboratorio.router)
app.include_router(servicio.router)
app.include_router(ticket.router)
app.include_router(auth.router)