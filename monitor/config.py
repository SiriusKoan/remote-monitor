import os
import logging

# Telegram notification information
# Telegram bot token, go get one from @BotFather
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
# Telegram chat_id, it can be yourself, the admin group, or a channel
# The ID can be retrived from any message in the chat, just forward a message to @JsonDumpBot and find it in the json
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
# Log format
TELEGRAM_LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

# Email notification information
# Email server, for example, smtp.gmail.com
EMAIL_HOST = os.getenv("EMAIL_HOST")
# Email server port, for example, 587 for gmail
EMAIL_PORT = os.getenv("EMAIL_PORT")
# Email sender
EMAIL_SENDER = os.getenv("EMAIL_SENDER")
# The email account used to send email
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
# Password for the email account
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
# The recipient
EMAIL_ADMIN = os.getenv("EMAIL_ADMIN")
# Log subject
EMAIL_LOG_SUBJECT = os.getenv("EMAIL_LOG_SUBJECT")
# Log format
EMAIL_LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

# Logging
# Log file path
LOG_FILE = "/var/log/monitoring.log"
# Log format for file
FILE_LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
# Log format for console
CONSOLE_LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
# Send notification in specified way when log is above certain level
# Set to None to disable
# Log level from low to high:
# NOTSET(0), DEBUG(10), INFO(20), WARNING(30), ERROR(40), CRITICAL(50)
SENDING_LEVEL = {
    "console": logging.DEBUG,
    "file": logging.DEBUG,
    "telegram": logging.WARNING,
    "email": logging.ERROR,
}

