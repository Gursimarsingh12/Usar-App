from fastapi import FastAPI, Request
from routers import subjects, users, notices
import uvicorn
import os
import asyncio

app = FastAPI()

app.include_router(notices.router)
app.include_router(users.router)
app.include_router(subjects.router)

@app.middleware("http")
async def event_loop_middleware(request: Request, call_next):
    loop = asyncio.get_event_loop()
    try:
        response = await call_next(request)
    finally:
        if loop.is_closed():
            asyncio.set_event_loop(asyncio.new_event_loop())
    return response

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT")))