from fastapi import FastAPI, File, UploadFile, HTTPException, Request,Depends
from fastapi.responses import FileResponse, JSONResponse

from fastapi.exceptions import RequestValidationError
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel ,constr 
import regex
from pathlib import Path
import shutil
import mimetypes
import os

app = FastAPI(debug=True)

# Folder to store uploaded files
FOLDER_PATH = Path(r"C:\Users\Z.S computers\Desktop\fastapi\APIS\apis\FileHandling\upload")
FOLDER_PATH.mkdir(parents=True, exist_ok=True)

# Mount static files to serve uploaded files
app.mount("/static_file", StaticFiles(directory=FOLDER_PATH), name="static_file")

# Custom validation error handler
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = []
    for err in exc.errors():
        errors.append({
            "message": err['msg'],
            "field": ".".join(map(str, err['loc']))
        })
    return JSONResponse(
        status_code=400,
        content={
            "status": "error",
            "error": errors,
            "message": "Validation failed"
        }
    )

# Upload endpoint
@app.post("/upload_file/")
def upload_file(file: UploadFile = File(...)):
    destination = FOLDER_PATH / file.filename

    # Save uploaded file
    try:
        with destination.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    finally:
        file.file.close()

    file_url = f"/static_file/{file.filename}"
    return {"file_url": file_url}

# Pydantic model to validate file_name with constraints
class FileNameModel(BaseModel):
    file_name: constr(min_length=1, max_length=100)

# Dependency to extract and validate the path param
def get_validated_file_name(file_name: str) -> FileNameModel:
    return FileNameModel(file_name=file_name)

@app.get("/get_file/{file_name}")
def get_file(file: FileNameModel = Depends(get_validated_file_name)):
    safe_path = (FOLDER_PATH / file.file_name).resolve()
    if not str(safe_path).startswith(str(FOLDER_PATH.resolve())):
        raise HTTPException(status_code=400, detail="Invalid file path")

    if not safe_path.exists() or not safe_path.is_file():
        raise HTTPException(status_code=404, detail="File not found")

    media_type, _ = mimetypes.guess_type(str(safe_path))
    media_type = media_type or "application/octet-stream"
    return FileResponse(path=str(safe_path), filename=file.file_name, media_type=media_type)