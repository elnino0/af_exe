
from fastapi import APIRouter
from Services.ForntXyZService import ForntXyZService
from fastapi import  UploadFile, File

router = APIRouter(
    prefix="/fontxyz",
    tags=["fontxyz"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)

forntXyZService = ForntXyZService()
@router.post("/scan")
async def scanFile(file: UploadFile = File(...)):
    return forntXyZService.uploadFile(file)
