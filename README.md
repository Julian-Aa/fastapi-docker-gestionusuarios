# FastAPI User Management with Docker

## Descripción

Proyecto API de gestión de usuarios construido con FastAPI y MySQL, ejecutado en contenedores Docker. Incluye migraciones de base de datos con Peewee, configuración con , y análisis de calidad de código con Pylint. Fácil despliegue y gestión con Docker.

## Estructura del proyecto

- app/
  - helpers/: Funciones de ayuda y utilidades.
  - migrations/: Migraciones de la base de datos utilizando .
  - models/: Definición de los modelos de la base de datos.
  - routes/: Rutas de la API para la gestión de usuarios.
  - services/: Lógica de negocio.
  - main.py: Archivo principal para ejecutar la API.
  - database.py: Configuración de la conexión a la base de datos MySQL.
  
- Dockerfile: Archivo para construir la imagen Docker de la aplicación.
- docker-compose.yml: Archivo para la orquestación de servicios Docker, incluyendo la aplicación FastAPI y la base de datos MySQL.
- .env: Variables de entorno utilizadas por Docker y la base de datos.
- .pylintrc: Archivo de configuración para el análisis de código con Pylint.
- requirements.txt: Dependencias del proyecto.
- MySQL/: Carpeta que contiene datos relacionados con la base de datos MySQL.

## Instalación y Ejecución

### Requisitos

- Docker y Docker Compose instalados.
- Python 3.12 instalado.

### Configuración

1. Clona el repositorio:
   git clone <URL-del-repositorio>
   cd <nombre-del-repositorio>

2. Crea un archivo .env en la raíz del proyecto y define las siguientes variables:
    DB_HOST=mysql
    DB_USER=root
    DB_PASSWORD=rootpassword
    DB_NAME=gestionusuarios

Instrucciones de Ejecución

1. Construye los contenedores de Docker:
    docker-compose up --build

2. Aplica las migraciones a la base de datos:
    docker-compose exec fastapi python -m app.migrations

3. Accede a la aplicación en tu navegador:
    http://localhost:8000

Ejecutar migraciones de la base de datos
El proyecto utiliza peewee_migrate para gestionar las migraciones. Puedes aplicar las migraciones ejecutando el siguiente comando dentro del contenedor FastAPI:
    docker-compose exec fastapi python -m app.migrations

Análisis de calidad de código
    pylint app/

