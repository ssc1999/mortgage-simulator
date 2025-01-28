from pydantic import BaseModel, EmailStr

class ClienteBase(BaseModel):
    nombre: str
    dni: str
    email: EmailStr
    capital: float

class ClienteCreate(ClienteBase):
    pass

class ClienteResponse(ClienteBase):
    id: int

    class Config:
        from_attributes = True

class SimulacionRequest(BaseModel):
    dni: str
    tae: float
    plazo: int

class SimulacionResponse(BaseModel):
    cuota_mensual: float
    importe_total: float

    class Config:
        from_attributes = True