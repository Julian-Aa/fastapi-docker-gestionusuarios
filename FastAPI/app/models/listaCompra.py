from peewee import Model, CharField, ForeignKeyField, AutoField, DateTimeField, BooleanField
from database import database  # Ajustar la ruta según la estructura de tu proyecto
from .menu import Menu
from datetime import datetime

class ListaCompra(Model):  # pylint: disable=too-few-public-methods
    """
    ListaCompra model that represents shopping lists.

    Attributes:
        id_lista (int): Primary key for the shopping list.
        id_menu (ForeignKey): Reference to the associated menu.
        nombre (str): Name of the shopping list.
        fecha_creacion (datetime): The date when the list was created.
        comprado (bool): Whether the items in the list have been purchased.
    """
    id_lista = AutoField()
    id_menu = ForeignKeyField(Menu, backref='listas_compras', on_delete='CASCADE', null=True)
    nombre = CharField(max_length=255, null=True)
    
    # Usando DateTimeField para gestionar la fecha de creación
    fecha_creacion = DateTimeField(default=datetime.now)
    
    comprado = BooleanField(default=False)

    class Meta:
        database = database
        table_name = 'listas_compras'
