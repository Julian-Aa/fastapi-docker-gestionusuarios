from peewee import Model, CharField, DateTimeField, ForeignKeyField, AutoField
from database import database
from .usuario import Usuario
from datetime import datetime

class Menu(Model):
    id_menu = AutoField()
    id_usuario = ForeignKeyField(Usuario, backref='menus', on_delete='CASCADE', null=True)
    nombre = CharField(max_length=255, null=True)
    
    # Usando DateTimeField para manejar fechas y horas
    fecha_inicio = DateTimeField(default=datetime.now, null=True)
    fecha_fin = DateTimeField(null=True)
    recurrencia = CharField(max_length=50, null=True)

    class Meta:
        database = database
        table_name = 'menus'
