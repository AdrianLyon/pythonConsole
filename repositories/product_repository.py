from sqlalchemy.orm import Session
from models import Product

class ProductRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_product(self, name: str, description: str, price: int, category_id: int):
        product = Product(name=name, description=description, price=price, category_id=category_id)
        self.db.add(product)
        self.db.commit()
        self.db.refresh(product)
        return product

    def list_products(self):
        return self.db.query(Product).all()
