from sqlalchemy.orm import Session
from repositories.user_repository import UserRepository
from models import User

class UserService:
    def __init__(self, db: Session):
        self.user_repo = UserRepository(db)

    def create_user(self, name: str, age: int, username: str, password: str):
        return self.user_repo.create_user(name, age, username, password)

    def get_user_by_username(self, username: str):
        return self.user_repo.get_user_by_username(username)

    def list_users(self):
        return self.user_repo.list_users()

    def initialize_admin_user(self):
        users = self.list_users()
        if not users:
            self.create_user("Admin", 30, "admin", "admin123")

