from fastapi import APIRouter, Depends, HTTPException
from app.models.user import User
from app.services.user_service import UserService

router = APIRouter()
user_service = UserService()

@router.post("/register/")
async def register_user(user: User):
    try:
        res_dict =  await user_service.create_user(user)
        print(res_dict["status"])
        if res_dict["status"]:
            return {"message": res_dict["message"]}
        else:
            raise HTTPException(status_code=401, detail=res_dict["message"])
            
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/login/")
async def login_user(username: str, password: str):
    try:
        authenticated = await user_service.authenticate_user(username, password)
        if authenticated:
            return {"message": "Login successful", "token" : authenticated["token"]}
        else:
            raise HTTPException(status_code=401, detail="Incorrect username or password")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
