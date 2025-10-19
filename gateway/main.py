from fastapi import FastAPI
from Routers.FontXyzRoute import router as routerAuth
app = FastAPI()

app.include_router(routerAuth)
    
