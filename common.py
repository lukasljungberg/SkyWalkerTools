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


def get_iface():
    try:
        return ifaces.dev_from_name("en0")
    except:
        try:
            return ifaces.dev_from_name("eth0")
        except:
            return ifaces.dev_from_name("lan")
