from fastapi import Request, FastAPI
import time
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


# agr do middle wear hen to dono chlnge

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (for testing)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Custom middleware
@app.middleware("http")
async def middle_wear(request: Request, call_next):
    start = time.time()
    response = await call_next(request)
    process_time = time.time() - start
    response.headers["X-Request-Process-Time"] = str(process_time)
    print(f"📌 Request took: {process_time:.4f} seconds for {request.url.path}")

    return response

@app.get("/login")
def login():
    return {"message": "login"}

@app.get("/logout")
def logout():
    return {"message": "logout"}
