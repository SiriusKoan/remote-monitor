import os, subprocess
from monitor import google

# check ping
if subprocess.call(["which", "ping"], stdout=open(os.devnull, "w"), stderr=open(os.devnull, "w")):
    print("\033[33mCommand 'ping' does not exist, 'ping' test may fail.\033[39m")
# check nmap
if subprocess.call(["which", "nmap"], stdout=open(os.devnull, "w"), stderr=open(os.devnull, "w")):
    print("\033[33mCommand 'nmap' does not exist, 'nmap' test may fail.\033[39m")


# google is example host, please replace the host with yours
google.start()
