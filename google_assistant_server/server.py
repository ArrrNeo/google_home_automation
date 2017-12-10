#!/usr/bin/env python
import os
import logging
import SocketServer
from subprocess import call
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

dir_path = os.path.dirname(os.path.realpath(__file__))

# logging stuff
fout = open(dir_path + '/out.txt', 'w')
ferr = open(dir_path + '/err.txt', 'w')
log_file_name = dir_path + '/logs.txt'
logging.basicConfig(filename=log_file_name, level=logging.DEBUG)

class tv_remote:
    def __init__(self):
        return

    def process_request(self, cmd):
        logging.debug("process cmd: " + cmd)
        if cmd == "switch_TV":
            logging.debug("turning on/off TV")
            fpath = dir_path + "/power.sh"
            call([fpath], stdout=fout, stderr=ferr)
            return
        if cmd == "volume_up":
            logging.debug("increasing the volume")
            fpath = dir_path + "/volumeup.sh"
            call([fpath], stdout=fout, stderr=ferr)
            return
        if cmd == "volume_down":
            logging.debug("decreasing the volume")
            fpath = dir_path + "/volumedown.sh"
            call([fpath], stdout=fout, stderr=ferr)
            return
        if cmd == "hdmi_1":
            logging.debug("switching to hdmi_1")
            fpath = dir_path + "/hdmi1.sh"
            call([fpath], stdout=fout, stderr=ferr)
            return
        if cmd == "hdmi_2":
            logging.debug("switching to hdmi_2")
            fpath = dir_path + "/hdmi2.sh"
            call([fpath], stdout=fout, stderr=ferr)
            return

# initialize remote class
tv = tv_remote()

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
