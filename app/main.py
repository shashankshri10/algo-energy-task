from fastapi import FastAPI

from .routes import user,asset,performance_metric

app = FastAPI()

app.include_router(user.router)
app.include_router(asset.router)
app.include_router(performance_metric.router)