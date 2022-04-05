import subprocess, os
import time
from .utils import MonitoringFunc, ping, nmap, smtp, smtps
from .log import logger

# There are some basic tests
class PingTest(MonitoringFunc):
    def __init__(self, name, func, interval=1) -> None:
        super().__init__(name, func, interval)
        self.failure_msg = "Ping Fail"
        self.success_msg = "Ping Success"
        self.recover_msg = "Ping Recover"

    def check_deps(self):
        super().check_deps()
        if subprocess.call(
            ["which", "ping"],
            stdout=open(os.devnull, "w"),
            stderr=open(os.devnull, "w"),
        ):
            logger.warning("Command 'ping' does not exist, 'ping' test may fail.")

class NmapTest(MonitoringFunc):
    def __init__(self, name, func, interval=1) -> None:
        super().__init__(name, func, interval)
        self.failure_msg = ""
        self.success_msg = ""
        self.recover_msg = ""

    def check_deps(self):
        super().check_deps()
        if subprocess.call(["which", "nmap"], stdout=open(os.devnull, "w"), stderr=open(os.devnull, "w")):
            logger.warning("Command 'nmap' does not exist, 'nmap' test may fail.")

    def job(self, host):
        try:
            while True:
                res = self.func(host)
                if res:
                    # the level is set to 'warning' because telegram and email can only receive messages with warning or above log level
                    self.send(res, "warning")
                else:
                    self.send_failure(res)
                time.sleep(self.interval)
        except:
            pass

class SMTPTest(MonitoringFunc):
    def __init__(self, name, func, interval=1) -> None:
        super().__init__(name, func, interval)
        self.failure_msg = "SMTP Fail"
        self.success_msg = "SMTP Success"
        self.recover_msg = "SMTP Recover"

    def check_deps(self):
        super().check_deps()

class SMTPSTest(MonitoringFunc):
    def __init__(self, name, func, interval=1) -> None:
        super().__init__(name, func, interval)
        self.failure_msg = "SMTPS Fail"
        self.success_msg = "SMTPS Success"
        self.recover_msg = "SMTPS Recover"

    def check_deps(self):
        super().check_deps()


ping_func = PingTest("ping", ping, interval=120)
nmap_func = NmapTest("nmap", nmap, interval=7200)
smtp_func = SMTPTest("smtp", smtp, interval=300)
smtps_func = SMTPSTest("smtps", smtps, interval=300)
