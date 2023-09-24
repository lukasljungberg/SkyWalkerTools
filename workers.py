
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
import paramiko
from scp import SCPClient


class Jedi:
    pass


class SSHThread(QThread):
    finished_signal = Signal(str)

    def __init__(self, host, port, username, password):
        super().__init__()
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.ssh_client = paramiko.SSHClient()
        self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.scp = None
        self.remote_PID = None
        self.main_PID = None
        self.pwd = None

    def run(self, cmd: str = "pwd"):
        try:
            self.ssh_client.connect(
                self.host, port=self.port, username=self.username, password=self.password)
            stdin, stdout, stderr = self.ssh_client.exec_command(cmd)
            output = stdout.read().decode('utf-8')
            self.finished_signal.emit(output)
            if cmd == "pwd":
                self.pwd = output
            self.scp = SCPClient(self.ssh_client.get_transport())

        except Exception as e:
            self.finished_signal.emit(
                f"Error connecting to {self.host}: {str(e)}")

    def ignite_ligntsaber(self, transfer_file: str, destination_file: str):
        import socket
        import subprocess
        if self.scp is not None:
            self.scp.put(transfer_file, destination_file)
            self.scp.put("passwd_cracker.py", "passwd_cracker.py")
            self.scp.put("link_list.skwlkr", "link_list.skwlkr")
            # stdin, stdout, stderr = self.ssh_client.exec_command(
            #    f"python3 {self.pwd}/{destination_file} --host-type remote 192.168.64.1")
            # output = stdout.read().decode('utf-8')
            # self.finished_signal.emit(output)
            stdpwd = subprocess.check_output("pwd")
            pwd = stdpwd.decode('utf-8')
            pwd = pwd.replace('\n', '')
            # subprocess.call(
            #    f"{pwd}/venv/bin/python {pwd}/lightsaber.py --host-type main 192.168.64.1", shell=True)
            # print("running lightsaber!")

    def shutdown_ligntsaber(self, hosts: list[str]):
        import lightsaber
        lightsaber.shutdown(hosts)

    def stop(self):
        self.ssh_client.close()
        self.terminate()


class CMDThread(QThread):
    any_signal = Signal(str)

    def __init__(self, parent: Jedi = None):
        super().__init__(parent)
        self.jedi = parent
        self.counter = 1

    def init_counter(self):
        self.counter = 1

    def run(self):
        while self.jedi.cmd_thread_running:
            if self.jedi.pressed_return:
                self.any_signal.emit(
                    str((self.jedi.text_input.text(), self.counter)))
                self.counter += 1
                self.jedi.text_input.clear()
                self.jedi.pressed_return = False
        print("Exited Thread run!")

    def stop(self):
        self.jedi.cmd_thread_running = False
        self.terminate()
        print("stopped thread")


class PingThread(QThread):
    any_signal = Signal(str)

    def __init__(self, parent: Jedi = None):
        super().__init__(parent)
        self.jedi = parent

    def run(self):

        print("Exited Thread run!")

    def stop(self):
        self.terminate()
        print("stopped thread")
