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
        logger.info(f"{host}:{self.__name__}:Start running")
        while True:
            try:
                res = self.job(host)
                if isinstance(res, bool):
                    if not res:
                        logger.warning(f"{host}:{self.__name__}:Failed")
                    else:
                        old_record = get_record(host, self.__name__)
                        if old_record.decode() != "true":
                            logger.info(f"{host}:{self.__name__}:Recover")
                    set_record(host, self.__name__, "true" if res else "false")
                else:
                    set_record(host, self.__name__, res)
            except Exception as e:
                set_record(host, self.__name__, "")
                logger.error(f"An error occurs at {self.__name__}: {e.args}")
            sleep(self.interval)

    @abc.abstractmethod
    def job(self, host):
        return NotImplemented
