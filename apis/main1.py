from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from models import User_Reg
from APIS.apis.sqlalchemy.db import get_db, User
app = FastAPI()

@app.post("/create_account")
def create_account(obj: User_Reg, db: Session = Depends(get_db)):
    data = obj.model_dump()  # ✅ For Pydantic v2
    check_email = data["email"]

    # Check if user already exists
    checker = db.query(User).filter(User.email == check_email).first()
    if checker:  # ✅ No len() needed
        return {"message": "Account with this email is in use"}

    # Create new user
    new_user = User(
        email=check_email,
        last_name=data["last_name"],
        first_name=data["first_name"],
        password=data["password"]
    )

    db.add(new_user)     # ✅ Add to session
    db.commit()          # ✅ Save to DB
    db.refresh(new_user) # ✅ Get auto-generated ID & updated fields

    return {"message": "Account created successfully", "user_id": new_user.id}
