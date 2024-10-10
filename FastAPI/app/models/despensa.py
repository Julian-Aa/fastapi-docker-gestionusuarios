"""
This module defines the Despensa model for the database.

The Despensa model represents a user's pantry and the ingredients it contains,
including their quantities, expiration dates, and categories.
"""

from peewee import Model, ForeignKeyField, AutoField, DecimalField, DateField, DateTimeField, TimestampField, SQL
from database import database  # Ajustar la ruta según la estructura de tu proyecto
from .usuario import Usuario
from .ingrediente import Ingrediente
from datetime import datetime
from .categoriaAlimento import CategoriaAlimento

class Despensa(Model):  # pylint: disable=too-few-public-methods
    """
    Despensa model that represents the user's pantry.

    Attributes:
        id_despensa (int): Primary key for the pantry item.
        id_usuario (ForeignKey): Reference to the user who owns the pantry.
        id_ingrediente (ForeignKey): Reference to the ingredient stored in the pantry.
        cantidad (DecimalField): The quantity of the ingredient.
        fecha_caducidad (DateField): The expiration date of the ingredient.
        fecha_agregado (TimestampField): The date when the ingredient was added to the pantry.
        id_categoria_alimento (ForeignKey): Reference to the category of the food.
    """
    id_despensa = AutoField()
    id_usuario = ForeignKeyField(Usuario, backref='despensa', on_delete='CASCADE', null=True)
    id_ingrediente = ForeignKeyField(Ingrediente, backref='despensa', on_delete='CASCADE', null=True)
 #   cantidad = DecimalField(max_digits=10, decimal_places=2, null=True)
    fecha_caducidad = DateField(null=True)
    fecha_agregado = DateTimeField(default=datetime.now)  # Usando DateTimeField con valor por defecto
    id_categoria_alimento = ForeignKeyField(CategoriaAlimento, backref='despensa', on_delete='SET NULL', null=True)

    class Meta:
        database = database
        table_name = 'despensa'
