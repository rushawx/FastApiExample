from typing import List

from fastapi import APIRouter, Request

from data.db import dogs_db
from models.dog import Dog

router = APIRouter(prefix="/dogs", tags=["dogs"])


@router.get("/dog")
async def get_dog(request: Request, kind: str) -> List[Dog]:
    response = []
    for _, dog in dogs_db.items():
        if dog.kind == kind:
            response.append(dog)
    return response


@router.post("/dog")
async def post_dog(request: Request, dog: Dog) -> Dog:
    idx = max(dogs_db.keys())
    dogs_db[idx] = dog
    return dog


@router.get("/dog/{pk}")
async def get_dog_by_pk(request: Request, pk: int) -> Dog | None:
    for _, dog in dogs_db.items():
        if dog.pk == pk:
            return dog
    return None


@router.patch("/dog/{pk}")
async def patch_dog(request: Request, pk: int, dog: Dog) -> Dog | None:
    for idx, val in dogs_db.items():
        if val.pk == pk:
            dogs_db[idx] = dog
            break
    return dog
