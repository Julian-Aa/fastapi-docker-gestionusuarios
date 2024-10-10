"""
Service module for managing CRUD operations for the Usuario entity.

This module provides the business logic for creating, retrieving, updating,
and deleting usuarios.
"""

from models.usuario import Usuario  # Asegúrate de que la ruta es correcta
from peewee import DoesNotExist

class UsuarioService:
    """
    Service class to manage usuarios in the system.

    Provides methods to create, retrieve, update, and delete usuarios.
    """
    
    def crear_usuario(self, data):
        """
        Creates a new usuario and adds it to the database.

        Args:
            data (dict): The data to create the usuario.

        Returns:
            Usuario: The created usuario.
        """
        usuario = Usuario.create(**data)
        return usuario

    def obtener_usuario(self, id_usuario):
        """
        Retrieves a usuario by its ID.

        Args:
            id_usuario (int): The ID of the usuario to retrieve.

        Returns:
            Usuario: The usuario if found, otherwise None.
        """
        try:
            return Usuario.get(Usuario.id_usuario == id_usuario)
        except DoesNotExist:
            return None

    def obtener_todos_los_usuarios(self):
        """
        Retrieves all usuarios.

        Returns:
            List[Usuario]: A list of all usuarios.
        """
        return list(Usuario.select())

    def actualizar_usuario(self, id_usuario, data):
        """
        Updates an existing usuario with new data.

        Args:
            id_usuario (int): The ID of the usuario to update.
            data (dict): The updated data for the usuario.

        Returns:
            Usuario: The updated usuario if found, otherwise None.
        """
        usuario = self.obtener_usuario(id_usuario)
        if usuario:
            query = Usuario.update(**data).where(Usuario.id_usuario == id_usuario)
            query.execute()
            return usuario
        return None

    def eliminar_usuario(self, id_usuario):
        """
        Deletes a usuario by its ID.

        Args:
            id_usuario (int): The ID of the usuario to delete.

        Returns:
            bool: True if the usuario was deleted, otherwise False.
        """
        usuario = self.obtener_usuario(id_usuario)
        if usuario:
            usuario.delete_instance()
            return True
        return False
