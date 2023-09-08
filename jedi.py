
# pyside6-uic ./GUI/graphics.ui -o jedi_ui.py
from typing import Optional
from PySide6.QtCore import *
import PySide6.QtGui
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from jedi_ui import Ui_MainWindow
import sys
import time
import os
import socket
import subprocess
import paramiko


class SSHThread(QThread):
    finished_signal = Signal(str)

    def __init__(self, host, port, username, password):
        super().__init__()
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        # Create an SSH client instance
        self.ssh_client = paramiko.SSHClient()
        self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        print("connecting")
        # Connect to the SSH server
        self.ssh_client.connect(self.host, port=self.port,
                                username=self.username, password=self.password)
        print("connected")

    def run_connect(self, cmd):
        try:

            # Execute the "ls" command
            stdin, stdout, stderr = self.ssh_client.exec_command(cmd)

            # Read and emit the command output
            output = stdout.read().decode('utf-8')
            self.finished_signal.emit(output)

        except Exception as e:
            self.finished_signal.emit(
                f"Error connecting to {self.host}: {str(e)}")

    def stop(self):
        self.ssh_client.close()
        self.terminate()
        print("stopped thread")


def is_ipv4(addr: str):
    try:
        socket.inet_aton(addr)
        return True
    except socket.error:
        return False


class Jedi(Ui_MainWindow):
    emitted_ssh_cmd = Signal(str)

    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.retranslateUi(self)

        self.pressed_return = False
        self.text_input.returnPressed.connect(self.pressReturnCMD)
        self.ssh_proto.pressed.connect(self.ssh_init)

        self.cmd_thread = CMDThread(self)
        self.cmd_thread.start()
        self.cmd_thread_running = True
        self.cmd_thread.any_signal.connect(self.enter_cmd)
        self.cmd_handler = CMDHandler()

        self.ssh_connection = None
        self.ssh_client = {}
        if os.path.isfile("./proxy_list.hosts"):
            self.cmd_handler.add_hosts(self)
        else:
            with open("./proxy_list.hosts", "w") as f:
                f.write("127.0.0.1")
            self.cmd_handler.add_hosts(self)

    def start_ssh(self):
        self.ssh_thread = SSHThread(self.remote_host.currentText(),
                                    self.remote_port.value(),
                                    self.ssh_client['username'],
                                    self.ssh_client['password'])
        self.emitted_ssh_cmd.connect(self.ssh_thread.run_connect)
        self.ssh_thread.finished_signal.connect(self.output)
        try:
            self.cmd_thread.any_signal.disconnect(self.enter_cmd)
        except:
            pass
        self.cmd_thread.any_signal.connect(self.running_ssh)
        self.ssh_thread.start()

    def pressReturnCMD(self):
        self.pressed_return = True

    def output(self, output: str):
        self.out_display.append(output)

    def running_ssh(self, cmd: str):
        cmd = eval(cmd)[0]
        if cmd == "exit":
            try:
                self.cmd_thread.any_signal.disconnect(self.running_ssh)
            except:
                pass
            self.cmd_thread.any_signal.connect(self.enter_cmd)
            self.ssh_thread.stop()
            self.output("SSH connection closed!")
            return
        if cmd == "clear":
            self.out_display.setText("")
        self.emitted_ssh_cmd.emit(cmd)

    def ssh_init(self):
        self.cmd_thread.init_counter()
        try:
            self.cmd_thread.any_signal.disconnect(self.enter_cmd)
        except:
            pass
        self.out_display.setText("Enter username...")
        self.cmd_thread.any_signal.connect(self.ssh_)

    def ssh_(self, cmd: str):
        cmd = eval(cmd)
        counter = cmd[1]
        cmd = cmd[0]
        if counter == 1:
            self.ssh_client["hostname"] = self.remote_host.currentText()
            self.out_display.setText("Enter password...")
            self.ssh_client["username"] = cmd

        if counter == 2:
            self.ssh_client["password"] = cmd
            try:
                self.start_ssh()
            except paramiko.ssh_exception.AuthenticationException:
                self.output("Connection failed!\nWrong credentials.")
                self.ssh_thread.finished_signal.connect(self.output)
                try:
                    self.cmd_thread.any_signal.disconnect(self.running_ssh)
                except:
                    pass
                self.cmd_thread.any_signal.connect(self.enter_cmd)
                return
            self.output("Connected.")

    def clear_hosts(self):
        self.next_host.clear()
        self.target_host.clear()
        self.remote_host.clear()

    # handles GUI after command
    def enter_cmd(self, cmd: str):
        cmd = eval(cmd)
        counter = cmd[1]
        cmd = cmd[0]
        if cmd == "clear":
            self.out_display.clear()
            return
        val = self.cmd_handler.handle_cmd(cmd)

        if cmd.split(' ')[0] == "append":
            if cmd.split(" ")[1].lower() == "host":
                self.clear_hosts()
                self.cmd_handler.add_hosts(self)
                self.out_display.append("added host " + val + "\n")
                return

        if cmd.split(' ')[0] == "delete":
            if cmd.split(" ")[1].lower() == "host":
                self.clear_hosts()
                self.cmd_handler.add_hosts(self)
                self.out_display.append("deleted host " + val + "\n")
                return

        if cmd.split(' ')[0] == "cd":
            os.chdir(cmd.split(' ')[1])

        if isinstance(val, bytes):
            self.out_display.append(val.decode())
        else:
            self.out_display.append(val + "\n")

    def closeEvent(self, event: QCloseEvent) -> None:
        self.cmd_thread_running = False
        time.sleep(0.2)
        self.cmd_thread.stop()
        return super().closeEvent(event)


class CMDHandler():

    def handle_cmd(self, cmd: str) -> str | None:
        if self.cmd_type(cmd) == "append":
            if self.cmd_action(cmd).lower() == "host":
                val = self.cmd_value(cmd)
                if is_ipv4(val):
                    self.append_host(val)
                    return val
        if self.cmd_type(cmd) == "delete":
            if self.cmd_action(cmd).lower() == "host":
                val = self.cmd_value(cmd)
                self.delete_host(val)
                return val

        output = subprocess.check_output(cmd.split(' '))
        return output

    def cmd_type(self, cmd) -> str:
        return str(cmd.split(" ")[0]).lower()

    def cmd_action(self, cmd) -> str:
        try:
            return str(cmd.split(" ")[1]).lower()
        except:
            return False

    def cmd_value(self, cmd):
        try:
            return str(cmd.split(" ")[-1]).lower()
        except:
            return False

    def append_host(self, addr: str) -> bool:
        if is_ipv4(addr):
            with open("./proxy_list.hosts", "a") as f:
                f.write(addr + "\n")
            return True
        else:
            return False

    def add_hosts(self, wid: Jedi):
        with open("./proxy_list.hosts", "r") as f:
            lines = f.read()
            lines = lines.split('\n')
            for line in lines:
                if line:
                    wid.remote_host.addItem(line)
                    wid.next_host.addItem(line)

    def delete_host(self, host):
        lines = None
        with open("./proxy_list.hosts", "r") as f:
            lines = f.read()
            lines = lines.split('\n')
            lines.remove(host)
        with open("./proxy_list.hosts", "w") as f:
            f.write(''.join([line + "\n" for line in lines if line]))


class CMDThread(QThread):
    any_signal = Signal(str)

    def __init__(self, parent: Jedi = None) -> None:
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
        self.terminate()
        print("stopped thread")


class PingThread(QThread):
    any_signal = Signal(str)

    def __init__(self, parent: Jedi = None) -> None:
        super().__init__(parent)
        self.jedi = parent

    def run(self):

        print("Exited Thread run!")

    def stop(self):
        self.terminate()
        print("stopped thread")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    file = QFile("./GUI/dark.qss")
    file.open(QFile.ReadOnly | QFile.Text)
    stream = QTextStream(file)
    app.setStyleSheet(stream.readAll())
    jedi = Jedi()
    jedi.show()
    sys.exit(app.exec())
