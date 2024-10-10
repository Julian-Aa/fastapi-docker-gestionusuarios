from peewee import Model, CharField, AutoField, DateTimeField, SQL
from database import database  # Ajustar la ruta según la estructura de tu proyecto
from datetime import datetime

class Grupo(Model):  # pylint: disable=too-few-public-methods
    """
    Grupo model that represents groups in the system.

    Attributes:
        id_grupo (int): Primary key for the group.
        nombre (str): Name of the group.
        fecha_creacion (datetime): The timestamp when the group was created.
        fecha_modificacion (datetime): The timestamp when the group was last modified.
    """
    id_grupo = AutoField()
    nombre = CharField(max_length=255)
    
    # Usando DateTimeField para manejar mejor las fechas con valores por defecto
    fecha_creacion = DateTimeField(default=datetime.now)
    fecha_modificacion = DateTimeField(default=datetime.now, constraints=[SQL('DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP')])

    class Meta:
        database = database
        table_name = 'grupos'
