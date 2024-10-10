"""
This module defines the CategoriaAlimento model for the database.

The CategoriaAlimento model represents categories of food items in the system.
"""

from peewee import Model, CharField, AutoField
from database import database  # Ajustar según la estructura de tu proyecto

class CategoriaAlimento(Model):  # pylint: disable=too-few-public-methods
    """
    CategoriaAlimento model that represents food categories.

    Attributes:
        id_categoria_alimento (int): Primary key for the food category.
        nombre (str): Name of the food category (must be unique).
    """
    id_categoria_alimento = AutoField()
    nombre = CharField(max_length=100, unique=True)

    class Meta:
        database = database
        table_name = 'categorias_alimentos'
