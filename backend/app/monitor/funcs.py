import os
from time import sleep
import subprocess
import requests
from ..redis import set_record
from .utils import Netcat

# bool functions
class Ping:
    def __init__(self, interval, ops="-c 1"):
        self.__name__ = "ping"
        self.interval = interval
        self.ops = ops

    def __call__(self, host):
        self.host = host
        while True:
            res = subprocess.call(
                ["ping", *self.ops.split(), self.host],
                stdout=open(os.devnull, "w"),
                stderr=open(os.devnull, "w"),
            )
            if res:
                set_record(self.host, self.__name__, "false")
            else:
                set_record(self.host, self.__name__, "true")
            sleep(self.interval)


class GeneralNC:
    def __init__(self, interval, port, timeout=2):
        self.__name__ = f"nc: {port}"
        self.interval = interval
        self.port = port
        self.timeout = timeout

    def __call__(self, host):
        self.host = host
        while True:
            with Netcat(self.host, self.port, self.timeout) as nc:
                if nc.connect():
                    set_record(self.host, self.__name__, "true")
                else:
                    set_record(self.vhost, self.__name__, "false")
            sleep(self.interval)


class CheckSSH:
    def __init__(self, interval, timeout=2):
        self.__name__ = "check SSH"
        self.interval = interval
        self.timeout = timeout

    def __call__(self, host):
        self.host = host
        while True:
            with Netcat(self.host, 22, self.timeout) as nc:
                if nc.connect():
                    set_record(self.host, self.__name__, "true")
                else:
                    set_record(self.host, self.__name__, "false")
            sleep(self.interval)


class CheckDNS:
    def __init__(self, interval, timeout=2):
        self.__name__ = "check DNS"
        self.interval = interval
        self.timeout = timeout

    def __call__(self, host):
        self.host = host
        while True:
            with Netcat(self.host, 53, self.timeout) as nc:
                if nc.connect():
                    set_record(self.host, self.__name__, "true")
                else:
                    set_record(self.host, self.__name__, "false")
            sleep(self.interval)


class CheckSMTP:
    def __init__(self, interval, timeout=2):
        self.__name__ = "check SMTP"
        self.interval = interval
        self.timeout = timeout

    def __call__(self, host):
        self.host = host
        while True:
            with Netcat(self.host, 25, self.timeout) as nc:
                if nc.connect():
                    set_record(self.host, self.__name__, "true")
                else:
                    set_record(self.host, self.__name__, "false")
            sleep(self.interval)


class CheckSMTPS:
    def __init__(self, interval, timeout=2):
        self.__name__ = "check SMTPS"
        self.interval = interval
        self.timeout = timeout

    def __call__(self, host):
        self.host = host
        while True:
            with Netcat(self.host, 465, self.timeout) as nc:
                if nc.connect():
                    set_record(self.host, self.__name__, "true")
                else:
                    set_record(self.host, self.__name__, "false")
            sleep(self.interval)


class CheckHTTP:
    def __init__(self, interval, timeout=2):
        self.__name__ = "check HTTP"
        self.interval = interval
        self.timeout = timeout

    def __call__(self, host):
        self.host = host
        while True:
            with Netcat(self.host, 80, self.timeout) as nc:
                if nc.connect():
                    set_record(self.host, self.__name__, "true")
                else:
                    set_record(self.host, self.__name__, "false")
            sleep(self.interval)


class CheckHTTPS:
    def __init__(self, interval, timeout=2):
        self.__name__ = "check HTTPS"
        self.interval = interval
        self.timeout = timeout

    def __call__(self, host):
        self.host = host
        while True:
            with Netcat(self.host, 443, self.timeout) as nc:
                if nc.connect():
                    set_record(self.host, self.__name__, "true")
                else:
                    set_record(self.host, self.__name__, "false")


class CheckIMAP:
    def __init__(self, interval, timeout=2):
        self.__name__ = "check IMAP"
        self.interval = interval
        self.timeout = timeout

    def __call__(self, host):
        self.host = host
        while True:
            with Netcat(self.host, 143, self.timeout) as nc:
                if nc.connect():
                    set_record(self.host, self.__name__, "true")
                else:
                    set_record(self.host, self.__name__, "false")


class CheckIMAPS:
    def __init__(self, interval, timeout=2):
        self.__name__ = "check IMAPS"
        self.interval = interval
        self.timeout = timeout

    def __call__(self, host):
        self.host = host
        while True:
            with Netcat(self.host, 993, self.timeout) as nc:
                if nc.connect():
                    set_record(self.host, self.__name__, "true")
                else:
                    set_record(self.host, self.__name__, "false")


class CheckPOP3:
    def __init__(self, interval, timeout=2):
        self.__name__ = "check POP3"
        self.interval = interval
        self.timeout = timeout

    def __call__(self, host):
        self.host = host
        while True:
            with Netcat(self.host, 110, self.timeout) as nc:
                if nc.connect():
                    set_record(self.host, self.__name__, "true")
                else:
                    set_record(self.host, self.__name__, "false")


class CheckPOP3S:
    def __init__(self, interval, timeout=2):
        self.__name__ = "check POP3S"
        self.interval = interval
        self.timeout = timeout

    def __call__(self, host):
        self.host = host
        while True:
            with Netcat(self.host, 995, self.timeout) as nc:
                if nc.connect():
                    set_record(self.host, self.__name__, "true")
                else:
                    set_record(self.host, self.__name__, "false")


class CheckWebsite:
    def __init__(self, interval, hostname=None, schema="http", port=None):
        self.__name__ = f"check website with hostname {hostname}"
        self.interval = interval
        self.hostname = hostname
        self.schema = schema
        self.port = port

    def __call__(self, host):
        self.host = host
        if not self.hostname:
            self.hostname = self.host
        self.__name__ = f"check website with hostname {self.hostname}"
        if self.port:
            url = f"{self.schema}://{self.host}:{self.port}"
        else:
            url = f"{self.schema}://{self.host}"
        while True:
            r = requests.get(url, headers={"Host": self.hostname}, verify=False)
            if r.status_code == 200:
                set_record(self.host, self.__name__, "true")
            else:
                set_record(self.host, self.__name__, "false")
            sleep(self.interval)


# text functions
class Nmap:
    def __init__(self, interval, ops="-Pn"):
        self.__name__ = "nmap"
        self.interval = interval
        self.ops = ops

    def __call__(self, host):
        self.host = host
        while True:
            with subprocess.Popen(
                f"nmap {self.ops} {self.host}", stdout=subprocess.PIPE, shell=True
            ) as process:
                output = process.communicate()[0].decode("utf-8")
                set_record(self.host, self.__name__, output)
            sleep(self.interval)


class DNSRecord:
    def __init__(self, interval, search, record_type="A", short=True):
        self.__name__ = f"DNS search {search} {record_type}"
        self.interval = interval
        self.search = search
        self.record_type = record_type
        self.short = short

    def __call__(self, host):
        self.host = host
        while True:
            if self.short:
                command = f"dig {self.record_type} {self.search} @{self.host} +short"
            else:
                command = f"dig {self.record_type} {self.search} @{self.host}"
            with subprocess.Popen(
                command,
                stdout=subprocess.PIPE,
                shell=True,
            ) as process:
                output = process.communicate()[0].decode("utf-8")
                set_record(self.host, self.__name__, output)
            sleep(self.interval)


class SSHCommand:
    def __init__(self, interval, command, username, key="id_rsa", name=None):
        # the command may be too long or contain troublesome char (like \t), so you can use name to name it
        self.__name__ = f"send command: {name if name else command}"
        self.interval = interval
        self.command = command
        self.username = username
        self.key = key

    def __call__(self, host):
        self.host = host
        while True:
            with subprocess.Popen(
                f"ssh -o StrictHostKeyChecking=no -i /app/keys/{self.key} {self.username}@{self.host} '{self.command}'",
                stdout=subprocess.PIPE,
                shell=True,
            ) as process:
                output = process.communicate()[0].decode("utf-8")
                set_record(self.host, self.__name__, output)
            sleep(self.interval)
