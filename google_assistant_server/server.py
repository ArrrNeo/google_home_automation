#!/usr/bin/env python
import os
import logging
from tv_remote import tv_remote
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer

dir_path = os.path.dirname(os.path.realpath(__file__))

# initialize log class
log_file_name = dir_path + '/logs.txt'
logging.basicConfig(filename=log_file_name, level=logging.DEBUG)

# initialize remote class
tv = tv_remote(logging)

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        logging.debug("get request recieved")
        logging.debug(self.path[1:])
        self._set_headers()
        #self.wfile.write("temperature is 201 F")
        self.wfile.write("<html><body><h1>hi!</h1></body></html>")

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        logging.debug("handling POST request")
        logging.debug(post_data)
        tv.process_request(post_data)

def run(server_class=HTTPServer, handler_class=S, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.debug('Starting httpd on port ' + str(port))
    httpd.serve_forever()

run(port=8080)
