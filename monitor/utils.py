class Host:
    def __init__(
        self, ip_addr=None, domain=None, mac=None, hostname=None, monitoring_func=[]
    ) -> None:
        self.ip_addr = ip_addr
        self.domain = domain
        self.mac = mac
        self.hostname = hostname
        self.monitoring_func = monitoring_func


class MonitoringFunc:
    def __init__(self, name, func, interval=1) -> None:
        self.name = name
        self.func = func
        self.interval = interval

    def send_failure(self):
        pass

    def send_success(self):
        pass

    def send_recover(self):
        pass
