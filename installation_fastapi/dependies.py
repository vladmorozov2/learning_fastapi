from typing import Annotated

from fastapi import Depends, FastAPI, APIRouter

router = APIRouter()


async def common_parameters(q: str | None = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}


@router.get("/items6543/", tags=["Depends"])
async def read_items(commons: Annotated[dict, Depends(common_parameters)]):
    return commons


@router.get("/users/", tags=["Depends"])
async def read_users(commons: Annotated[dict, Depends(common_parameters)]):
    return commons
