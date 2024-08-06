from fastapi import FastAPI
from routers import subjects, users, notices
import uvicorn
import os
from dependencies import client, connect_to_database, close_database_connection
from mangum import Mangum

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    await connect_to_database()

@app.on_event("shutdown")
async def shutdown_event():
    await close_database_connection()

app.include_router(notices.router)
app.include_router(users.router)
app.include_router(subjects.router)

handler = Mangum(app)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 8000)))
