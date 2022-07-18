import threading
from time import sleep
from backend.monitor.hosts import hosts

for host in hosts:
    addr = host["addr"]
    for f in host["bool_functions"] + host["text_functions"]:
        t = threading.Thread(target=f[0], args=[addr, *f[1]])
        t.setDaemon(True)
        t.start()

sleep(10000)
