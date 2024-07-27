from db import get_db
from services.user_service import UserService
from services.product_service import ProductService
from services.category_service import CategoryService
import getpass

def login():
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    db = next(get_db())
    user_service = UserService(db)
    user = user_service.get_user_by_username(username)
    if user and user.password == password:
        print("Login successful!")
        show_menu()
    else:
        print("Invalid credentials.")

def show_menu():
    while True:
        print("1. Crear usuario")
        print("2. Listar usuarios")
        print("3. Crear categoría")
        print("4. Listar categorías")
        print("5. Crear producto")
        print("6. Listar productos")
        print("7. Salir")
        choice = input("Selecciona una opción: ")
        
        db = next(get_db())
        user_service = UserService(db)
        category_service = CategoryService(db)
        product_service = ProductService(db)

        if choice == '1':
            name = input("Nombre: ")
            age = int(input("Edad: "))
            username = input("Username: ")
            password = getpass.getpass("Password: ")
            user_service.create_user(name, age, username, password)
        elif choice == '2':
            users = user_service.list_users()
            for user in users:
                print(user)
        elif choice == '3':
            name = input("Nombre de la categoría: ")
            category_service.create_category(name)
        elif choice == '4':
            categories = category_service.list_categories()
            for category in categories:
                print(category)
        elif choice == '5':
            name = input("Nombre del producto: ")
            description = input("Descripción: ")
            price = int(input("Precio: "))
            category_id = int(input("ID de la categoría: "))
            product_service.create_product(name, description, price, category_id)
        elif choice == '6':
            products = product_service.list_products()
            for product in products:
                print(product)
        elif choice == '7':
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")
