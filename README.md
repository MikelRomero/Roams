# Simulador de Hipotecas - API RESTful

¡Bienvenido al proyecto de Simulador de Hipotecas! Esta es una API RESTful desarrollada en Python con FastAPI que permite realizar simulaciones de hipotecas para diferentes clientes. La API utiliza SQLite como base de datos y ofrece operaciones CRUD para gestionar clientes y simulaciones de hipotecas.

## Características principales

- **Gestión de clientes**:
  - Crear un nuevo cliente con datos personales y financieros (nombre, DNI, email, capital solicitado).
  - Consultar los datos de un cliente existente por su DNI.
  - Modificar o eliminar los datos de un cliente existente.

- **Simulación de hipotecas**:
  - Solicitar una simulación de hipoteca para un cliente dado, con un TAE y un plazo de amortización como inputs.
  - La API devuelve la cuota mensual a pagar y el importe total a devolver.
  - Las simulaciones se guardan en la base de datos para su posterior consulta.

- **Validación de datos**:
  - Validación del DNI utilizando el algoritmo oficial.
  - Manejo de errores y excepciones para entradas inválidas o datos duplicados.

- **Documentación automática**:
  - La API está documentada automáticamente usando Swagger UI y ReDoc. Puedes acceder a la documentación interactiva en `/docs` o `/redoc`.

## Requisitos previos

Antes de ejecutar el proyecto, asegúrate de tener instalado lo siguiente:

- **Python 3.8 o superior**.
- **pip** (gestor de paquetes de Python).

## Instalación

Sigue estos pasos para instalar y ejecutar el proyecto:

1. **Clona el repositorio**:
   ```bash
   git clone https://github.com/tu-usuario/simulador-hipotecas.git
   cd simulador-hipotecas
