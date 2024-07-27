from db import Base, engine, get_db
from models import User, Product, Category
from services.user_service import UserService
from menus import login

# Crear las tablas
Base.metadata.create_all(bind=engine)

# Crear un usuario administrador por defecto si no existen usuarios
db = next(get_db())
user_service = UserService(db)
user_service.initialize_admin_user()

if __name__ == "__main__":
    login()
