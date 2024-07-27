from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True)
    age = Column(Integer)
    username = Column(String(50), unique=True, index=True)
    password = Column(String(100))

    def __repr__(self):
        return f"<User(id={self.id}, name={self.name}, age={self.age}, username={self.username})>"

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True)
    description = Column(String(255))
    price = Column(Integer)
    category_id = Column(Integer, ForeignKey('categories.id'))

    def __repr__(self):
        return f"<Product(id={self.id}, name={self.name}, description={self.description}, price={self.price}, category_id={self.category_id})>"

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, index=True)
    products = relationship("Product", back_populates="category")

    def __repr__(self):
        return f"<Category(id={self.id}, name={self.name})>"

Product.category = relationship("Category", back_populates="products")
