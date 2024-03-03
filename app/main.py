from fastapi import Depends,FastAPI

from .routes import user

app = FastAPI()

app.include_router(user.router)