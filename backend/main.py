from fastapi import FastAPI
from routers import subjects
import uvicorn
import os

app = FastAPI()

app.include_router(subjects.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT")))