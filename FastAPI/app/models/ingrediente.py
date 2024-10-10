from peewee import Model, CharField, AutoField, DecimalField
from database import database  # Ajustar la ruta según la estructura de tu proyecto
#from decimal import ROUND_HALF_EVEN

class Ingrediente(Model):  # pylint: disable=too-few-public-methods
    """
    Ingrediente model that represents ingredients in the system.
    """
    id_ingrediente = AutoField()
    nombre = CharField(max_length=255, unique=True)
#    calorias = DecimalField(max_digits=10, decimal_places=2, rounding=ROUND_HALF_EVEN, null=True)  # Aquí usa ROUND_HALF_EVEN
    categoria = CharField(max_length=100, null=True)
    unidad = CharField(max_length=50, null=True)

    class Meta:
        database = database
        table_name = 'ingredientes'
