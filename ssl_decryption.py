from cryptography.hazmat.primitives.serialization import load_pem_private_key
from cryptography.hazmat.primitives.asymmetric.padding import AsymmetricPadding
from scapy.all import *
from scapy.layers.tls.all import *


def get_private_key(file_path):
    key = None
    with open(file_path, 'rb') as key_file:
        key = key_file.read()

    return load_pem_private_key(key, None)


def decrypt(pcap_path, key_path):
    load_layer('tls')
    packets = rdpcap(pcap_path)
    key = get_private_key(key_path)

    for packet in packets:
        tls_record = None
        print(packet)
        try:
            tls_record = packet[Raw]
            print(tls_record)
        except Exception as exc:
            print(exc)
        if hasattr(tls_record, 'load'):
            for record in tls_record.records:
                print(record)
                try:
                    decrypted_data = key.decrypt(tls_record.load, AsymmetricPadding())
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
