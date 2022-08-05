from ..funcs import (
    Ping,
    GeneralNC,
    CheckSSH,
    CheckDNS,
    CheckSMTP,
    CheckSMTPS,
    CheckHTTP,
    CheckHTTPS,
    CheckIMAP,
    CheckIMAPS,
    CheckPOP3,
    CheckPOP3S,
    CheckWebsite,
    Nmap,
    DNSRecord,
    SSHCommand,
)


def test_ping():
    func = Ping(0)
    func.job("8.8.8.8")


def test_general_nc():
    func = GeneralNC(0, 80)
    func.job("8.8.8.8")


def test_check_ssh():
    func = CheckSSH(0)
    func.job("8.8.8.8")


def test_check_dns():
    func = CheckDNS(0)
    func.job("8.8.8.8")


def test_check_smtp():
    func = CheckSMTP(0)
    func.job("8.8.8.8")


def test_check_smtps():
    func = CheckSMTPS(0)
    func.job("8.8.8.8")


def test_check_http():
    func = CheckHTTP(0)
    func.job("8.8.8.8")


def test_check_https():
    func = CheckHTTPS(0)
    func.job("8.8.8.8")


def test_check_imap():
    func = CheckIMAP(0)
    func.job("8.8.8.8")


def test_check_imaps():
    func = CheckIMAPS(0)
    func.job("8.8.8.8")


def test_check_pop3():
    func = CheckPOP3(0)
    func.job("8.8.8.8")


def test_check_pop3s():
    func = CheckPOP3S(0)
    func.job("8.8.8.8")


def test_check_website():
    func = CheckWebsite(0)
    func.job("1.1.1.1")


def test_nmap():
    func = Nmap(0)
    func.job("8.8.8.8")


def test_dns_record():
    func = DNSRecord(0, "google.com")
    func.job("8.8.8.8")


# def test_ssh_command():
#    func = SSHCommand(0, "ping 1.1.1.1", "root")
#    func.job("8.8.8.8")
