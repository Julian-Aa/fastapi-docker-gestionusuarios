"""
This module defines the UsuarioGrupo model for the database.

The UsuarioGrupo model represents the many-to-many relationship between
users and groups, including the role of the user in the group.
"""

from peewee import Model, ForeignKeyField, CharField
from database import database  # Ajustar la ruta según la estructura de tu proyecto
from .usuario import Usuario
from .grupo import Grupo

class UsuarioGrupo(Model):  # pylint: disable=too-few-public-methods
    """
    UsuarioGrupo model that represents the user-group relationships.

    Attributes:
        id_usuario (ForeignKey): Reference to the user in the group.
        id_grupo (ForeignKey): Reference to the group.
        rol (str): The role of the user in the group (default is 'miembro').
    """
    id_usuario = ForeignKeyField(Usuario, backref='grupos', on_delete='CASCADE')
    id_grupo = ForeignKeyField(Grupo, backref='usuarios', on_delete='CASCADE')
    rol = CharField(max_length=50, default='miembro')

    class Meta:
        database = database
        table_name = 'usuarios_grupos'
        primary_key = False
