from pydantic import BaseModel , EmailStr , Field
from typing import Optional
class User_Reg(BaseModel):
    first_name : str = Field(... ,description="Enter your name" , example="Jibran")
    last_name  : Optional[str] =Field(default=None,description="Enter your last name",example="saleem")
    email : EmailStr=Field(description="Enter your email" , example="...@gmail.com")
    password : str 
    