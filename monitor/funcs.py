from .utils import NotifyEmail, NotifyTelegram, ping


class PingTest(NotifyTelegram):
    def __init__(self, name, func, interval=1) -> None:
        super().__init__(name, func, interval)
        self.failure_msg = "Ping Failure"
        self.success_msg = "Ping Success"
        self.recover_msg = "Ping Recover"


ping_func = PingTest("ping", ping, interval=10)
