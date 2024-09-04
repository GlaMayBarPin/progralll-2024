from urllib import parse
from http.server import HTTPServer, SimpleHTTPRequestHandler

class ServidorBasico(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write("Hola Mundo".encode())

server = HTTPServer(('Localhost',3000), ServidorBasico)
server.serve_forever()
print("servidor ejecutado en el puerto 3000")