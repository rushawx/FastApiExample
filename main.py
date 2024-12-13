import uvicorn
from fastapi import FastAPI, Request

from handlers.dogs import router as dog_router
from handlers.posts import router as post_router

app = FastAPI()
app.include_router(post_router)
app.include_router(dog_router)


@app.get("/")
def root(request: Request):
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
