from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import subjects, users, notices
import uvicorn
import os
from dependencies import MongoDB

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    await MongoDB.connect()

@app.on_event("shutdown")
async def shutdown_event():
    await MongoDB.close()

app.include_router(notices.router)
app.include_router(users.router)
app.include_router(subjects.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT")))