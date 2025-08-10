from fastapi import APIRouter
login_router = APIRouter()



@login_router.post("/signup")
def signup():
    return {"message": "Signup successful"}

@login_router.post("/login")
def login():
    return {"message": "Login successful"}
