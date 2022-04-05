import abc
import socket
import os
import subprocess
import smtplib
import time
import threading
import telebot
from . import config
from .log import logger


class Host(abc.ABC):
    def __init__(
        self, ip_addr, domain=None, mac=None, hostname=None, monitoring_func=[]
    ) -> None:
        self.ip_addr = ip_addr
        self.domain = domain
        self.mac = mac
        self.hostname = hostname
        self.monitoring_func = monitoring_func

    def start(self):
        for func in self.monitoring_func:
            func.set_host(self)
            func.start()


class MonitoringFunc(abc.ABC):
    def __init__(self, name, func, interval=1) -> None:
        self.check_deps()
        self.name = name
        self.func = func
        self.interval = interval
        self.thread = None

    def set_host(self, host):
        self.host = host
        self.failure_msg = f"Host: {self.host.ip_addr}\n" + self.failure_msg
        self.success_msg = f"Host: {self.host.ip_addr}\n" + self.success_msg
        self.recover_msg = f"Host: {self.host.ip_addr}\n" + self.recover_msg

    def job(self, host):
        try:
            fail = False
            while True:
                res = self.func(host)
                if not res:
                    self.send_failure()
                    fail = True
                else:
                    if fail:
                        self.send_recover()
                        fail = False
                time.sleep(self.interval)
        except Exception as e:
            logger.error("Exception in thread:", exc_info=True)

    @staticmethod
    def colorize(category, msg):
        color_table = {
            "warning": "33m",
            "error": "31m",
            "info": "34m",
        }
        return "\033[" + color_table[category] + msg + "\033[39m"

    def check_deps(self):
        pass

    def start(self):
        self.thread = threading.Thread(target=self.job, args=(self.host,))
        self.thread.start()

    def send(self, msg, level):
        level = level.lower()
        getattr(logger, level)(msg)

    def send_failure(self, msg=None):
        if msg:
            logger.warning(msg)
        else:
            logger.warning(self.failure_msg)

    def send_success(self, msg=None):
        if msg:
            logger.info(msg)
        else:
            logger.info(self.success_msg)

    def send_recover(self, msg=None):
        if msg:
            logger.warning(msg)
        else:
            logger.warning(self.recover_msg)

class Netcat:
    """ Python 'netcat like' module """
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
    res = subprocess.call(["ping", *args.split(), host.ip_addr], stdout=open(os.devnull, "w"), stderr=open(os.devnull, "w"))
    if res:
        return False
    else:
        return True

def nmap(host, args="-Pn"):
    with subprocess.Popen(f"nmap {args} {host.ip_addr}", stdout=subprocess.PIPE, shell=True) as process:
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

