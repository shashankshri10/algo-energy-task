from fastapi import Depends,FastAPI

from .routes import user,asset

app = FastAPI()

app.include_router(user.router)
app.include_router(asset.router)