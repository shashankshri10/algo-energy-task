from datetime import datetime
from typing import Optional
from fastapi import Header, HTTPException
from jose import jwt
from app.services.asset_service import AssetService
import os 
SECRET_KEY = os.getenv("SECRET_KEY") 
ALGORITHM = os.getenv("ALGORITHM") 
asset_service = AssetService()

async def verify_token(token: Optional[str] = Header(None)) -> str:
    if not token:
        raise HTTPException(status_code=401, detail="Missing token")
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("user_id")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        expiration = payload.get("exp")
        if expiration is not None and expiration < datetime.utcnow().timestamp():
            raise HTTPException(status_code=401, detail="Token has expired")
        return user_id
    except jwt.JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

async def verify_asset(asset_id:str,token: Optional[str] = Header(None)) -> str:
    if not token:
        raise HTTPException(status_code=401, detail="Missing token")
    if not asset_id:
        raise HTTPException(status_code=401, detail="Missing asset id")
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("user_id")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        expiration = payload.get("exp")
        if expiration is not None and expiration < datetime.utcnow().timestamp():
            raise HTTPException(status_code=401, detail="Token has expired")
        assets = await asset_service.get_assets_by_user_id(user_id)
        if not assets:
            raise HTTPException(status_code=401, detail="No assets found")
        asset_found=False
        for asset in assets:
            if (asset["_id"]==asset_id):
                asset_found = True
                break
        if asset_found is False:
            raise HTTPException(status_code=401, detail="No assets found")
        pass
    except jwt.JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

        