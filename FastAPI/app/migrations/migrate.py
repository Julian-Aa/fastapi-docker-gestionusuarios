from peewee_migrate import Router
from models.usuario import Usuario
from models.receta import Receta
from models.despensa import Despensa
from models.grupo import Grupo
from models.ingrediente import Ingrediente
from models.menu import Menu
from models.notificacion import Notificacion
from models.listaCompra import ListaCompra
from models.menuReceta import MenuReceta
from models.usuarioGrupo import UsuarioGrupo
from models.categoriaAlimento import CategoriaAlimento
from models.categoriaReceta import CategoriaReceta
from database import database  # Asegúrate de que esta ruta sea correcta

# Define el router de migraciones, apuntando al directorio de migraciones
router = Router(database, migrate_dir='migrations')

if __name__ == "__main__":
    # Crear una nueva migración automáticamente basada en los modelos
    router.create(auto=True)
    print("Ejecutando migraciones...")

    # Ejecutar las migraciones pendientes
    router.run(fake=True)
    database.create_tables([
        CategoriaAlimento,
        CategoriaReceta,
        Despensa,
        Grupo,
        Ingrediente,
        Menu,
        Notificacion,
        ListaCompra,
        Receta,          # Asegúrate de que Receta esté antes de MenuReceta
        MenuReceta,      # MenuReceta depende de Receta y Menu
        UsuarioGrupo,
        Usuario
    ])
    print("Migraciones completadas.")
