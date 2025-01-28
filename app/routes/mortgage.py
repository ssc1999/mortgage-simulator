from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import SimulacionRequest, SimulacionResponse
from app.models import Simulacion
from app.crud import create_simulacion, get_cliente_by_dni
from app.models import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=SimulacionResponse)
def simulate_mortgage(simulacion: SimulacionRequest, db: Session = Depends(get_db)):
    cliente = get_cliente_by_dni(db, simulacion.dni)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    
    i = (simulacion.tae / 100) / 12
    n = simulacion.plazo * 12
    cuota_mensual = cliente.capital * i / (1 - (1 + i) ** -n)
    importe_total = cuota_mensual * n

    nueva_simulacion = Simulacion(
        cliente_dni=simulacion.dni,
        tae=simulacion.tae,
        plazo=simulacion.plazo,
        cuota_mensual=cuota_mensual,
        importe_total=importe_total
    )
    create_simulacion(db, nueva_simulacion)
    return nueva_simulacion