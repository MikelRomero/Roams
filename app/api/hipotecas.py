from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from database import get_session
from models.models import SimulacionHipoteca
from schemas.schemas import SimulacionHipotecaCreate, SimulacionHipotecaResponse
from crud.crud import simular_hipoteca

router = APIRouter()

# Endpoint para simular una hipoteca
@router.post("/", response_model=SimulacionHipotecaResponse)
async def simular_hipoteca_endpoint(simulacion: SimulacionHipotecaCreate, db: Session = Depends(get_session)):
    return simular_hipoteca(db, simulacion)