from typing import Annotated, Literal, Any
from pydantic import BaseModel, Field
from fastapi import Path, Query, APIRouter

router = APIRouter()


class BaseUser(BaseModel):
    username: str
    email: str
    full_name: str | None = None


class UserIn(BaseUser):
    password: str


@router.post("/user12/", response_model=BaseModel)
async def create_user(user: UserIn) -> BaseUser:
    return user
