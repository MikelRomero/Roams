from sqlmodel import SQLModel, create_engine, Session

# Configuración de la base de datos
DATABASE_URL = "sqlite:///database.db"
engine = create_engine(DATABASE_URL)

# Crear las tablas en la base de datos
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

# Obtener una sesión de la base de datos
def get_session():
    with Session(engine) as session:
        yield session