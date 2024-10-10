"""
This module defines the CategoriaReceta model for the database.

The CategoriaReceta model represents the categories of recipes in the system.
"""

from peewee import Model, CharField, AutoField
from database import database  # Ajustar la ruta según la estructura de tu proyecto

class CategoriaReceta(Model):  # pylint: disable=too-few-public-methods
    """
    CategoriaReceta model that represents the categories of recipes.

    Attributes:
        id_categoria_receta (int): Primary key for the recipe category.
        nombre (str): Name of the recipe category (must be unique).
    """
    id_categoria_receta = AutoField()
    nombre = CharField(max_length=100, unique=True)

    class Meta:
        database = database
        table_name = 'categorias_recetas'
