from pydantic import BaseModel
from typing import Union
class TODO(BaseModel):
    id : int
    desc : list[Union[int , str , bool]]
    done : bool
    
class User(BaseModel):
    username: str
    password: str