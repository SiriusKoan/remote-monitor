import socket
import abc
from time import sleep
from .log import logger
from ..redis import set_record, get_record


class Netcat:
    """Python 'netcat like' module"""

    """ The snippet is from https://gist.github.com/leonjza/f35a7252babdf77c8421 """

    def __init__(self, ip, port, timeout):
        self.buff = ""
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.settimeout(timeout)
        self.ip = ip
        self.port = port

    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        self.socket.close()

    def connect(self):
        try:
            self.socket.connect((self.ip, self.port))
            return True
        except:
            return False

    def read(self, length=1024):
        return self.socket.recv(length)

    def write(self, data):
        self.socket.send(data)


class Base(abc.ABC):
    @abc.abstractmethod
    def __init__(self):
        return NotImplemented

    def __call__(self, host):
        logger.info(f"{self.__name__} start running")
        while True:
            try:
                res = self.job(host)
                if isinstance(res, bool):
                    set_record(host, self.__name__, "true" if res else "false")
                    if not res:
                        logger.warning(f"{self.__name__}: failed")
                else:
                    old_record = get_record(host, self.__name__)
                    if not old_record or old_record == "false":
                        logger.info(f"{self.__name__}: recover")
                    set_record(host, self.__name__, res)
            except Exception as e:
                set_record(host, self.__name__, "")
                logger.error(f"An error occurs at {self.__name__}: {e.args}")
            sleep(self.interval)

    @abc.abstractmethod
    def job(self, host):
        return NotImplemented
