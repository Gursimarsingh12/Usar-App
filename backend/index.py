from http.server import BaseHTTPRequestHandler
from fastapi.middleware.wsgi import WSGIMiddleware
from main import app as fastapi_app

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        from io import BytesIO
        from urllib.parse import urlparse, parse_qs
        from wsgiref.simple_server import make_server

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

        fastapi_app = WSGIMiddleware(fastapi_app)
        result = fastapi_app(environ, start_response)
        for data in result:
            self.wfile.write(data)
        return
