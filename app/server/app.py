from fastapi import FastAPI
from server.routes.user import router as UserRouter

app = FastAPI(docs_url="/")

app.include_router(UserRouter, tags=["User"], prefix="/user")

@app.get("/root", tags=["Root"])
async def welcome():
    return {"message": "Welcome to PyMongo+FastAPI app!"}
