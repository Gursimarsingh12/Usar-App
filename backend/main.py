from fastapi import FastAPI
from routers import subjects, users, notices
from dependencies import MongoDBClient
import uvicorn
import os

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    await MongoDBClient.get_client()

@app.on_event("shutdown")
async def shutdown_event():
    await MongoDBClient.close_client()

app.include_router(notices.router)
app.include_router(users.router)
app.include_router(subjects.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 8000)))
