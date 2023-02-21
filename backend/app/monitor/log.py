import logging
import logging.handlers
from . import config

class StreamFormatter(logging.Formatter):
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
stream_handler = logging.StreamHandler()
stream_format = StreamFormatter(config.CONSOLE_LOG_FORMAT)
stream_handler.setLevel(config.SENDING_LEVEL.get("console"))
stream_handler.setFormatter(stream_format)
logger.addHandler(stream_handler)
