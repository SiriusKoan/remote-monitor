import threading
from .hosts import hosts

def start_monitor():
    for host in hosts:
        for f in host["bool_functions"] + host["text_functions"]:
            t = threading.Thread(target=f[0], args=(host["addr"], *f[1]))
            t.setDaemon(True)
            t.start()
