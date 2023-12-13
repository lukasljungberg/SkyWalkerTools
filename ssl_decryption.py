from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
from scapy.all import *
from scapy.layers.tls.all import TLS, TLS13


def get_private_key(file_path):
    key = None
    with open(file_path, 'rb') as key_file:
        key_data = key_file.read()

    return serialization.load_pem_private_key(
        key_data,
        password=None,
        backend=default_backend()
    )


def decrypt(pcap_path, key_path):
    packets = rdpcap(pcap_path)
    private_key = get_private_key(key_path)

    for packet in packets:
        if TLS or TLS13 in packet:
            tls_record = packet[TLS] if TLS in packet else packet[TLS13]
            try:
                for record in tls_record.records:
                    decrypted_data = private_key.decrypt(
                        record.load,
                        padding.OAEP(
                            mgf=padding.MGF1(algorithm=hashes.SHA256()),
                            algorithm=hashes.SHA256(),
                            label=None
                        )
                    )
                    print("Decrypted Data:", decrypted_data.decode('utf-8', 'ignore'))
            except Exception as exc:
                print("Exc: ", exc)


if __name__ == '__main__':
    import sys
    pcap = sys.argv[1]
    key = sys.argv[2]
    try:
        decrypt(pcap, key)
    except FileNotFoundError:
        print(f"Error: File not found.")
    except Exception as exc:
        print("Exc: ", exc)
