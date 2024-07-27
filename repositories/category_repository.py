from sqlalchemy.orm import Session
from models import Category

class CategoryRepository:
    def __init__(self, db: Session):
        self.db = db
    def create_category(self, name: str):
        category = Category(name=name)
        self.db.add(category)
        self.db.commit()
        self.db.refresh(category)
        return category
    def list_category(self):
        return self.db.query(Category).all()
