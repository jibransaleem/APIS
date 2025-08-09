from sqlalchemy import create_engine, Column, Integer, String, CheckConstraint, CHAR, Boolean, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, Mapped, mapped_column, relationship
from datetime import timedelta , datetime
from typing import Dict , List,Annotated,Optional
from starlette import status
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from jose import JWTError , jwt 
from fastapi.security import OAuth2PasswordRequestForm,OAuth2PasswordBearer

# Database connection

# Dependency
def get_db():
    try:
        db = localsession()
        yield db
    finally:
        db.close()
Base = declarative_base()

# User class
class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(String(30), unique=True, nullable=False)
    first_name: Mapped[str] = mapped_column(String(50), nullable=False)
    last_name: Mapped[str] = mapped_column(String(50))
    password: Mapped[str] = mapped_column(String(50), nullable=False)

    todos: Mapped[list["Todo"]] = relationship(back_populates="users", cascade="all, delete")

    def __init__(self, email, first_name, last_name, password):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
# Todo class
class Todo(Base):
    __tablename__ = "todo"

    todo_id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False, autoincrement=True)
    done: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    description: Mapped[str] = mapped_column(String(200), nullable=True)

    # Foreign key & relationship
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    users: Mapped["User"] = relationship(back_populates="todos")

    def __init__(self, done, description):
        self.done = done
        self.description = description
url = "sqlite:///database.db"
engine = create_engine(url, echo=True)
localsession = sessionmaker(bind=engine, autoflush=False)


# Create tables
Base.metadata.create_all(bind=engine)

