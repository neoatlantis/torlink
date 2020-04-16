#!/usr/bin/env python3

"""Mailbox: a hidden service receiving pushed messages."""

from http.server import *
from threading import Thread


class LinkTerminalHandler(BaseHTTPRequestHandler):
    
    def __init__(self, request, client_address, server):
        BaseHTTPRequestHandler.__init__(self, request, client_address, server)
        print(client_address)

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"OK")




class LinkTerminalServer(HTTPServer):

    def __init__(self, server_address):
        HTTPServer.__init__(self, server_address, LinkTerminalHandler)
        
    def __enter__(self):
        self._thread = Thread(target=self.serve_forever, args=())
        self._thread.start()
        return self

    def __exit__(self, *args, **kvargs):
        self.shutdown()







