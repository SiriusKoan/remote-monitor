import subprocess, os
from .utils import NotifyEmail, NotifyTelegram, ping


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


ping_func = PingTest("ping", ping, interval=10)
