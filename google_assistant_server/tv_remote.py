#!/usr/bin/env python
from subprocess import call

class tv_remote:
    def process_request(self, cmd):
        print "process cmd: " + cmd
        if cmd == "switch_TV":
            print "turning on/off TV"
            cmd_arg=["irsend", "SEND_ONCE", "lg_tv_remote", "KEY_POWER"]
            call(cmd_arg)
            return
        if cmd == "volume_up":
            print "increasing the volume"
            cmd_arg=["irsend", "SEND_ONCE", "lg_tv_remote", "KEY_VOLUMEUP"]
            call(cmd_arg)
            call(cmd_arg)
            call(cmd_arg)
            call(cmd_arg)
            call(cmd_arg)
            return
        if cmd == "volume_down":
            print "decreasing the volume"
            cmd_arg=["irsend", "SEND_ONCE", "lg_tv_remote", "KEY_VOLUMEDOWN"]
            call(cmd_arg)
            call(cmd_arg)
            call(cmd_arg)
            call(cmd_arg)
            call(cmd_arg)
            return
