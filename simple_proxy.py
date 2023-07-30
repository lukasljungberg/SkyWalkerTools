import sys
import socket
import threading
import argparse

HEX_FILTER = ''.join([(len(repr(chr(i))) == 3) and chr(i)
                      or '.' for i in range(256)])


def hexdump(src, length=16, show=True):
    if isinstance(src, bytes):
        try:
            src = src.decode()
        except:
            line = "[*** un-decodable data ***]"
            print(line)
            return

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


def receive_from(connection):
    buffer = b""
    connection.settimeout(5)
    try:
        while True:
            data = connection.recv(4096)
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


def proxy_handler(client_socket: socket.socket, remote_host, remote_port, receive_first):
    remote_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    remote_socket.connect((remote_host, remote_port))

    if receive_first:
        remote_buffer = receive_from(remote_socket)
        hexdump(remote_buffer)

        remote_buffer = response_handler(remote_buffer)

        if len(remote_buffer):
            print("[<==] Sending %d bytes to localhost. [<==]" %
                  len(remote_buffer))
            client_socket.send(remote_buffer)

    while True:
        local_buffer = receive_from(client_socket)

        if len(local_buffer):
            print("[==>] Received %d bytes from localhost. [==>]")
            hexdump(local_buffer)
            local_buffer = request_handler(local_buffer)
            remote_socket.send(local_buffer)
            print("[==>] Sent %d bytes to remote. [==>]" % len(local_buffer))

        remote_buffer = receive_from(remote_socket)
        if len(remote_buffer):
            print("[<==] Receiving %d bytes from remote. [<==]" %
                  len(remote_buffer))
            hexdump(remote_buffer)

            remote_buffer = response_handler(remote_buffer)
            client_socket.send(remote_buffer)
            print("[<==] Sent %d bytes to localhost. [<==]" %
                  len(remote_buffer))

        if not len(local_buffer) or not len(remote_buffer):
            client_socket.close()
            remote_socket.close()
            print("[***] No more data. Closing connections. [***]")
            break


def server_loop(local_host, local_port, remote_host, remote_port, receive_first):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.bind((local_host, local_port))
    except Exception as e:
        print("[!!] Cannot bind socket: %r [!!]" % e)
        print("[!!] Closing program. [!!]")
        sys.exit(0)

    print("[*] Listening on %s:%d" % (local_host, local_port))
    server.listen(2)

    while True:
        client_socket, addr = server.accept()
        print("[***] Connection from %s:%d [***]" % (addr[0], addr[1]))
        proxy_thread = threading.Thread(target=proxy_handler,
                                        args=(client_socket, remote_host,
                                              remote_port, receive_first))
        proxy_thread.start()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-lhost", type=str)
    parser.add_argument("-lport", type=int)
    parser.add_argument("-rhost", type=str)
    parser.add_argument("-rport", type=int)
    parser.add_argument("-recv_first", type=bool)
    args = parser.parse_args()

    server_loop(local_host=args.lhost, local_port=args.lport,
                remote_host=args.rhost, remote_port=args.rport,
                receive_first=args.receive_first)
    print('[***] Finished! [***]')
