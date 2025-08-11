# from fastapi import FastAPI,File,Form,UploadFile,HTTPException
# from fastapi.staticfiles import StaticFiles
# import os
# import shutil
# from fastapi.responses import FileResponse
# app =FastAPI(debug=True)
# # mounting the app to  the upload folder
# FOLDER_PATH = r"C:\Users\Z.S computers\Desktop\fastapi\APIS\apis\FileHandling\upload"
# os.makedirs(FOLDER_PATH , exist_ok=True)
# app.mount("/static_file", StaticFiles(directory=(FOLDER_PATH)))

# # ROUTE FOR UPLOADING THE FILE
# @app.post("/upload_file")
# def upload_file(file :UploadFile =File(...)):
#     file_complete_path = os.path.join(FOLDER_PATH , file.filename)
    
#     #storing the  file
#     with open(file_complete_path , "wb") as f :
#         shutil.copyfileobj(file.file,f)
    
#     file_url = f"/static/{file.filename}"
#     return file_url
# # Route for displaying file by  file name
# @app.get("/get_file/{file_name}")
# def get_file(file_name):
#     file_name= file_name.strip()
#     try  :
#         file_path =os.path.join(FOLDER_PATH,file_name)
#         if os.path.exists(file_path):
#             return FileResponse(path = file_path , filename=file_name ,media_type='text/plain')
#     except FileExistsError:
#         raise HTTPException(status_code = 404  ,detail ="file not  found")
# ypical structure of each error dict:
# python
# Copy
# Edit
# {
#   'loc': ('body', 'field_name'),  # where error happened (e.g. in request body, which field)
#   'msg': 'field required',         # human-readable error message
#   'type': 'value_error.missing'   # error type code
}