import os
from time import sleep
import subprocess
from ..redis import set_record
from .utils import Netcat


def ping(host, interval, ops="-c 1"):
    while True:
        res = subprocess.call(
            ["ping", *ops.split(), host],
            stdout=open(os.devnull, "w"),
            stderr=open(os.devnull, "w"),
        )
        if res:
            set_record(host, "ping", "false")
        else:
            set_record(host, "ping", "true")
        sleep(interval)


def nmap(host, interval, ops="-Pn"):
    while True:
        with subprocess.Popen(
            f"nmap {ops} {host}", stdout=subprocess.PIPE, shell=True
        ) as process:
            output = process.communicate()[0].decode("utf-8")
            set_record(host, "nmap", output)
        sleep(interval)


def smtp(host, interval, timeout=2):
    while True:
        with Netcat(host, 25, timeout) as nc:
            if nc.connect():
                set_record(host, "smtp", "true")
            else:
                set_record(host, "smtp", "false")
        sleep(interval)


def smtps(host, interval, timeout=2):
    while True:
        with Netcat(host, 465, timeout) as nc:
            if nc.connect():
                set_record(host, "smtps", "true")
            else:
                set_record(host, "smtps", "false")
        sleep(interval)
