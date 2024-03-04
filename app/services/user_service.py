import bcrypt
from datetime import datetime, timedelta
from app.models.user import User
from app.db import connect_to_mongodb,close_mongodb_connection
from jose import jwt
import os

class UserService:
    # Function to insert the user
    async def create_user(self, user: User) -> dict:
        database = await connect_to_mongodb()
        user_data = await database.users.find_one({"username":user.username})
        if user_data is not None:
            return {"status": False, "message":"Username already exists"}
        if len(user.password) < 8:
            return {"status": False, "message":"Password is less than 8 characters"}
        hashed_password = await self.hash_password(user.password)
        user_data = user.model_dump()
        user_data['password'] = hashed_password
        result = await database.users.insert_one(user_data)
        await close_mongodb_connection(database)
        if result.acknowledged:
            return {"status":True,"message":f"User created with id:{result.inserted_id}"}
        return {"status":False,"message":"Could not insert user"}
        

    async def hash_password(self, password: str) -> str:
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    async def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))

    # Function to login
    async def authenticate_user(self, username: str, password: str) -> dict:
        database = await connect_to_mongodb()
        user_data = await database.users.find_one({"username": username})
        await close_mongodb_connection(database)
        if not user_data:
            return {"status": False, "message": "User not found"}
        
        hashed_password = user_data.get('password')
        if not await self.verify_password(password, hashed_password):
            return {"status": False, "message": "Incorrect password"}
        
        # Generate JWT token
        token = self.generate_jwt_token(str(user_data['_id']))

        return {"status": True, "message": "Login successful", "token": token,"user_id":str(user_data["_id"])}
    
    async def find_user_by_username(self, username: str):
        database = await connect_to_mongodb()
        user_data = await database.users.find_one({"username": username})
        await close_mongodb_connection(database)
        return user_data

    def generate_jwt_token(self, user_id: str) -> str:
        payload = {
            'user_id': user_id,
            'exp': datetime.utcnow() + timedelta(days=7)
        }
        # Replace 'your_secret_key' with your actual secret key
        return jwt.encode(payload, os.getenv("SECRET_KEY"), algorithm=os.getenv("ALGORITHM"))
