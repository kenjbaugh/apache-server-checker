#!/usr/bin/python

import subprocess

cmd1 = "systemctl status httpd"
cmd2 = "systemctl start httpd"

success = subprocess.call(cmd1, shell=True)
start = subprocess.call(cmd2, shell=True)

if success == True:
        print("Web Server is running properly", success)
else:
        print("Server not running. Attempting to start service", start)
