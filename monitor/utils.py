import abc
import os
import subprocess
import smtplib
import time
import threading
import telebot
from . import config


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
        self.failure_msg = f"{self.host.ip_addr} Failure"
        self.success_msg = f"{self.host.ip_addr} Success"
        self.recover_msg = f"{self.host.ip_addr} Recover"

    def job(self, host):
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

    @staticmethod
    def colorize(category, msg):
        color_table = {
            "warning": "33m",
            "error": "31m",
            "info": "34m",
        }
        return "\033[" + color_table[category] + msg + "\033[39m"

    def check_deps(self):
        return NotImplemented

    def start(self):
        self.thread = threading.Thread(target=self.job, args=(self.host,))
        self.thread.start()

    def send_failure(self, msg=None):
        return NotImplemented

    def send_success(self, msg=None):
        return NotImplemented

    def send_recover(self, msg=None):
        return NotImplemented


class NotifyTelegram(MonitoringFunc):
    def __init__(self, name, func, interval=1) -> None:
        super().__init__(name, func, interval)
        self.bot = telebot.TeleBot(config.TELEGRAM_TOKEN)
        self.chat_id = config.TELEGRAM_CHAT_ID

    def check_deps(self):
        if not config.TELEGRAM_TOKEN:
            print(
                self.colorize(
                    "warning",
                    "[Warning] Environmental variable 'TELEGRAM_TOKEN' is not set, telegram notification may not work.",
                )
            )
        if not config.TELEGRAM_CHAT_ID:
            print(
                self.colorize(
                    "warning",
                    "[Warning] Environmental variable 'TELEGRAM_CHAT_ID' is not set, telegram notification may not work.",
                )
            )

    def send_failure(self, msg=None):
        if msg:
            self.bot.send_message(self.chat_id, msg)
        else:
            self.bot.send_message(self.chat_id, self.failure_msg)

    def send_success(self, msg=None):
        if msg:
            self.bot.send_message(self.chat_id, msg)
        else:
            self.bot.send_message(self.chat_id, self.success_msg)

    def send_recover(self):
        if msg:
            self.bot.send_message(self.chat_id, msg)
        else:
            self.bot.send_message(self.chat_id, self.recover_msg)


class NotifyEmail(MonitoringFunc):
    def __init__(self, name, func, interval=1) -> None:
        super().__init__(name, func, interval)
        self.host = config.EMAIL_HOST
        self.port = config.EMAIL_PORT
        self.username = config.EMAIL_HOST_USER
        self.password = config.EMAIL_HOST_PASSWORD

    def check_deps(self):
        if not config.EMAIL_HOST:
            print(
                colorize(
                    "[Warning] Environmental variable 'EMAIL_HOST' is not set, email notification may not work."
                )
            )
        if not config.EMAIL_PORT:
            print(
                colorize(
                    "[Warning] Environmental variable 'EMAIL_HOST_PORT' is not set, email notification may not work."
                )
            )
        if not config.EMAIL_HOST_USER:
            print(
                colorize(
                    "[Warning] Environmental variable 'EMAIL_HOST_USER' is not set, email notification may not work."
                )
            )
        if not config.EMAIL_HOST_PASSWORD:
            print(
                colorize(
                    "[Warning] Environmental variable 'EMAIL_HOST_PASSWORD' is not set, email notification may not work."
                )
            )
        if not config.EMAIL_ADMIN:
            print(
                colorize(
                    "[Warning] Environmental variable 'EMAIL_ADMIN' is not set, email notification may not work."
                )
            )

    def connect_to_server(self):
        server = smtplib.SMTP(self.host, self.port)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(self.username, self.password)
        return server

    def compose_msg(self, subject, msg):
        return f"Subject: {subject}\n\n{msg}"

    def send_failure(self):
        with self.connect_to_server() as server:
            server.sendmail(
                self.username,
                self.username,
                self.compose_msg("failure", self.failure_msg),
            )

    def send_success(self):
        with self.connect_to_server() as server:
            server.sendmail(
                self.username,
                self.username,
                self.compose_msg("success", self.success_msg),
            )

    def send_recover(self):
        with self.connect_to_server() as server:
            server.sendmail(
                self.username,
                self.username,
                self.compose_msg("recover", self.recover_msg),
            )


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

