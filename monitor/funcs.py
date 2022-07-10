import socket
import os
import subprocess
from . import config
from .log import logger


class Netcat:
    """Python 'netcat like' module"""

    """ The snippet is from https://gist.github.com/leonjza/f35a7252babdf77c8421 """

    def __init__(self, ip, port, timeout):
        self.buff = ""
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.settimeout(timeout)
        self.ip = ip
        self.port = port

    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        self.socket.close()

    def connect(self):
        try:
            self.socket.connect((self.ip, self.port))
            return True
        except socket.timeout:
            return False

    def read(self, length=1024):
        return self.socket.recv(length)

    def write(self, data):
        self.socket.send(data)


def ping(host, args="-c 1"):
    res = subprocess.call(
        ["ping", *args.split(), host.ip_addr],
        stdout=open(os.devnull, "w"),
        stderr=open(os.devnull, "w"),
    )
    if res:
        return False
    else:
        return True


def nmap(host, args="-Pn"):
    with subprocess.Popen(
        f"nmap {args} {host.ip_addr}", stdout=subprocess.PIPE, shell=True
    ) as process:
        output = process.communicate()[0].decode("utf-8")
        return output


def smtp(host, timeout=3):
    with Netcat(host.ip_addr, 25, timeout) as nc:
        if nc.connect():
            return True
        else:
            return False


def smtps(host, timeout=3):
    with Netcat(host.ip_addr, 465, timeout) as nc:
        if nc.connect():
            return True
        else:
            return False
