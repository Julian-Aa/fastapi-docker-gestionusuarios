"""
Main module for FastAPI application setup.

This module sets up the FastAPI application, manages the database connection
lifecycle, and includes routes for user management.
"""

from contextlib import asynccontextmanager
from fastapi import FastAPI
from starlette.responses import RedirectResponse
from database import database as connection, connect_db, close_db, create_tables
from models.categoriaAlimento import CategoriaAlimento
from models.categoriaReceta import CategoriaReceta
from models.despensa import Despensa
from models.grupo import Grupo
from models.itemLista import ItemLista
from models.listaCompra import ListaCompra
from models.menu import Menu
from models.menuReceta import MenuReceta
from models.notificacion import Notificacion
from models.receta import Receta
from models.usuario import Usuario
from models.usuarioGrupo import UsuarioGrupo
from routes.usuario_route import router as usuario_router

@asynccontextmanager
async def manage_lifespan(_app: FastAPI):
    """
    Manage the lifespan of the FastAPI application.

    Ensures the database connection is opened and closed properly,
    and creates tables if they do not exist.
    """
    connect_db()  # Conectar la base de datos
    try:
        create_tables([Usuario, CategoriaAlimento, CategoriaReceta, Despensa, Grupo,
                       ItemLista, ListaCompra, Menu, MenuReceta, Notificacion, Receta, UsuarioGrupo])  # Crear las tablas
        yield
    except Exception as e:
        print(f"❌ Error al gestionar el ciclo de vida de la aplicación: {e}")
    finally:
        close_db()  # Cerrar la conexión a la base de datos

app = FastAPI(
    title="Gestión de Usuarios",
    version="1.0",
    contact={
        "name": "Julian Andres Arango",
        "url": "https://github.com/Julian-Aa",
        "email": "julian.arango.re@gmail.com",
    },
    lifespan=manage_lifespan
)

@app.get("/")
async def read_root():
    """
    Redirect the root path to the API documentation.

    Returns a redirection response to the documentation page.
    """
    return RedirectResponse(url="/docs")

# Incluir las rutas de gestión de usuarios
app.include_router(usuario_router, prefix="/usuarios", tags=["Usuarios"])
