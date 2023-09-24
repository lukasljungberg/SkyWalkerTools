from distutils.util import strtobool
from rich.table import Table
from rich.live import Live
from rich.console import Console
import sys
import socket
import threading
import argparse
from rich.align import Align
from rich import themes
from common import string_newline, hexdump


def generate_table(print_data: tuple, live: Live = None) -> Table:
    """Make a new table."""

    table = Table(expand=True)
    table.add_column("HEX_dump_local")
    table.add_column("Info")
    table.add_column("Connection")
    table.add_column("HEX_dump_remote")
    if live:
        live.console.clear()
        print("[ ctrl + c ] to exit..")
    if print_data:
        hl, info, cinfo, hr = print_data
        table.add_row(
            string_newline(hl[0], 16 * 2) if hl else "", string_newline(info, 100), string_newline(cinfo, 150), string_newline(
                hr[0], 16 * 2) if hr else ""
        )
        # Adding the hex rows
        for lrow, rrow in zip(hl, hr):
            table.add_row(
                string_newline(lrow, 16 * 2) if lrow else "", "", "", string_newline(
                    rrow, 16 * 2) if rrow else ""
            )
    table = Align.center(table, height=10, vertical="middle")
    return table


live = Live(generate_table(()), refresh_per_second=1)
live.console.set_window_title("[***] Simple proxy [***]")


def receive_from(connection: socket.socket):
    buffer = b""
    connection.settimeout(20)
    try:
        while True:
            data = connection.recv(4096*2)
            if not data:
                break
            buffer += data
    except Exception as e:
        pass

    return buffer


def request_handler(buffer):
    # perform packet modifications
    return buffer


def response_handler(buffer):
    # perform packet modifications
    return buffer


def proxy_handler(client_socket: socket.socket, remote_host, remote_port, receive_first, cinfo):

    remote_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    remote_socket.connect((remote_host, remote_port))
    remote_hex = []
    local_hex = []
    info = None
    if receive_first:
        remote_buffer = receive_from(remote_socket)
        _hex = hexdump(remote_buffer)
        for hex in _hex:
            remote_hex.append(hex)
        remote_buffer = response_handler(remote_buffer)

        if len(remote_buffer):
            info = "[<==] Sending %d bytes to localhost. [<==]" % len(
                remote_buffer)
            client_socket.send(remote_buffer)
    empty_data_cntr = 0
    with live as l:
        l.update(generate_table((local_hex, info, cinfo, remote_hex), l))
    while True:
        local_buffer = receive_from(client_socket)

        if len(local_buffer):
            info = "[==>] Received %d bytes from localhost. [==>]"
            _hex = hexdump(local_buffer)
            print(_hex)
            for hex in _hex:
                local_hex.append(hex)
            local_buffer = request_handler(local_buffer)
            remote_socket.send(local_buffer)
            info = "[==>] Sent %d bytes to remote. [==>]" % len(local_buffer)
            with live as l:
                l.update(generate_table(
                    (local_hex, info, cinfo, remote_hex), l))
        remote_buffer = receive_from(remote_socket)
        if len(remote_buffer):
            info = "[<==] Receiving %d bytes from remote. [<==]" % len(
                remote_buffer)
            with live as l:
                l.update(generate_table(
                    (local_hex, info, cinfo, remote_hex), l))
            _hex = hexdump(remote_buffer)
            print(_hex)
            for hex in _hex:
                remote_hex.append(hex)
            remote_buffer = response_handler(remote_buffer)
            client_socket.send(remote_buffer)
            info = "[<==] Sent %d bytes to localhost. [<==]" % len(
                remote_buffer)
        with live as l:
            l.update(generate_table((local_hex, info, cinfo, remote_hex), l))
        if not len(local_buffer) or not len(remote_buffer):
            empty_data_cntr += 1
            if empty_data_cntr >= 5:
                empty_data_cntr = 0
                client_socket.close()
                remote_socket.close()
                info = "[***] No more data. Closing connections. [***]"
                break

    with live as l:
        l.update(generate_table((local_hex, info, cinfo, remote_hex), l))


def server_loop(local_host, local_port, remote_host, remote_port, recieve_first):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cinfo = "INIT"
    global live
    try:
        server.bind((local_host, local_port))
    except Exception as e:
        cinfo = "[!!] Cannot bind socket: %r [!!]" % e
        cinfo += "\n[!!] Closing program. [!!]"
        print_data = (['init'], ['init'], cinfo, ['init'])
        with live as l:
            l.update(generate_table(print_data))
        sys.exit(0)

    cinfo = "[*] Listening on %s:%d" % (local_host, local_port) + "[*]"
    server.listen(2)
    with live as l:
        l.update(generate_table(([""], "", cinfo, [""]), l))
    while True:
        try:
            client_socket, addr = server.accept()
        except KeyboardInterrupt:
            live.console.clear()
            exit(0)
        cinfo = "[***] Connection from %s:%d [***]" % (addr[0], addr[1])
        proxy_thread = threading.Thread(target=proxy_handler,
                                        args=(client_socket, remote_host,
                                              remote_port, recieve_first, cinfo))
        proxy_thread.daemon = True
        proxy_thread.start()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-lhost", type=str)
    parser.add_argument("-lport", type=int)
    parser.add_argument("-rhost", type=str)
    parser.add_argument("-rport", type=int)
    parser.add_argument("-recv_first", type=strtobool)
    args = parser.parse_args()
    server_loop(local_host=args.lhost, local_port=args.lport,
                remote_host=args.rhost, remote_port=args.rport,
                recieve_first=args.recv_first)
