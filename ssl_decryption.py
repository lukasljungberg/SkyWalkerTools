from cryptography.hazmat.primitives.serialization import load_pem_private_key
from cryptography.hazmat.primitives.asymmetric.padding import AsymmetricPadding
from scapy.layers.tls.all import TLS13
from scapy.all import *


def get_private_key(file_path):
    key = None
    with open(file_path, 'rb') as key_file:
        key = key_file.read()

    return load_pem_private_key(key, None)


def decrypt(pcap_path, key_path):
    packets = rdpcap(pcap_path)
    key = get_private_key(key_path)

    for packet in packets:
        if 'TLS' in packet:
            tls_record = packet[TLS13]
            print(tls_record)
            if hasattr(tls_record, 'records'):
                for record in tls_record.records:
                    print(record)
                    try:
                        decrypted_data = key.decrypt(record.load, AsymmetricPadding())
                        print("Decrypted Data:", decrypted_data.decode('utf-8', 'ignore'))
                    except Exception as exc:
                        print("Exc: ", exc)


if __name__ == '__main__':
    pcap = sys.argv[1]
    key = sys.argv[2]
    try:
        decrypt(pcap, key)
    except FileNotFoundError:
        print(f"Error: File not found.")
    except Exception as exc:
        print("Exc: ", exc)
