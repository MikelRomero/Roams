from sqlmodel import Session, select
from app.models.models import Cliente, SimulacionHipoteca
from app.schemas.schemas import ClienteCreate, SimulacionHipotecaCreate
from typing import Optional

# Validar el DNI
def validar_dni(dni: str) -> bool:
    letras_validas = "TRWAGMYFPDXBNJZSQVHLCKE"
    if len(dni) != 9:
        return False
    digitos = dni[:8]
    letra = dni[-1].upper()
    if not digitos.isdigit():
        return False
    resto = int(digitos) % 23
    letra_calculada = letras_validas[resto]
    return letra == letra_calculada

# Crear un nuevo cliente
def create_cliente(db: Session, cliente: ClienteCreate):
    if not validar_dni(cliente.dni):
        raise ValueError("DNI no válido")
    db_cliente = Cliente(**cliente.model_dump())
    db.add(db_cliente)
    db.commit()
    db.refresh(db_cliente)
    return db_cliente

# Obtener un cliente por su DNI
def get_cliente_by_dni(db: Session, dni: str):
    return db.exec(select(Cliente).where(Cliente.dni == dni)).first()

# Obtener un cliente por su ID
def get_cliente(db: Session, cliente_id: int):
    return db.get(Cliente, cliente_id)

# Actualizar un cliente existente
def update_cliente(db: Session, db_cliente: Cliente, cliente: ClienteCreate):
    db_cliente.nombre = cliente.nombre
    db_cliente.email = cliente.email
    db_cliente.capital_solicitado = cliente.capital_solicitado
    db.commit()
    db.refresh(db_cliente)
    return db_cliente

# Eliminar un cliente existente
def delete_cliente(db: Session, db_cliente: Cliente):
    db.delete(db_cliente)
    db.commit()

# Simular una hipoteca
def simular_hipoteca(db: Session, simulacion: SimulacionHipotecaCreate):
    cliente = db.get(Cliente, simulacion.cliente_id)
    if not cliente:
        raise ValueError("Cliente no encontrado")
    tae_mensual = simulacion.tae / 100 / 12
    plazo_meses = simulacion.plazo_amortizacion
    capital = cliente.capital_solicitado
    cuota_mensual = (capital * tae_mensual) / (1 - (1 + tae_mensual) ** -plazo_meses)
    importe_total = cuota_mensual * plazo_meses
    db_simulacion = SimulacionHipoteca(
        cliente_id=simulacion.cliente_id,
        tae=simulacion.tae,
        plazo_amortizacion=simulacion.plazo_amortizacion,
        cuota_mensual=cuota_mensual,
        importe_total=importe_total
    )
    db.add(db_simulacion)
    db.commit()
    db.refresh(db_simulacion)
    return db_simulacion