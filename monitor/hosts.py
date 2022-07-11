from .funcs import ping, nmap, smtp, smtps

hosts = [
    {
        "name": "DNS",
        "addr": "8.8.8.8",
        "bool_functions": [(ping, [1])],
    },
    {
        "name": "Mail",
        "addr": "10.1.1.1",
        "bool_functions": [(ping, [1]), (smtp, [3, 3])],
        "text_functions": [(nmap, [3])],
    },
]
