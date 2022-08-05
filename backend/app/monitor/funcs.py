import os
import subprocess
import requests
from .utils import Netcat, Base

# bool functions
class Ping(Base):
    def __init__(self, interval, ops="-c 1"):
        self.__name__ = "ping"
        self.interval = interval
        self.ops = ops

    def job(self, host):
        res = subprocess.call(
            ["ping", *self.ops.split(), host],
            stdout=open(os.devnull, "w"),
            stderr=open(os.devnull, "w"),
        )
        return True if res == 0 else False


class GeneralNC(Base):
    def __init__(self, interval, port, timeout=2):
        self.__name__ = f"nc: {port}"
        self.interval = interval
        self.port = port
        self.timeout = timeout

    def job(self, host):
        with Netcat(host, self.port, self.timeout) as nc:
            return nc.connect()


class CheckSSH(Base):
    def __init__(self, interval, timeout=2):
        self.__name__ = "check SSH"
        self.interval = interval
        self.timeout = timeout

    def job(self, host):
        with Netcat(host, 22, self.timeout) as nc:
            return nc.connect()


class CheckDNS(Base):
    def __init__(self, interval, timeout=2):
        self.__name__ = "check DNS"
        self.interval = interval
        self.timeout = timeout

    def job(self, host):
        with Netcat(host, 53, self.timeout) as nc:
            return nc.connect()


class CheckSMTP(Base):
    def __init__(self, interval, timeout=2):
        self.__name__ = "check SMTP"
        self.interval = interval
        self.timeout = timeout

    def job(self, host):
        with Netcat(host, 25, self.timeout) as nc:
            return nc.connect()


class CheckSMTPS(Base):
    def __init__(self, interval, timeout=2):
        self.__name__ = "check SMTPS"
        self.interval = interval
        self.timeout = timeout

    def job(self, host):
        with Netcat(host, 465, self.timeout) as nc:
            return nc.connect()


class CheckHTTP(Base):
    def __init__(self, interval, timeout=2):
        self.__name__ = "check HTTP"
        self.interval = interval
        self.timeout = timeout

    def job(self, host):
        with Netcat(host, 80, self.timeout) as nc:
            return nc.connect()


class CheckHTTPS(Base):
    def __init__(self, interval, timeout=2):
        self.__name__ = "check HTTPS"
        self.interval = interval
        self.timeout = timeout

    def job(self, host):
        with Netcat(host, 443, self.timeout) as nc:
            return nc.connect()


class CheckIMAP(Base):
    def __init__(self, interval, timeout=2):
        self.__name__ = "check IMAP"
        self.interval = interval
        self.timeout = timeout

    def job(self, host):
        with Netcat(host, 143, self.timeout) as nc:
            return nc.connect()


class CheckIMAPS(Base):
    def __init__(self, interval, timeout=2):
        self.__name__ = "check IMAPS"
        self.interval = interval
        self.timeout = timeout

    def job(self, host):
        with Netcat(host, 993, self.timeout) as nc:
            return nc.connect()


class CheckPOP3(Base):
    def __init__(self, interval, timeout=2):
        self.__name__ = "check POP3"
        self.interval = interval
        self.timeout = timeout

    def job(self, host):
        with Netcat(host, 110, self.timeout) as nc:
            return nc.connect()


class CheckPOP3S(Base):
    def __init__(self, interval, timeout=2):
        self.__name__ = "check POP3S"
        self.interval = interval
        self.timeout = timeout

    def job(self, host):
        with Netcat(host, 995, self.timeout) as nc:
            return nc.connect()


class CheckWebsite(Base):
    def __init__(self, interval, hostname=None, schema="http", port=None):
        self.__name__ = f"check website"
        self.interval = interval
        self.hostname = hostname
        self.schema = schema
        self.port = port

    def job(self, host):
        if not self.hostname:
            self.hostname = host
        else:
            self.__name__ = f"check website with hostname {self.hostname}"
        if self.port:
            url = f"{self.schema}://{host}:{self.port}"
        else:
            url = f"{self.schema}://{host}"
        r = requests.get(url, headers={"Host": self.hostname}, verify=False)
        if str(r.status_code).startswith("2") or str(r.status_code).startswith("3"):
            # 2xx and 3xx are both okay
            return True
        else:
            return False


# text functions
class Nmap(Base):
    def __init__(self, interval, ops="-Pn"):
        self.__name__ = "nmap"
        self.interval = interval
        self.ops = ops

    def job(self, host):
        with subprocess.Popen(
            f"nmap {self.ops} {host}", stdout=subprocess.PIPE, shell=True
        ) as process:
            output = process.communicate()[0].decode("utf-8")
            return output


class DNSRecord(Base):
    def __init__(self, interval, search, record_type="A", short=True):
        self.__name__ = f"DNS search {search} {record_type}"
        self.interval = interval
        self.search = search
        self.record_type = record_type
        self.short = short

    def job(self, host):
        if self.short:
            command = f"dig {self.record_type} {self.search} @{host} +short"
        else:
            command = f"dig {self.record_type} {self.search} @{host}"
            with subprocess.Popen(
                command,
                stdout=subprocess.PIPE,
                shell=True,
            ) as process:
                output = process.communicate()[0].decode("utf-8")
                return output


class SSHCommand(Base):
    def __init__(self, interval, command, username, key="id_rsa", name=None):
        # the command may be too long or contain troublesome char (like \t), so you can use name to name it
        self.__name__ = f"send command: {name if name else command}"
        self.interval = interval
        self.command = command
        self.username = username
        self.key = key

    def job(self, host):
        with subprocess.Popen(
            f"ssh -o StrictHostKeyChecking=no -i /app/keys/{self.key} {self.username}@{host} '{self.command}'",
            stdout=subprocess.PIPE,
            shell=True,
        ) as process:
            output = process.communicate()[0].decode("utf-8")
            return output
