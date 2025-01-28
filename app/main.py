from fastapi import FastAPI
from app.routes import clients, mortgage
from app.models import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Roams Mortgage Simulator")

app.include_router(clients.router, prefix="/clients", tags=["Clients"])
app.include_router(mortgage.router, prefix="/mortgage", tags=["Mortgage"])