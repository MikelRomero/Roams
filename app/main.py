from fastapi import FastAPI
from app.api import clientes, hipotecas
from app.database import create_db_and_tables

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

# Montar las rutas
app.include_router(clientes.router, prefix="/clientes", tags=["clientes"])
app.include_router(hipotecas.router, prefix="/hipotecas", tags=["hipotecas"])