import datetime

from fastapi import APIRouter, Request
from models.timestamp import Timestamp
from data.db import post_db


router = APIRouter(
    prefix="/posts",
    tags=["posts"]
)


@router.post("/post")
async def post_record(request: Request) -> Timestamp:
    post_record = Timestamp(
        id=post_db[-1].id + 1,
        timestamp=int(datetime.datetime.now().timestamp()),
    )
    post_db.append(post_record)
    return post_record
