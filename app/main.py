from fastapi import FastAPI
from contextlib import asynccontextmanager
from api import clientes, hipotecas
from database import create_db_and_tables

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Code to run on startup
    create_db_and_tables()
    yield
    # Code to run on shutdown (if needed)

app = FastAPI(lifespan=lifespan)

# Montar las rutas
app.include_router(clientes.router, prefix="/clientes", tags=["clientes"])
app.include_router(hipotecas.router, prefix="/hipotecas", tags=["hipotecas"])