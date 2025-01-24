from sqlmodel import SQLModel, Field

# Modelo de la base de datos (SQLModel)
class Cliente(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    nombre: str
    dni: str = Field(unique=True, index=True)
    email: str = Field(unique=True, index=True)
    capital_solicitado: float

class SimulacionHipoteca(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    cliente_id: int = Field(foreign_key="cliente.id")
    tae: float
    plazo_amortizacion: int
    cuota_mensual: float
    importe_total: float