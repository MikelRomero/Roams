from pydantic import BaseModel

# Modelos base para evitar redundancia
class ClienteBase(BaseModel):
    nombre: str
    dni: str
    email: str
    capital_solicitado: float

class SimulacionHipotecaBase(BaseModel):
    cliente_id: int
    tae: float
    plazo_amortizacion: int

# Modelos para la creación de datos (inputs)
class ClienteCreate(ClienteBase):
    pass  # Hereda todos los campos de ClienteBase

class SimulacionHipotecaCreate(SimulacionHipotecaBase):
    pass  # Hereda todos los campos de SimulacionHipotecaBase

# Modelos para la respuesta de la API (outputs)
class ClienteResponse(ClienteBase):
    id: int  # Añade el campo ID

    class ConfigDict:
        orm_mode = True  # Permite la conversión automática a/desde ORM

class SimulacionHipotecaResponse(SimulacionHipotecaBase):
    id: int  # Añade el campo ID
    cuota_mensual: float  # Campos adicionales para la respuesta
    importe_total: float

    class ConfigDict:
        orm_mode = True  # Permite la conversión automática a/desde ORM