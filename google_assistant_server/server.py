#!/usr/bin/env python
import logging
from tv_remote import tv_remote
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer

# initialize log class
log_file_name='/home/pi/google_home_automation/google_assistant_server/logs.txt'
logging.basicConfig(filename=log_file_name, level=logging.DEBUG)

# initialize remote class
tv = tv_remote(logging)

class S(BaseHTTPRequestHandler):
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
