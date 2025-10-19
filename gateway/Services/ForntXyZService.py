from fastapi import UploadFile
import HttpClient.XyzClient as XyzClient
from config import AppConfig
import shutil
from pathlib import Path
max_size = 10 * 1024 * 1024

class ForntXyZService:
    def __init__(self):
        self.client = XyzClient.XyzClient(AppConfig.xyz_api_url,AppConfig.xyz_api_key)


    def uploadFile(self, file: UploadFile):
        filename = file.filename
        if file.size > max_size :
            raise FileNotFoundError("File is too big")
        new_dir = Path("uploads")
        try:
            new_dir.mkdir()
        except FileExistsError:
            print(f"Directory '{new_dir}' already exists.")
        try:
            with open(f"uploads/{filename}", "wb") as buffer:
                shutil.copyfileobj(file.file, buffer)
                return self.client.uploadFile(f"uploads/{filename}")
        finally:
            Path.unlink(f"uploads/{filename}")