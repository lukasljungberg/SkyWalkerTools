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



def is_local_ipv4(ip_address):
    # Check if the IP address belongs to the local network and starts with "192."
    return ip_address.startswith("192.168.")

def get_local_ip_addresses():
    import psutil
    local_ip_addresses = []

    # Iterate over all network interfaces
    for interface, addrs in psutil.net_if_addrs().items():
        for addr in addrs:
            # Check if the address is an IPv4 address and is on the local network
            if addr.family == socket.AF_INET and is_local_ipv4(addr.address):
                local_ip_addresses.append((interface, addr.address))

    return local_ip_addresses


def get_network_adapter_ip():
    for iface in get_local_ip_addresses():
        res = iface[1]
        isIP = is_ipv4(res) and res != "127.0.0.1" and res != "0.0.0.0"
        if isIP:
            return res
    raise Exception(
        "No network adapter found! Are you connected to a network?")


def get_network_adapter_ip_test():
    interfaces = get_local_ip_addresses()
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