"""
Routes module for managing CRUD operations for the Usuario entity.

This module provides routes for creating, retrieving, updating, and deleting
usuarios in the system using the UsuarioService.
"""

from fastapi import APIRouter, HTTPException
from services.usuario_service import UsuarioService  # Ajustar la importación según la estructura

router = APIRouter()
usuario_service = UsuarioService()

@router.post("/usuarios")
def crear_usuario(data: dict):
    """
    Creates a new usuario in the system.

    Args:
        data (dict): The data to create a new usuario.

    Returns:
        dict: The created usuario.
    """
    return usuario_service.crear_usuario(data)

@router.get("/usuarios/{id_usuario}")
def obtener_usuario(id_usuario: int):
    """
    Retrieves a usuario by its ID.

    Args:
        id_usuario (int): The ID of the usuario to retrieve.

    Raises:
        HTTPException: If the usuario is not found.

    Returns:
        dict: The usuario if found.
    """
    usuario = usuario_service.obtener_usuario(id_usuario)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

@router.get("/usuarios")
def obtener_todos_los_usuarios():
    """
    Retrieves all usuarios in the system.

    Returns:
        List[dict]: A list of all usuarios.
    """
    return usuario_service.obtener_todos_los_usuarios()

@router.put("/usuarios/{id_usuario}")
def actualizar_usuario(id_usuario: int, data: dict):
    """
    Updates a usuario by its ID.

    Args:
        id_usuario (int): The ID of the usuario to update.
        data (dict): The updated usuario data.

    Raises:
        HTTPException: If the usuario is not found.

    Returns:
        dict: The updated usuario if found.
    """
    usuario = usuario_service.actualizar_usuario(id_usuario, data)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

@router.delete("/usuarios/{id_usuario}")
def eliminar_usuario(id_usuario: int):
    """
    Deletes a usuario by its ID.

    Args:
        id_usuario (int): The ID of the usuario to delete.

    Raises:
        HTTPException: If the usuario is not found.

    Returns:
        dict: A confirmation message if the usuario is deleted.
    """
    if not usuario_service.eliminar_usuario(id_usuario):
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return {"detail": "Usuario eliminado exitosamente"}
