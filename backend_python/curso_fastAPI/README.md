# FastAPI Movies Backend

Este proyecto es una API backend desarrollada con FastAPI en Python. Permite gestionar información de películas y utiliza una base de datos SQLite para almacenar los datos. Incluye autenticación JWT para proteger los endpoints y una estructura modular para facilitar el mantenimiento.

## Características
- CRUD de películas
- Autenticación con JWT
- Base de datos SQLite
- Estructura modular (configuración, modelos, etc.)

## Requisitos
- Python 3.10+
- FastAPI
- Uvicorn
- SQLAlchemy

## Instalación
1. Clona el repositorio:
   ```sh
   git clone https://github.com/oscardbocanegra/learning_platzi.git
   cd learning_platzi/backend_python/curso_fastAPI
   ```
2. Instala las dependencias:
   ```sh
   pip install fastapi uvicorn sqlalchemy
   ```

## Ejecución
1. Inicia el servidor:
   ```sh
   uvicorn main:app --reload
   ```
2. Accede a la documentación interactiva en [http://localhost:8000/docs](http://localhost:8000/docs)

## Estructura del proyecto
- `main.py`: Punto de entrada de la API
- `models/`: Modelos de datos
- `config/`: Configuración de la base de datos
- `jwt_manager.py`: Manejo de autenticación JWT
- `database.sqlite`: Base de datos

## Licencia
Este proyecto es solo para fines educativos.
