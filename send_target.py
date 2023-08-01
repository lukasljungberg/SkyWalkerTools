import socket
import argparse


def is_IPv4(host):
    if socket.gethostbyaddr(host):
        return True
    return False


def send_target(target_host, target_port, chain_proxy: tuple):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print(target_host)
        if is_IPv4(target_host) and isinstance(target_port, int):
            target_port = str(target_port)

            s.connect(chain_proxy)
            data = ('[' + target_host + ']' + ':' + str(target_port)).encode()
            s.send(data)
        s.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-host", type=str)
    parser.add_argument("-port", type=int)
    parser.add_argument("-chain_host", type=str)
    parser.add_argument("-chain_port", type=int)
    args = parser.parse_args()
    send_target(args.host, args.port, (args.chain_host, args.chain_port))
