# from fastapi import FastAPI
# from fastapi import Header
# app = FastAPI()

# @app.get("/")
# def home():
#     return {"message": "hello"}

# @app.get("/get")
# def index(name: str):
#     return {"name": f"My name is {name}"}

# @app.get("/header" , status_code=400)
# def get_header(
#     accept : str = Header(None),
#     content_type : str = Header(None),
#     user_agent : str = Header(None),
#     host : str = Header(None)
#     ):
#     request_headers = {}
#     request_headers['host']=host
#     request_headers['user_agent']=user_agent
#     request_headers['accept']= accept
#     request_headers['content_type']= content_type
#     return request_headers