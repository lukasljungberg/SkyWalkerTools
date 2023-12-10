import socket
import sys
import threading


def scan_camera(ip, port):
    # Attempt to connect to the specified IP and port
    try:
        with socket.create_connection((ip, port), timeout=1):
            print(f"Service found at {ip}:{port}")
    except (socket.timeout, socket.error):
        pass


def detect_cameras(subnet, start_range, end_range, port):
    # Iterate through the IP range in the specified subnet
    for i in range(start_range, end_range + 1):
        ip = f"{subnet}.{i}"
        # Use threading for faster scanning
        threading.Thread(target=scan_camera, args=(ip, port)).start()


if __name__ == "__main__":
    # Specify your local network details
    subnet = "192.168.1"  # Change this to your subnet
    start_ip = 1
    end_ip = 2
    target_port = int(sys.argv[1])

    # Detect cameras on the local network
    detect_cameras(subnet, start_ip, end_ip, target_port)