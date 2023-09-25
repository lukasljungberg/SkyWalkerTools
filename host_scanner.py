import socket
import os
from rich.table import Table
from rich.live import Live
from rich.align import Align
from rich.console import Console
from scapy.all import *
from scapy.layers.inet import ICMP, IP, UDP

# host to listen on
print(ifaces)
iface = ifaces.dev_from_index(2)
HOST = get_if_addr(iface)
found_hosts = []

print(HOST)


def get_n_byte(target, n, n2):
    arr = bytearray(target)[0:76]
    return arr


console = Console(record=True)


def main():
    # create raw socket, bin to public interface
    if os.name == 'nt':
        socket_protocol = socket.IPPROTO_IP
    else:
        socket_protocol = socket.IPPROTO_ICMP

    sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)
    sniffer.bind((HOST, 0))
    # include the IP header in the capture
    sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

    if os.name == 'nt':
        # if we are on windows turn on promiscuous mode
        sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
    table = Table()
    table.add_column("Host")
    table.add_column("Packet")
    # TODO: implement port info
    table.title = HOST

    while True:
        try:
            hostdata = sniffer.recv(66565)
        except KeyboardInterrupt:
            save: str = input("Save HTML file? (y/n)")
            if save.lower() == "y" or save.lower() == "yes":
                console.save_html('./scanned_hosts.html',)
                exit(0)

        pkt = IP(hostdata)

        if str(pkt.getfieldval("src")) not in found_hosts:
            table.add_row(str(pkt.getfieldval("src")), str(pkt))

            found_hosts.append(str(pkt.getfieldval("src")))
            with Live(table, console=console) as l:
                l.console.clear()
                l.console.clear_live()

                table_aligned = Align.center(table, vertical="middle")
                l.update(table_aligned)
            console._record_buffer = console._record_buffer[-(
                32)-(12)*len(table.rows):-1]
        print(len(console._record_buffer))

    # if we are on windows turn off promiscuous mode
    if os.name == 'nt':
        sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)


if __name__ == '__main__':
    main()
