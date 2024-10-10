from peewee import Model, CharField, DateTimeField, AutoField
from database import database  # Asegúrate de que la importación es correcta
from datetime import datetime

class Usuario(Model):  # pylint: disable=too-few-public-methods
    """
    Usuario model that represents the users in the system.

    Attributes:
        id_usuario (int): Primary key.
        nombre (str): Name of the user.
        email (str): Email of the user (must be unique).
        password (str): User password (encrypted).
        foto_perfil (str, optional): URL to the user's profile picture.
        rol (str): Role of the user, defaults to 'usuario'.
        fecha_creacion (datetime): When the user was created.
        fecha_modificacion (datetime): When the user was last modified.
    """
    id_usuario = AutoField()
    nombre = CharField(max_length=255)
    email = CharField(max_length=255, unique=True)
    password = CharField(max_length=255)
    foto_perfil = CharField(max_length=255, null=True)
    rol = CharField(max_length=50, default='usuario')
    
    # Cambiado a DateTimeField con valores predeterminados
    fecha_creacion = DateTimeField(default=datetime.now)
    fecha_modificacion = DateTimeField(default=datetime.now)

    class Meta:
        database = database
        table_name = 'usuarios'
