import http.server
import socketserver
import urllib.parse

PORT = 8000

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/login':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            decoded_data = urllib.parse.parse_qs(post_data.decode('utf-8'))

            username = decoded_data.get('username', [None])[0]
            password = decoded_data.get('clave', [None])[0]

            print(f'Username: {username}, clave: {clave}')

            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'Ingreso exitoso')

        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Not Found')

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Server started at http://localhost:{PORT}")
    httpd.serve_forever()