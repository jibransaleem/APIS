# # from fastapi import FastAPI
# # from fastapi import Header
# # app = FastAPI()

# # @app.get("/")
# # def home():
# #     return {"message": "hello"}

# # @app.get("/get")
# # def index(name: str):
# #     return {"name": f"My name is {name}"}

# # @app.get("/header" , status_code=400)
# # def get_header(
# #     accept : str = Header(None),
# #     content_type : str = Header(None),
# #     user_agent : str = Header(None),
# #     host : str = Header(None)
# #     ):
# #     request_headers = {}
# #     request_headers['host']=host
# #     request_headers['user_agent']=user_agent
# #     request_headers['accept']= accept
# #     request_headers['content_type']= content_type
# #     return request_headers

# # Database connection

# # Dependency
# def get_db():
#     try:
#         db = localsession()
#         yield db
#     finally:
#         db.close()
# Base = declarative_base()

# # User class
# class User(Base):
#     __tablename__ = "user"

#     id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
#     email: Mapped[str] = mapped_column(String(30), unique=True, nullable=False)
#     first_name: Mapped[str] = mapped_column(String(50), nullable=False)
#     last_name: Mapped[str] = mapped_column(String(50))
#     password: Mapped[str] = mapped_column(String(50), nullable=False)

#     todos: Mapped[list["Todo"]] = relationship(back_populates="users", cascade="all, delete")

#     def __init__(self, email, first_name, last_name, password):
#         self.email = email
#         self.first_name = first_name
#         self.last_name = last_name
#         self.password = password
# # Todo class
# class Todo(Base):
#     __tablename__ = "todo"

#     todo_id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False, autoincrement=True)
#     done: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
#     description: Mapped[str] = mapped_column(String(200), nullable=True)

#     # Foreign key & relationship
#     user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
#     users: Mapped["User"] = relationship(back_populates="todos")

#     def __init__(self, done, description):
#         self.done = done
#         self.description = description
# url = "sqlite:///database.db"
# engine = create_engine(url, echo=True)
# localsession = sessionmaker(bind=engine, autoflush=False)


# # Create tables
# Base.metadata.create_all(bind=engine)

