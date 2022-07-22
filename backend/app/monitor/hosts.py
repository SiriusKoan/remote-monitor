from .funcs import (
    Ping,
    Nmap,
    CheckSSH,
    CheckSMTP,
    CheckSMTPS,
    CheckDNS,
    DNSRecord,
    CheckWebsite,
    GeneralNC,
    CheckHTTP,
    CheckHTTPS,
    CheckIMAP,
    CheckIMAPS,
    CheckPOP3,
    CheckPOP3S,
)

hosts = [
    {
        "name": "DNS",
        "addr": "10.8.0.2",
        "bool_functions": [Ping(1), CheckSSH(3), CheckDNS(3)],
        "text_functions": [],
    },
    {
        "name": "Mail",
        "addr": "10.8.0.1",
        "bool_functions": [
            Ping(1),
            CheckSMTP(3),
            CheckWebsite(60, hostname="google.com", schema="https"),
            CheckHTTP(3),
            CheckHTTPS(3),
            CheckIMAP(3),
            CheckPOP3(3),
        ],
        "text_functions": [],
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
        "text_functions": [Nmap(3600)],
    },
]
