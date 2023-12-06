import socket
import os
from rich.table import Table
from rich.live import Live
from rich.align import Align
from rich.console import Console
from scapy.all import *
from sniffer_ip import IP
from common import get_network_adapter_ip

# host to listen on, works on linux, macOS and windows
HOST = get_network_adapter_ip()
if HOST == "0.0.0.0":
    print("No network found..")
    exit(2)
found_hosts = []


def get_n_byte(target, n, n2):
    arr = bytearray(target)[n:n2]
    return arr


console = Console(record=False)


def main():
    # create raw socket, bin to public interface
    if os.name == 'nt':
        # IP layer protocol (windows)
        socket_protocol = socket.IPPROTO_IP
    else:
        # Else icmp layer protocol (macOS)
        socket_protocol = socket.IPPROTO_ICMP

    sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)
    sniffer.bind((HOST, 0))
    # include the IP header in the capture
    sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

    if os.name == 'nt':
        # if we are on windows turn on promiscuous mode
        sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
    table = Table()
    table.add_column("Source host")
    table.add_column("Destination address")
    # TODO: implement port info
    table.title = HOST

    while True:
        try:
            hostdata = sniffer.recv(66565)
        except KeyboardInterrupt:
            console.clear()
            save: str = input("Save HTML file? (y/n)")
            if save.lower() == "y" or save.lower() == "yes":
                console.save_html('./scanned_hosts.html',)
                exit(0)
            exit(0)

        pkt = IP(hostdata)

        if str(pkt.src_addr) not in found_hosts:
            table.add_row(str(pkt.src_addr), str(pkt.dst_addr))

            found_hosts.append(str(pkt.src_addr))
            with Live(table, console=console) as l:
                l.console.clear()
                table_aligned = Align.center(table, vertical="middle")
                l.update(table_aligned)
    # if we are on windows turn off promiscuous mode
    if os.name == 'nt':
        sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)


if __name__ == '__main__':
    main()
