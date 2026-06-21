import os
import platform
import socket
import getpass

print("====Linux System Monitor====")


print("Hostname:",socket.gethostname())
print("User:",getpass.getuser())
print("Operating System:", platform.system())
print("OS Version:", platform.release())
print("Python Version:",platform.python_version())

print("\n====Memory====")
os.system("free -h")

print("\n====Disk====")
os.system("df -h /")

print("\n====Uptime====")
os.system("uptime")

