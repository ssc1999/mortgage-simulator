from sqlalchemy import Column, String, Float, Integer, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./database.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Cliente(Base):
    __tablename__ = "clientes"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    dni = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    capital = Column(Float, nullable=False)

class Simulacion(Base):
    __tablename__ = "simulaciones"
    id = Column(Integer, primary_key=True, index=True)
    cliente_dni = Column(String, nullable=False)
    tae = Column(Float, nullable=False)
    plazo = Column(Integer, nullable=False)
    cuota_mensual = Column(Float, nullable=False)
    importe_total = Column(Float, nullable=False)