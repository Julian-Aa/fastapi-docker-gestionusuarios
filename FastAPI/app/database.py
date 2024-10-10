from peewee import MySQLDatabase
from dotenv import load_dotenv
import os
import peewee

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Configuración de la base de datos MySQL utilizando las variables de entorno
database = MySQLDatabase(
    os.getenv("MYSQL_DATABASE", "gestionusuarios"),  # Nombre de la base de datos
    user=os.getenv("MYSQL_USER", "root"),            # Usuario de MySQL
    password=os.getenv("MYSQL_PASSWORD", "root"),    # Contraseña de MySQL
    host=os.getenv("MYSQL_HOST", "localhost"),       # Host de MySQL
    port=int(os.getenv("MYSQL_PORT", 3306))          # Puerto de MySQL
)

def connect_db():
    """Conecta a la base de datos si no está ya conectada."""
    try:
        if database.is_closed():
            database.connect(reuse_if_open=True)
            print("✅ Conexión a la base de datos establecida.")
    except peewee.OperationalError as e:
        print(f"❌ Error al conectar a la base de datos: {e}")
    except Exception as e:
        print(f"❌ Error inesperado al conectar a la base de datos: {e}")

def close_db():
    """Cierra la conexión de la base de datos si está abierta."""
    try:
        if not database.is_closed():
            database.close()
            print("✅ Conexión a la base de datos cerrada.")
    except peewee.OperationalError as e:
        print(f"❌ Error al cerrar la conexión de la base de datos: {e}")
    except Exception as e:
        print(f"❌ Error inesperado al cerrar la conexión de la base de datos: {e}")

def create_tables(models):
    """Crea las tablas en la base de datos si no existen."""
    try:
        with database:
            database.create_tables(models)
            print("✅ Tablas creadas correctamente o ya existen.")
    except peewee.OperationalError as e:
        print(f"❌ Error al crear las tablas en la base de datos: {e}")
    except Exception as e:
        print(f"❌ Error inesperado al crear las tablas: {e}")
