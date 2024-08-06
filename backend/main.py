from fastapi import FastAPI
from routers import subjects, users, notices
from dependencies import connect_to_database, close_database_connection
import uvicorn
from http.server import BaseHTTPRequestHandler
import os

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

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        from io import BytesIO
        from urllib.parse import urlparse, parse_qs
        import asyncio

        async def app(scope, receive, send):
            if scope['type'] == 'http':
                headers = [(k.encode(), v.encode()) for k, v in self.headers.items()]
                body = await receive()

                send({
                    'type': 'http.response.start',
                    'status': 200,
                    'headers': headers
                })
                send({
                    'type': 'http.response.body',
                    'body': body
                })

        uvicorn.run(app, host='0.0.0.0', port=int(os.getenv("PORT", 8000)))

        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write('Hello, world!'.encode('utf-8'))
        return
