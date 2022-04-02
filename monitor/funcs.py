import subprocess, os
import time
from .utils import NotifyEmail, NotifyTelegram, ping, nmap

# There are some basic tests
class PingTest(NotifyTelegram):
    def __init__(self, name, func, interval=1) -> None:
        super().__init__(name, func, interval)
        self.failure_msg = "Ping Failure"
        self.success_msg = "Ping Success"
        self.recover_msg = "Ping Recover"

    def check_deps(self):
        super().check_deps()
        if subprocess.call(
            ["which", "ping"],
            stdout=open(os.devnull, "w"),
            stderr=open(os.devnull, "w"),
        ):
            print(
                self.colorize(
                    "warning",
                    "[Warning] Command 'ping' does not exist, 'ping' test may fail.",
                )
            )

class NmapTest(NotifyTelegram):
    def __init__(self, name, func, interval=1) -> None:
        super().__init__(name, func, interval)

    def check_deps(self):
        super().check_deps()
        if subprocess.call(["which", "nmap"], stdout=open(os.devnull, "w"), stderr=open(os.devnull, "w")):
            print(self.colorize("warning", "[Warning] Command 'nmap' does not exist, 'nmap' test may fail."))

    def job(self, host):
        while True:
            res = self.func(host)
            if res:
                self.send_success(res)
            else:
                self.send_failure(res)
            time.sleep(self.interval)


ping_func = PingTest("ping", ping, interval=10)
nmap_func = NmapTest("nmap", nmap, interval=1000)
