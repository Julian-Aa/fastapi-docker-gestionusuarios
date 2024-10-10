from peewee import Model, CharField, TextField, ForeignKeyField, AutoField, DateTimeField
from database import database  # Ajustar según la estructura de tu proyecto
from .usuario import Usuario
from datetime import datetime

class Notificacion(Model):  # pylint: disable=too-few-public-methods
    """
    Notificacion model that represents notifications in the system.

    Attributes:
        id_notificacion (int): Primary key.
        id_usuario (int): Foreign key referring to the associated user.
        tipo (str): The type of notification.
        mensaje (str): The content of the notification.
        fecha_envio (datetime): The date and time when the notification was sent.
    """
    id_notificacion = AutoField()
    id_usuario = ForeignKeyField(Usuario, backref='notificaciones', on_delete='CASCADE', null=True)
    tipo = CharField(max_length=50, null=True)
    mensaje = TextField(null=True)

    # Cambiado de TimestampField a DateTimeField
    fecha_envio = DateTimeField(default=datetime.now, null=True)

    class Meta:
        database = database
        table_name = 'notificaciones'
