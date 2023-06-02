import logging
import logging.handlers
import requests
from . import config

class ColorFormatter(logging.Formatter):
    def __init__(self, fmt):
        self.color_table = {
            logging.CRITICAL: "\033[31m",
            logging.ERROR: "\033[31m",
            logging.WARNING: "\033[33m",
            logging.INFO: "\033[34m",
        }
        super().__init__(fmt)

    def format(self, msg):
        color = self.color_table[msg.levelno]
        formatter = logging.Formatter(self._fmt)
        return color + formatter.format(msg) + "\033[39m"

class ObjectFormatter(logging.Formatter):
    def __init__(self, fmt):
        super().__init__("")

    def format(self, msg):
        color = self.color_table[msg.levelno]
        formatter = logging.Formatter(self._fmt)
        return color + formatter.format(msg) + "\033[39m"

class DiscordHandler(logging.Handler):
    def __init__(self):
        self.webhook_url = config.DC_WEBHOOK_URL
        self.color_table = {
            "ERROR": 16711680, # red
            "WARNING": 16744192, # orange
            "INFO": 65280, # green
        }
        super().__init__()

    def emit(self, msg):
        info = msg.msg
        level = msg.levelname
        data = {
            "username": "Remote Monitor",
            "embeds": [
                {
                    "title": info,
                    # "description": stat,
                    "color": self.color_table.get(level, self.color_table["INFO"])
                }
            ],
        }
        requests.post(self.webhook_url, json=data)


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# console handler
stream_handler = logging.StreamHandler()
stream_format = ColorFormatter(config.CONSOLE_LOG_FORMAT)
stream_handler.setLevel(config.SENDING_LEVEL.get("console"))
stream_handler.setFormatter(stream_format)
logger.addHandler(stream_handler)

# file handler
file_handler = logging.FileHandler(config.LOG_FILE)
file_format = ColorFormatter(config.FILE_LOG_FORMAT)
file_handler.setLevel(config.SENDING_LEVEL.get("file"))
file_handler.setFormatter(file_format)
logger.addHandler(file_handler)

# email handler
email_handler = logging.handlers.SMTPHandler(mailhost=config.MAIL_HOST, fromaddr=config.EMAIL_SENDER, toaddrs=config.EMAIL_ADMIN, subject=config.EMAIL_LOG_SUBJECT)
email_format = logging.Formatter(config.EMAIL_LOG_FORMAT)
email_handler.setLevel(config.SENDING_LEVEL.get("email"))
email_handler.setFormatter(email_format)
logger.addHandler(email_handler)

# Discord handler
discord_handler = DiscordHandler()
discord_format = ObjectFormatter(config.EMAIL_LOG_FORMAT)
discord_handler.setLevel(config.SENDING_LEVEL.get("discord"))
discord_handler.setFormatter(discord_format)
logger.addHandler(discord_handler)

