

from simple_proxy import receive_from
import socket
import argparse
import time
from distutils.util import strtobool
args_parser = argparse.ArgumentParser()
args_parser.add_argument("-rhost", type=str)
args_parser.add_argument("-rport", type=int)
args_parser.add_argument("-lhost", type=str)
args_parser.add_argument("-lport", type=int)
args_parser.add_argument("-recv_first", type=strtobool)
args = args_parser.parse_args()

rhost = args.rhost
rport = args.rport
lhost = args.lhost
lport = args.lport
recv_first = args.recv_first

if recv_first == False:

    i = 0
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((rhost, rport))
    while True:

        i += 2
        time.sleep(0.2)
        msg = input("send msg:\n\t ")
        if msg == "exit":
            break
        s.send(msg.encode()*i)
        print("sent")
    s.close()
else:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((lhost, lport))
        s.listen()

        i = 0

        while True:
            i += 3
            cl, info = s.accept()
            print(info)
            data = receive_from(cl)
            cl.send(b"DATA")
            print(data)
