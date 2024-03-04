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

from fastapi import HTTPException

@router.post("/login/")
async def login_user(username: str, password: str):
    try:
        # Check if the username is present in the database
        user_data = await user_service.find_user_by_username(username)
        if not user_data:
            # If username is not found, raise an HTTPException with status code 404
            raise HTTPException(status_code=404, detail="User not found")

        # If username is found, authenticate the user with the provided password
        authenticated = await user_service.authenticate_user(username, password)
        print(authenticated)
        if authenticated["status"]:
            # If authentication is successful, return a success message and token
            return {"message": "Login successful", "token": authenticated["token"],"user_id":authenticated["user_id"]}
        else:
            raise HTTPException(status_code=401, detail="Incorrect Password")
    except Exception as e:
        # Handle other exceptions (e.g., database errors) and raise an HTTPException with status code 500
        raise HTTPException(status_code=500, detail=str(e))

