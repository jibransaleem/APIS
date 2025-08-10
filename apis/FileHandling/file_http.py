from fastapi import FastAPI, File, Form, UploadFile
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import shutil
import os

UPLOAD_FOLDER = r"APIS\apis\FileHandling\uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app = FastAPI()

# Serve static files from UPLOAD_FOLDER
app.mount("/static_file", StaticFiles(directory=UPLOAD_FOLDER), name="static")

@app.post("/upload_file/")
async def upload_file(file: UploadFile = File(...), description: str = Form(...)):
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    with open(file_path, "wb") as f:
        shutil.copyfileobj(file.file, f)
        
    file_url = f"/static_file/{file.filename}"  # fixed URL to match mounted path
    return {"filename": file.filename, "file_url": file_url}

@app.get("/get_file")
async def get_file():
    file_path = r"C:\Users\Z.S computers\Desktop\fastapi\APIS\apis\FileHandling\uploads\wa.jpg"
    return FileResponse(path=file_path, filename="wa.jpg", media_type="image/jpeg")  # added return
