#!/usr/bin/env python
from tv_remote import tv_remote
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer

class S(BaseHTTPRequestHandler):
    def do_POST(self):
        tv = tv_remote()
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        print "handling POST request"
        print post_data
        tv.process_request(post_data)

def run(server_class=HTTPServer, handler_class=S, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Starting httpd on port ' + str(port)
    httpd.serve_forever()

run(port=8080)
