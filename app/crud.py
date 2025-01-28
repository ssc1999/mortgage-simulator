from sqlalchemy.orm import Session
from app.models import Cliente, Simulacion

def get_cliente_by_dni(db: Session, dni: str):
    return db.query(Cliente).filter(Cliente.dni == dni).first()

def create_cliente(db: Session, cliente: Cliente):
    db.add(cliente)
    db.commit()
    db.refresh(cliente)
    return cliente

def create_simulacion(db: Session, simulacion: Simulacion):
    db.add(simulacion)
    db.commit()
    db.refresh(simulacion)
    return simulacion