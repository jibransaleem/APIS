from fastapi import Request , middleware
from fastapi import FastAPI

app = FastAPI()

@app.get("/login")
def login():
    return {"message":"login"}
@app.get("/logout")
def logout():
    return {"message":"logout"}