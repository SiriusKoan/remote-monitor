import os, subprocess
from monitor import google

# check ping
if subprocess.call(["which", "ping"], stdout=open(os.devnull, "w"), stderr=open(os.devnull, "w")):
    print("\033[31mCommand 'ping' does not exist, 'ping' test may fail.\033[39m")
# check nmap
if subprocess.call(["which", "nmap"], stdout=open(os.devnull, "w"), stderr=open(os.devnull, "w")):
    print("\033[31mCommand 'nmap' does not exist, 'nmap' test may fail.\033[39m")
# check telegram
if not os.getenv("TELEGRAM_TOKEN"):
    print("\033[31mEnvironmental variable 'TELEGRAM_TOKEN' is not set, telegram notification may not work.\033[39m")
if not os.getenv("TELEGRAM_CHAT_ID"):
    print("\033[31mEnvironmental variable 'TELEGRAM_CHAT_ID' is not set, telegram notification may not work.\033[39m")
# check email
if not os.getenv("EMAIL_HOST"):
    print("\033[31mEnvironmental variable 'EMAIL_HOST' is not set, email notification may not work.\033[39m")
if not os.getenv("EMAIL_PORT"):
    print("\033[31mEnvironmental variable 'EMAIL_HOST_PORT' is not set, email notification may not work.\033[39m")
if not os.getenv("EMAIL_HOST_USER"):
    print("\033[31mEnvironmental variable 'EMAIL_HOST_USER' is not set, email notification may not work.\033[39m")
if not os.getenv("EMAIL_HOST_PASSWORD"):
    print("\033[31mEnvironmental variable 'EMAIL_HOST_PASSWORD' is not set, email notification may not work.\033[39m")
if not os.getenv("EMAIL_ADMIN"):
    print("\033[31mEnvironmental variable 'EMAIL_ADMIN' is not set, email notification may not work.\033[39m")


# google is example host, please replace the host with yours
google.start()
