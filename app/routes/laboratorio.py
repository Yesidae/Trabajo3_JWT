from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.laboratorio import Laboratorio
from app.schemas.laboratorio import LaboratorioCreate, LaboratorioResponse

router = APIRouter(prefix="/laboratorios", tags=["Laboratorios"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=LaboratorioResponse)
def crear_laboratorio(lab: LaboratorioCreate, db: Session = Depends(get_db)):
    nuevo = Laboratorio(**lab.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo


@router.get("/", response_model=list[LaboratorioResponse])
def listar_laboratorios(db: Session = Depends(get_db)):
    return db.query(Laboratorio).all()


@router.get("/{id_laboratorio}", response_model=LaboratorioResponse)
def obtener_laboratorio(id_laboratorio: int, db: Session = Depends(get_db)):
    lab = db.query(Laboratorio).filter(Laboratorio.id_laboratorio == id_laboratorio).first()
    if not lab:
        raise HTTPException(status_code=404, detail="Laboratorio no encontrado")
    return lab