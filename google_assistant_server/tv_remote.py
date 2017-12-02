#!/usr/bin/env python
from subprocess import call

class tv_remote:
    def __init__(self, log_class):
        self.logging = log_class
        return

    def process_request(self, cmd):
        self.logging.debug("process cmd: " + cmd)
        if cmd == "switch_TV":
            self.logging.debug("turning on/off TV")
            cmd_arg=["irsend", "SEND_ONCE", "lg_tv_remote", "KEY_POWER"]
            call(cmd_arg)
            return
        if cmd == "volume_up":
            self.logging.debug("increasing the volume")
            cmd_arg=["irsend", "SEND_ONCE", "lg_tv_remote", "KEY_VOLUMEUP"]
            call(cmd_arg)
            call(cmd_arg)
            call(cmd_arg)
            call(cmd_arg)
            call(cmd_arg)
            return
        if cmd == "volume_down":
            self.logging.debug("decreasing the volume")
            cmd_arg=["irsend", "SEND_ONCE", "lg_tv_remote", "KEY_VOLUMEDOWN"]
            call(cmd_arg)
            call(cmd_arg)
            call(cmd_arg)
            call(cmd_arg)
            call(cmd_arg)
            return
        if cmd == "hdmi_1":
            self.logging.debug("switching to hdmi_1")
            cmd_arg=["irsend", "SEND_ONCE", "lg_tv_remote", "KEY_CYCLEWINDOWS"]
            call(cmd_arg)
            cmd_arg=["irsend", "SEND_ONCE", "lg_tv_remote", "KEY_LEFT"]
            call(cmd_arg)
            cmd_arg=["irsend", "SEND_ONCE", "lg_tv_remote", "KEY_OK"]
            call(cmd_arg)
            return
        if cmd == "hdmi_2":
            self.logging.debug("switching to hdmi_2")
            cmd_arg=["irsend", "SEND_ONCE", "lg_tv_remote", "KEY_CYCLEWINDOWS"]
            call(cmd_arg)
            cmd_arg=["irsend", "SEND_ONCE", "lg_tv_remote", "KEY_RIGHT"]
            call(cmd_arg)
            cmd_arg=["irsend", "SEND_ONCE", "lg_tv_remote", "KEY_OK"]
            call(cmd_arg)
            return
