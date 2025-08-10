from fastapi import  APIRouter ,Depends,HTTPException
from fastapi.responses import JSONResponse
from models import TODO
todo_router = APIRouter()
# id : desc
todos =[
       {
           "id":2,
           "desc" :["I have to learn pandas"],
           "done" : False
       } 
        
]
def match_key(key :int )->bool:
    ket = int(key)
    for match in todos:
        if match['id']== key:
            return True
    return False
@todo_router.post("/add_todo")
def add_todo(data:TODO):
    try :
        todo = data.model_dump()
        key = todo['id']
        if   match_key(key): 
            return JSONResponse(status_code=401,content={"message":"key already exixts"}) 
        todos.append(todo) 
        return JSONResponse(status_code=200 , content={"message":"added"})
    except KeyError as e:
        return HTTPException(status_code=404 , detail="server error")     
    
@todo_router.get("/get_todo")
def  get_data():
    return todos
