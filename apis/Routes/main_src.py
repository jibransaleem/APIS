from  todo_route import todo_router
from  login_route import login_router
from fastapi import FastAPI


app = FastAPI(debug=True)

app.include_router(router=todo_router , prefix='/todo',tags=['Todo'])
app.include_router(router=login_router , prefix='/auth',tags=['auth'])