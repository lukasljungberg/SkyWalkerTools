import threading
from ctypes import *
from scapy.all import *
from common import get_network_adapter_ip
import ipaddress
print(f'OS: {os.name}')

# Subnet to target
SUBNET = '192.168.1.0/24'
# Spray-string to send
MESSAGE = "PYTHONIC!"


class ICMP(Structure):
    _fields_ = [
        ("type", c_ubyte, 8),
        ("code", c_ubyte, 8),
        ("checksum", c_ushort, 16),
        ("unused", c_ushort, 16),
        ("next_hop_mtu", c_ushort, 16),
    ]

    def __new__(cls, socket_buff=None):
        return cls.from_buffer_copy(socket_buff)

    def __init__(self, socket_buff=None):
        pass  # You can add any additional initialization logic if needed


class IP(Structure):
    # headers for IP protocol
    _fields_ = [
        ("version", c_ubyte, 4),
        ("ihl", c_ubyte, 4),
        ("tos", c_ubyte, 8),
        ("len", c_ushort, 16),
        ("id", c_ushort, 16),
        ("offset", c_ushort, 16),
        ("ttl", c_ubyte, 8),
        ("protocol_num", c_ubyte, 8),
        ("sum", c_ushort, 16),
        ("src", c_uint32, 32),
        ("dst", c_uint32, 32),
    ]

    def __new__(cls, socket_buff=None):
        return cls.from_buffer_copy(socket_buff)

    def __init__(self, socket_buff=None):
        # readable IP adresses
        self.src_addr = socket.inet_ntoa(struct.pack("<L", self.src))
        self.dst_addr = socket.inet_ntoa(struct.pack("<L", self.dst))

        # map protocol constant to their names
        self.protocol_map = {1: "ICMP", 6: "TCP", 17: "UDP"}
        try:
            self.protocol = self.protocol_map[self.protocol_num]
        except Exception as e:
            print("%s No protocol for %s" % (e, self.protocol_num))
            self.protocol = str(self.protocol_num)


def udp_sender():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sender:
        for ip in ipaddress.ip_network(SUBNET).hosts():
            sender.sendto(bytes(MESSAGE, 'utf-8'), (str(ip), 65212))


class Scanner:
    """Works best on windows, because of the promiscuous mode."""
    def __init__(self, host) -> None:
        self.host = host
        if os.name == 'nt':
            socket_protocol = socket.IPPROTO_IP
        else:
            socket_protocol = socket.IPPROTO_ICMP

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)
        self.socket.bind((host, 0))
        self.socket.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

        if os.name == 'nt':
            self.socket.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

    def sniff(self) -> None:
        hosts_up = {f'{str(self.host)} *'}
        try:
            while True:
                # read packet
                raw_buffer = self.socket.recvfrom(65535)[0]
                ip_header = IP(raw_buffer[0:20])

                if ip_header.protocol == "ICMP":
                    icmp_packet = ICMP(raw_buffer[sizeof(IP):])
                    if icmp_packet.code == 3 and icmp_packet.type == 3:
                        if ipaddress.ip_address(ip_header.src_addr) in ipaddress.IPv4Network(SUBNET):
                            if raw_buffer[len(raw_buffer) - len(MESSAGE):] == bytes(MESSAGE, 'utf-8'):
                                tgt = str(ip_header.src_addr)
                                if tgt != self.host and tgt not in hosts_up:
                                    hosts_up.add(str(ip_header.src_addr))
                                    print(f'Host up: {tgt}')
        except KeyboardInterrupt:
            if os.name == 'nt':
                self.socket.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
            print('\n User interrupted.')
            if hosts_up:
                print(f'\n\nSummary: Hosts up on {SUBNET}')
            for host in sorted(hosts_up):
                print(f'{host}')


if __name__ == '__main__':
    if len(sys.argv) == 2:
        HOST = sys.argv[1]
    else:
        # host to listen on, works on linux and macOS and windows
        HOST = get_network_adapter_ip()

    print(f'Host: {HOST}')
    s = Scanner(HOST)
    time.sleep(5)
    t = threading.Thread(target=udp_sender)
    t.start()
    s.sniff()
