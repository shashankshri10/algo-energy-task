from datetime import datetime
from typing import Optional
from fastapi import Header, HTTPException
from jose import jwt
import os 
SECRET_KEY = os.getenv("SECRET_KEY") 
ALGORITHM = os.getenv("ALGORITHM") 

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
