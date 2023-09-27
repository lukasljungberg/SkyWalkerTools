from ctypes import *
import socket
import struct
import os
import sys
from scapy.all import *
from common import get_iface


class IP(Structure):
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


def sniff(host):
    if os.name == 'nt':
        socket_protocol = socket.IPPROTO_IP
    else:
        socket_protocol = socket.IPPROTO_ICMP

    sniffer = socket.socket(
        socket.AF_INET, socket.SOCK_RAW, socket_protocol)
    sniffer.bind((host, 0))
    # include IP header
    sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

    if os.name == 'nt':
        sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

    try:
        while True:
            # read a packet
            raw_buffer = sniffer.recv(65535)
            # create a IP header from first 20 bytes
            ip_header = IP(raw_buffer[0:20])
            # print detected protocol and hosts
            print('Protocol: %s %s -> %s' % (ip_header.protocol,
                                             ip_header.src_addr,
                                             ip_header.dst_addr))
    except KeyboardInterrupt:
        # if windows, turn off promiscuous mode
        if os.name == 'nt':
            sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
        sys.exit()


if __name__ == '__main__':
    if len(sys.argv) == 2:
        HOST = sys.argv[1]
    else:
        # host to listen on, works only on linux and macOS
        iface = get_iface()

        HOST = get_if_addr(iface)
        if HOST == "0.0.0.0":
            print("No network found..")
            exit(2)
    sniff(HOST)
