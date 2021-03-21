import http.server
import socketserver

import route

host = 'localhost'
port = 8000

@route('/')
def home():
    print('hello word')



http = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer((host, port), http) as httpd:
    print(f'serving at port : {port}')
    httpd.serve_forever()