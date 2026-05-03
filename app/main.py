from fastapi import FastAPI

from app.routes.usuarios import router as usuario_router
from app.routes.laboratorio import router as laboratorio_router
from app.routes.servicio import router as servicio_router
from app.routes.ticket import router as ticket_router

app = FastAPI()

app.include_router(usuario_router)
app.include_router(laboratorio_router)
app.include_router(servicio_router)
app.include_router(ticket_router)
