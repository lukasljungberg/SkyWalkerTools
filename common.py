import socket
from scapy.all import *
HEX_FILTER = ''.join([(len(repr(chr(i))) == 3) and chr(i)
                      or '.' for i in range(256)])


def is_ipv4(addr: str):
    try:
        socket.inet_aton(addr)
        return True
    except socket.error:
        return False


def string_newline(string, x):
    new = ''
    cnt = 0
    if string is not None:
        for ch in string:
            if cnt % x == 0 and cnt != 0:
                new += '\n'
            cnt += 1
            new += ch
    return new


def hexdump(src, length=16, show=False):
    if isinstance(src, bytes):
        try:
            src = src.decode()
        except:
            line = "| un-decodable |"
            return [line]

    results = list()
    for i in range(0, len(src), length):
        word = str(src[i:i+length])

        printable = word.translate(HEX_FILTER)
        hexa = ' '.join(f'{ord(c)}' for c in word)
        hex_width = length*3
        results.append(f'{i:04x} {hexa:<{hex_width}} {printable}')

        if show:
            for line in results:
                print(line)
        else:
            return results


def get_network_adapter_ip():
    for iface in ifaces.data.keys():
        res = get_if_addr(ifaces.dev_from_name(iface))
        isIP = is_ipv4(res) and res != "127.0.0.1" and res != "0.0.0.0"
        if isIP:
            return res
    raise Exception(
        "No network adapter found! Are you connected to a network?")


def get_network_adapter_ip_test():
    from scapy.all import conf
    interfaces = conf.route.routes
    prev = 1
    for interface in interfaces:
        print(interface)
        for i in interface:
            if prev == 0:
                prev = i
                continue
            if i == 0:
                prev = i
            if str(i).startswith('192.'):
                return str(i)

    raise Exception("No network adapter found! Are you connected to a network?")