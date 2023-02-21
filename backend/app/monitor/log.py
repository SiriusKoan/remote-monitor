import logging
import logging.handlers
from . import config

class Formatter(logging.Formatter):
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


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# console handler
stream_handler = logging.StreamHandler()
stream_format = Formatter(config.CONSOLE_LOG_FORMAT)
stream_handler.setLevel(config.SENDING_LEVEL.get("console"))
stream_handler.setFormatter(stream_format)
logger.addHandler(stream_handler)

# file handler
file_handler = logging.FileHandler(config.LOG_FILE)
file_format = Formatter(config.FILE_LOG_FORMAT)
file_handler.setLevel(config.SENDING_LEVEL.get("file"))
file_handler.setFormatter(file_format)
logger.addHandler(file_handler)

