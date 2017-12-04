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
            cmd_arg=["./power.sh"]
            call(cmd_arg)
            return
        if cmd == "volume_up":
            self.logging.debug("increasing the volume")
            cmd_arg=["./volumeup.sh"]
            call(cmd_arg)
            return
        if cmd == "volume_down":
            self.logging.debug("decreasing the volume")
            cmd_arg=["./volumedown.sh"]
            call(cmd_arg)
            return
        if cmd == "hdmi_1":
            self.logging.debug("switching to hdmi_1")
            cmd_arg=["./hdmi1.sh"]
            call(cmd_arg)
            return
        if cmd == "hdmi_2":
            self.logging.debug("switching to hdmi_2")
            cmd_arg=["./hdmi2.sh"]
            call(cmd_arg)
            return
