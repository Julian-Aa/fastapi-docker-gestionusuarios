from peewee import Model, CharField, TextField, ForeignKeyField, AutoField, DateTimeField, BooleanField
from database import database  # Ajustar la ruta según la estructura de tu proyecto
from .usuario import Usuario
from .categoriaReceta import CategoriaReceta
from datetime import datetime

class Receta(Model):  # pylint: disable=too-few-public-methods
    """
    Receta model that represents recipes in the system.

    Attributes:
        id_receta (int): Primary key for the recipe.
        id_usuario (ForeignKey): Reference to the user who created the recipe.
        nombre (str): Name of the recipe.
        descripcion (str): A description of the recipe.
        instrucciones (str): Instructions for preparing the recipe.
        id_categoria_receta (ForeignKey): Reference to the recipe category.
        dificultad (str): The difficulty level of the recipe.
        tiempo_preparacion (str): Time required to prepare the recipe.
        publica (bool): Whether the recipe is public or private.
        fecha_creacion (datetime): When the recipe was created.
        fecha_modificacion (datetime): When the recipe was last modified.
    """
    id_receta = AutoField()
    id_usuario = ForeignKeyField(Usuario, backref='recetas', on_delete='CASCADE', null=True)
    nombre = CharField(max_length=255)
    descripcion = TextField(null=True)
    instrucciones = TextField(null=True)
    id_categoria_receta = ForeignKeyField(CategoriaReceta, backref='recetas', on_delete='SET NULL', null=True)
    dificultad = CharField(max_length=50, null=True)
    tiempo_preparacion = CharField(max_length=50, null=True)
    publica = BooleanField(default=False)

    # Cambiado a DateTimeField con valores predeterminados
    fecha_creacion = DateTimeField(default=datetime.now)
    fecha_modificacion = DateTimeField(default=datetime.now)

    class Meta:
        database = database
        table_name = 'recetas'
