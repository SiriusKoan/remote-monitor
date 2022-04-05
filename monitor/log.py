import logging
import logging.handlers
import telebot
from . import config


class TelegramHandler(logging.Handler):
    def __init__(self):
        self.bot = telebot.TeleBot(config.TELEGRAM_TOKEN)
        self.chat_id = config.TELEGRAM_CHAT_ID
        super().__init__()

    def emit(self, msg):
        self.bot.send_message(self.chat_id, self.format(msg))

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
handlers = []
if config.SENDING_LEVEL:
    # stream
    if config.SENDING_LEVEL.get("console", None):
        if not config.CONSOLE_LOG_FORMAT:
            logger.warning("No log format is set for 'console'.")
        stream_handler = logging.StreamHandler()
        stream_format = StreamFormatter(config.CONSOLE_LOG_FORMAT)
        stream_handler.setLevel(config.SENDING_LEVEL.get("console"))
        stream_handler.setFormatter(stream_format)
        handlers.append(stream_handler)
    else:
        logger.warning("Log level for 'console' is not set, no 'console' output.")
    # file
    if config.SENDING_LEVEL.get("file", None):
        if not config.LOG_FILE:
            logger.warning("No log file provided.")
        if not config.FILE_LOG_FORMAT:
            logger.warning("No log format is set for 'file'.")
        file_handler = logging.FileHandler(config.LOG_FILE)
        file_format = logging.Formatter(config.FILE_LOG_FORMAT)
        file_handler.setLevel(config.SENDING_LEVEL.get("file"))
        file_handler.setFormatter(file_format)
        handlers.append(file_handler)
    else:
        logger.warning("Log level for 'file' is not set, no 'file' output.")
    # telegram
    if config.SENDING_LEVEL.get("telegram", None):
        if not config.TELEGRAM_TOKEN:
            logger.warning(
                "Environmental variable 'TELEGRAM_TOKEN' is not set, telegram notification may not work."
            )
        if not config.TELEGRAM_CHAT_ID:
            logger.warning(
                "Environmental variable 'TELEGRAM_CHAT_ID' is not set, telegram notification may not work."
            )
        if not config.TELEGRAM_LOG_FORMAT:
            logger.warning("No log format is set for 'telegram'")
        telegram_handler = TelegramHandler()
        telegram_format = logging.Formatter(config.TELEGRAM_LOG_FORMAT)
        telegram_handler.setLevel(config.SENDING_LEVEL.get("telegram"))
        telegram_handler.setFormatter(telegram_format)
        handlers.append(telegram_handler)
    # email
    if config.SENDING_LEVEL.get("email", None):
        if not config.EMAIL_HOST:
            logger.warning(
                "Environmental variable 'EMAIL_HOST' is not set, email notification may not work."
            )
        if not config.EMAIL_PORT:
            logger.warning(
                "Environmental variable 'EMAIL_HOST_PORT' is not set, email notification may not work."
            )
        if not config.EMAIL_SENDER:
            logger.warning(
                "Environmental variable 'EMAIL_HOST_SENDER' is not set, email notification may not work."
            )
        if not config.EMAIL_HOST_USER:
            logger.warning(
                "Environmental variable 'EMAIL_HOST_USER' is not set, email notification may not work."
            )
        if not config.EMAIL_HOST_PASSWORD:
            logger.warning(
                "Environmental variable 'EMAIL_HOST_PASSWORD' is not set, email notification may not work."
            )
        if not config.EMAIL_ADMIN:
            logger.warning(
                "Environmental variable 'EMAIL_ADMIN' is not set, email notification may not work."
            )
        if not config.EMAIL_LOG_SUBJECT:
            logger.warning(
                "Environmental variable 'EMAIL_LOG_SUBJECT' is not set, email notification may not work."
            )
        if not config.EMAIL_LOG_FORMAT:
            logger.warning("No log format is set for 'email'.")
        email_handler = logging.handlers.SMTPHandler(
            mailhost=config.EMAIL_HOST,
            fromaddr=config.EMAIL_SENDER,
            toaddrs=config.EMAIL_ADMIN.split(),
            subject=config.EMAIL_LOG_SUBJECT,
            credentials=(config.EMAIL_HOST_USER, config.EMAIL_HOST_PASSWORD),
        )
        email_format = logging.Formatter(config.EMAIL_LOG_FORMAT)
        email_handler.setLevel(config.SENDING_LEVEL.get("email"))
        email_handler.setFormatter(email_format)
        handlers.append(email_handler)
    for handler in handlers:
        logger.addHandler(handler)
    logger.info("Loggers are loaded.")
else:
    logger.warning("config.SENDING_LEVEL is not set, no information will be recorded.")
