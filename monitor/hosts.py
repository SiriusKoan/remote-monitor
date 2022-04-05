from .utils import Host
from .funcs import ping_func, nmap_func, smtp_func, smtps_func


google = Host("8.8.8.8", monitoring_func=[ping_func, nmap_func, smtp_func, smtps_func])
