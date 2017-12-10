#!/usr/bin/env python
import os
from subprocess import call

fout = open("out.txt", "w")
ferr = open("err.txt", "w")


class tv_remote:
    def __init__(self, log_class):
        self.dir_path = os.path.dirname(os.path.realpath(__file__))
        self.logging = log_class
        return

    def process_request(self, cmd):
        self.logging.debug("process cmd: " + cmd)
        if cmd == "switch_TV":
            self.logging.debug("turning on/off TV")
            fpath = self.dir_path + "/power.sh"
            call([fpath], stdout=fout, stderr=ferr)
            return
        if cmd == "volume_up":
            self.logging.debug("increasing the volume")
            fpath = self.dir_path + "/volumeup.sh"
            call([fpath], stdout=fout, stderr=ferr)
            return
        if cmd == "volume_down":
            self.logging.debug("decreasing the volume")
            fpath = self.dir_path + "/volumedown.sh"
            call([fpath], stdout=fout, stderr=ferr)
            return
        if cmd == "hdmi_1":
            self.logging.debug("switching to hdmi_1")
            fpath = self.dir_path + "/hdmi1.sh"
            call([fpath], stdout=fout, stderr=ferr)
            return
        if cmd == "hdmi_2":
            self.logging.debug("switching to hdmi_2")
            fpath = self.dir_path + "/hdmi2.sh"
            call([fpath], stdout=fout, stderr=ferr)
            return
