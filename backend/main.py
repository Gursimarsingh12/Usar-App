from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import subjects, users, notices
import uvicorn
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(notices.router)
app.include_router(users.router)
app.include_router(subjects.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT")))