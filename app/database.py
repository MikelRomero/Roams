from sqlmodel import SQLModel, create_engine, AsyncSession

# Configuración de la base de datos
DATABASE_URL = "sqlite:///database.db"
engine = create_engine(DATABASE_URL)

# Crear las tablas en la base de datos
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

# Obtener una sesión de la base de datos

async def get_session() -> AsyncSession:
    async with AsyncSession(engine) as session:
        yield session