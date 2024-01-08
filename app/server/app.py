from fastapi import FastAPI
from server.routes.user import router as UserRouter

app = FastAPI(docs_url="/docs")

app.include_router(UserRouter, tags=["User"], prefix="/user")

@app.get("/", tags=["Root"])
async def welcome():
    return {"message": "This page doesn't contain any data"}

