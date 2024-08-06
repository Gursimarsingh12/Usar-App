from fastapi import FastAPI
from routers import subjects, users, notices
from dependencies import connect_to_database, close_database_connection
from http.server import BaseHTTPRequestHandler
from fastapi import FastAPI
from asgiref.wsgi import WsgiToAsgi

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

# Convert the FastAPI app to a WSGI-compatible app
fastapi_app = WsgiToAsgi(app)

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        from io import BytesIO
        from urllib.parse import urlparse, parse_qs

        environ = {
            'REQUEST_METHOD': self.command,
            'PATH_INFO': self.path,
            'SERVER_NAME': self.server.server_address[0],
            'SERVER_PORT': str(self.server.server_address[1]),
            'wsgi.input': BytesIO(),
            'wsgi.errors': BytesIO(),
            'wsgi.version': (1, 0),
            'wsgi.url_scheme': 'http',
            'wsgi.multithread': False,
            'wsgi.multiprocess': False,
            'wsgi.run_once': False,
        }

        def start_response(status, headers):
            self.send_response(int(status.split(' ')[0]))
            for header in headers:
                self.send_header(*header)
            self.end_headers()

        result = fastapi_app(environ, start_response)
        for data in result:
            self.wfile.write(data)
        return

