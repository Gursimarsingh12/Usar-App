from fastapi import FastAPI
from routers import subjects, users, notices
from dependencies import connect_to_database, close_database_connection

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
