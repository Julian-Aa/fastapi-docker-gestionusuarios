"""
This module defines the ItemLista model for the database.

The ItemLista model represents an item in a shopping list, which is associated
with a list and an ingredient.
"""

from peewee import Model, ForeignKeyField, AutoField, DecimalField, BooleanField
from database import database  # Ajusta la ruta según la estructura de tu proyecto
from .listaCompra import ListaCompra
from .ingrediente import Ingrediente

class ItemLista(Model):  # pylint: disable=too-few-public-methods
    """
    ItemLista model that represents an item in a shopping list.

    Attributes:
        id_item_lista (int): Primary key for the item.
        id_lista (ForeignKey): Reference to the shopping list (ListaCompra).
        id_ingrediente (ForeignKey): Reference to the ingredient.
        cantidad (DecimalField): Quantity of the item in the list.
        disponible (bool): Whether the item is available.
    """
    id_item_lista = AutoField()
    id_lista = ForeignKeyField(ListaCompra, backref='items_lista', on_delete='CASCADE', null=True)
    id_ingrediente = ForeignKeyField(Ingrediente, backref='items_lista', on_delete='CASCADE', null=True)
 #   cantidad = DecimalField(max_digits=10, decimal_places=2, null=True)
    disponible = BooleanField(default=False)

    class Meta:
        database = database
        table_name = 'items_lista'
