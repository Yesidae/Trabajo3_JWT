from fastapi import APIRouter, Depends, HTTPException, Security
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.ticket import Ticket
from app.schemas.ticket import TicketCreate, TicketResponse, TicketEstadoUpdate
from app.dependencies import get_current_user

router = APIRouter(prefix="/tickets", tags=["Tickets"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def crear_ticket(
    ticket: TicketCreate,
    db: Session = Depends(get_db),
    user=Security(get_current_user, scopes=["tickets:crear"])
):
    nuevo = Ticket(**ticket.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo


@router.get("/")
def listar_tickets(
    db: Session = Depends(get_db),
    user=Security(get_current_user, scopes=["tickets:ver_propios"])
):
    return db.query(Ticket).all()


@router.get("/{id_ticket}", response_model=TicketResponse)
def obtener_ticket(id_ticket: int, db: Session = Depends(get_db)):
    ticket = db.query(Ticket).filter(Ticket.id_ticket == id_ticket).first()
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket no encontrado")
    return ticket


@router.patch("/{id_ticket}/estado")
def cambiar_estado(
    id_ticket: int,
    data: TicketEstadoUpdate,
    db: Session = Depends(get_db),
    user=Security(get_current_user, scopes=["tickets:atender"])
):
    ticket = db.query(Ticket).filter(Ticket.id_ticket == id_ticket).first()

    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket no encontrado")

    ticket.estado = data.estado
    db.commit()
    db.refresh(ticket)

    return ticket