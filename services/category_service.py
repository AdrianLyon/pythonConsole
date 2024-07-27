from sqlalchemy.orm import Session
from repositories.category_repository import CategoryRepository

class CategoryService:
    def __init__(self, db: Session):
        self.category_repo = CategoryRepository(db)

    def create_category(self, name:str):
        return self.category_repo.create_category(name)

    def list_categories(self):
        return self.category_repo.list_category()
