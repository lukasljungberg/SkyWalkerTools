import simple_proxy
import socket
import argparse
import send_target


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-port", type=int)
    parser.add_argument("-seq_nr", type=int)
    parser.add_argument("-chain_count", type=int)
    args = parser.parse_args()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        host = socket.gethostbyname(socket.gethostname())
        s.bind((host, args.port))
        s.listen(1)
        print("[***] Listening for connections on %s:%d [***]" %
              (host, args.port))
        conn, addr = s.accept()
        data = simple_proxy.receive_from(conn)
        simple_proxy.hexdump(data)
        data = data.decode()
        data = (data.split('[')[1].split(']')[0], int(data.split(':')[1]))
        if args.seq_nr == args.chain_count:
            print("[<==] Streaming data.. [<==]")
            simple_proxy.server_loop(
                host, args.port, data[0], int(data[1]), False)
        else:
            print("[==>] Forwarding target.. [==>]")
            send_target.send_target(data[0], int(data[1]),
                                    (data[2], int(data[3])))

        conn.close()
        s.close()
