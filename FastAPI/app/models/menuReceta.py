from peewee import Model, ForeignKeyField, AutoField, DateTimeField
from database import database
from .menu import Menu
from .receta import Receta
from datetime import datetime

class MenuReceta(Model):
    """
    MenuReceta model that represents the relationship between menus and recipes.

    Attributes:
        id_menu_receta (int): Primary key for the menu-recipe relationship.
        id_menu (ForeignKey): Reference to the associated menu.
        id_receta (ForeignKey): Reference to the associated recipe.
        fecha (DateTimeField): The date and time on which the recipe is part of the menu.
    """
    id_menu_receta = AutoField()
    id_menu = ForeignKeyField(Menu, backref='menu_recetas', on_delete='CASCADE', null=True)
    id_receta = ForeignKeyField(Receta, backref='menu_recetas', on_delete='CASCADE', null=True)
    
    # Cambiado de DateField a DateTimeField
    fecha = DateTimeField(default=datetime.now, null=True)

    class Meta:
        database = database
        table_name = 'menu_recetas'
