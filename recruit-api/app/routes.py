from fastapi import APIRouter, FastAPI, Request, Form
from services import Hello,getUser,post_user
from pydantic import BaseModel
# from models.model import StudentAnswerSheet
import json

class UserModel(BaseModel):
    user_id: str
    password: str

router = APIRouter()

@router.get("/hello")
async def hello():
    return {"message": Hello()}


@router.get("/users/{user_id}")
async def get_user(user_id):
    return getUser(user_id)

@router.post("/signup")
async def create(user: UserModel):
    return {
"message": "Account successfully created",
"user": {
  "user_id": user.user_id,
  "nickname": "TaroYamada"
}
}

@router.post("/test")
async def test(data):
    return {"ss": data}
