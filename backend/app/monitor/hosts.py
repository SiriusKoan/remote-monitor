from .funcs import Ping, Nmap, CheckSMTP, CheckSMTPS, CheckDNS, DNSRecord, CheckWebsite, GeneralNC

hosts = [
    {
        "name": "DNS",
        "addr": "10.8.0.2",
        "bool_functions": [Ping(1), CheckDNS(3, 3)],
        "text_functions": [DNSRecord(60, "google.com")],
    },
    {
        "name": "Mail",
        "addr": "10.8.0.1",
        "bool_functions": [Ping(1), CheckSMTP(3, 3), CheckSMTPS(3, 3), CheckWebsite(60, schema="https")],
        "text_functions": [Nmap(3600)],
    },
    {
        "name": "Minecraft",
        "addr": "10.8.0.101",
        "bool_functions": [Ping(1), GeneralNC(60, 25565)],
        "text_functions": [],
    },
    {
        "name": "NFS",
        "addr": "10.8.0.123",
        "bool_functions": [Ping(1)],
        "text_functions": [],
    },
]
