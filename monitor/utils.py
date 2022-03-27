import abc
import smtplib
import time
import threading
import telebot
from . import config


class Host(abc.ABC):
    def __init__(
        self, ip_addr=None, domain=None, mac=None, hostname=None, monitoring_func=[]
    ) -> None:
        self.ip_addr = ip_addr
        self.domain = domain
        self.mac = mac
        self.hostname = hostname
        self.monitoring_func = monitoring_func


class MonitoringFunc(abc.ABC):
    def __init__(self, name, func, interval=1) -> None:
        self.name = name
        self.func = func
        self.interval = interval
        self.thread = threading.Thread(target=self.job)

    def job(self):
        fail = False
        while True:
            res = self.func()
            if not res:
                self.send_failure()
                fail = True
            else:
                if fail:
                    self.send_recover()
                    fail = False
            time.sleep(self.interval)

    def start(self):
        self.thread.start()

    def send_failure(self):
        return NotImplemented

    def send_success(self):
        return NotImplemented

    def send_recover(self):
        return NotImplemented


class NotifyTelegram(MonitoringFunc):
    def __init__(self, name, func, interval=1) -> None:
        super().__init__(name, func, interval)
        self.bot = telebot.TeleBot(config.TELEGRAM_TOKEN)
        self.chat_id = config.TELEGRAM_CHAT_ID

    def send_failure(self, msg):
        self.bot.send_message(self.chat_id, msg)

    def send_success(self, msg):
        self.bot.send_message(self.chat_id, msg)

    def send_recover(self, msg):
        self.bot.send_message(self.chat_id, msg)


class NotifyEmail(MonitoringFunc):
    def __init__(self, name, func, interval=1) -> None:
        super().__init__(name, func, interval)
        self.host = config.EMAIL_HOST
        self.port = config.EMAIL_PORT
        self.username = config.EMAIL_HOST_USER
        self.password = config.EMAIL_HOST_PASSWORD

    def connect_to_server(self):
        server = smtplib.SMTP(self.host, self.port)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(self.username, self.password)
        return server

    def compose_msg(self, subject, msg):
        return f"Subject: {subject}\n\n{msg}"

    def send_msg(self, msg):
        with self.connect_to_server() as server:
            server.sendmail(self.username, self.username, msg)

