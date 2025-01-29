from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_session
from schemas.schemas import ClienteCreate, ClienteResponse
from models.models import Cliente
from crud.crud import create_cliente, get_cliente_by_dni, update_cliente, delete_cliente, validar_dni

router = APIRouter()

# Endpoint para crear un nuevo cliente
@router.post("/", response_model=ClienteResponse)
async def create_new_cliente(cliente: ClienteCreate, db: Session = Depends(get_session)):
    if not validar_dni(cliente.dni):
        raise HTTPException(status_code=400, detail="DNI no válido")
    db_cliente = get_cliente_by_dni(db, cliente.dni)
    if db_cliente:
        raise HTTPException(status_code=400, detail="Cliente ya existe")
    return create_cliente(db, cliente)

# Endpoint para obtener un cliente por su DNI
@router.get("/dni/{dni}", response_model=ClienteResponse)
async def read_cliente_by_dni(dni: str, db: Session = Depends(get_session)):
    cliente = get_cliente_by_dni(db, dni)
    if cliente is None:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return cliente

# Endpoint para actualizar un cliente existente
@router.put("/dni/{dni}", response_model=ClienteResponse)
async def update_existing_cliente(dni: str, cliente: ClienteCreate, db: Session = Depends(get_session)):
    db_cliente = get_cliente_by_dni(db, dni)
    if db_cliente is None:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return update_cliente(db, db_cliente, cliente)

# Endpoint para eliminar un cliente existente
@router.delete("/dni/{dni}")
async def delete_existing_cliente(dni: str, db: Session = Depends(get_session)):
    db_cliente = get_cliente_by_dni(db, dni)
    if db_cliente is None:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    delete_cliente(db, db_cliente)
    return {"message": "Cliente eliminado"}