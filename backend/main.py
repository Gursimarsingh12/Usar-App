from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import subjects, users, notices
import uvicorn
import os, asyncio

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

def get_or_create_event_loop():
    try:
        return asyncio.get_event_loop()
    except RuntimeError as ex:
        if "There is no current event loop in thread" in str(ex):
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            return loop
        else:
            raise

if __name__ == "__main__":
    loop = get_or_create_event_loop()
    loop.run_until_complete(uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT"))))