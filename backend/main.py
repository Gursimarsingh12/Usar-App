from fastapi import FastAPI
from routers import subjects, users, notices
import uvicorn
import os
from mangum import Mangum

app = FastAPI()

app.include_router(notices.router)
app.include_router(users.router)
app.include_router(subjects.router)

handler = Mangum(app=app)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT")))