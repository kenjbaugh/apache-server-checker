#!/usr/bin/python

import subprocess

server_version = "httpd -v"

version_status = subprocess.call(server_version, shell=True)
print(version_status)


server_status = "systemctl status httpd"
run_service = "systemctl start httpd"

success = subprocess.call(server_status, shell=True)
start = subprocess.call(run_service, shell=True)

if success == True:
	print("Web Server is running properly", success)

else:
	if success == False:
		print("Server not currently running. Attempting to start httpd service", start)
