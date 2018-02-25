#!/usr/local/bin/python
# coding: utf-8

import requests
import http.server
import socketserver
from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, unquote, parse_qs

def start(port, callback):
    def handler(*args):
        CallbackServer(callback, *args)
    server = socketserver.TCPServer(('', int(port)), handler)
    server.serve_forever()

class CallbackServer(BaseHTTPRequestHandler):
    def __init__(self, callback, *args):
        self.callback = callback
        BaseHTTPRequestHandler.__init__(self, *args)

    def do_GET(self):
        parsed_path = urlparse(self.path)
        query = parse_qs(parsed_path.query)

        self.send_response(200)
        self.end_headers()

        result = self.callback(query)
        self.wfile.write(result.encode('utf-8'))

        return
