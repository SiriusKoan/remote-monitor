from .utils import Host
from .funcs import ping_func


class Google(Host):
    pass


google = Google("8.8.8.8", monitoring_func=[ping_func])
