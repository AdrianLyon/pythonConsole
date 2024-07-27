from sqlalchemy.orm import Session
from repositories.product_repository import ProductRepository

class ProductService:
    def __init__(self, db: Session):
        self.product_repo = ProductRepository(db)

    def create_product(self, name: str, description: str, price: int, category_id: int):
        return self.product_repo.create_product(name, description, price, category_id)

    def list_products(self):
        return self.product_repo.list_products()

