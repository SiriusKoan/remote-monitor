import os
from time import sleep
import subprocess
from .utils import Netcat


def ping(host, interval, ops="-c 1"):
    while True:
        res = subprocess.call(
            ["ping", *ops.split(), host.ip_addr],
            stdout=open(os.devnull, "w"),
            stderr=open(os.devnull, "w"),
        )
        if res:
            pass
            # return False
        else:
            pass
            # return True
        sleep(interval)


def nmap(host, interval, ops="-Pn"):
    while True:
        with subprocess.Popen(
            f"nmap {ops} {host.ip_addr}", stdout=subprocess.PIPE, shell=True
        ) as process:
            output = process.communicate()[0].decode("utf-8")
            # return output
        sleep(interval)


def smtp(host, interval, timeout=2):
    while True:
        with Netcat(host.ip_addr, 25, timeout) as nc:
            if nc.connect():
                pass
                # return True
            else:
                pass
                # return False
        sleep(interval)


def smtps(host, interval, timeout=2):
    while True:
        with Netcat(host.ip_addr, 465, timeout) as nc:
            if nc.connect():
                pass
                # return True
            else:
                pass
                # return False
        sleep(interval)
