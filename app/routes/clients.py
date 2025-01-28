from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models import Cliente
from app.schemas import ClienteCreate, ClienteResponse
from app.crud import create_cliente, get_cliente_by_dni
from app.models import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=ClienteResponse)
def create_client(cliente: ClienteCreate, db: Session = Depends(get_db)):
    if get_cliente_by_dni(db, cliente.dni):
        raise HTTPException(status_code=400, detail="DNI ya registrado")
    nuevo_cliente = Cliente(**cliente.dict())
    return create_cliente(db, nuevo_cliente)

@router.get("/{dni}", response_model=ClienteResponse)
def get_client(dni: str, db: Session = Depends(get_db)):
    cliente = get_cliente_by_dni(db, dni)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return cliente