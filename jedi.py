
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


def is_ipv4(addr: str):
    try:
        socket.inet_aton(addr)
        return True
    except socket.error:
        return False


class Jedi(Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.retranslateUi(self)

        self.pressed_return = False
        self.text_input.returnPressed.connect(self.pressReturnCMD)
        self.cmd_thread = CMDThread(self)
        self.cmd_thread.start()
        self.cmd_thread_running = True
        self.cmd_thread.any_signal.connect(self.enter_cmd)
        self.cmd_handler = CMDHandler()
        if os.path.isfile("./proxy_list.hosts"):
            self.cmd_handler.add_hosts(self)
        else:
            with open("./proxy_list.hosts", "w") as f:
                f.write("127.0.0.1")
            self.cmd_handler.add_hosts(self)

    def pressReturnCMD(self):
        self.pressed_return = True

    def enter_cmd(self, cmd: str):
        if cmd == "clear":
            self.out_display.clear()
            return
        val = self.cmd_handler.handle_cmd(cmd)
        if len(cmd.split(' ')) == 3:
            if cmd.split(" ")[1].lower() == "host":
                self.next_host.clear()
                self.target_host.clear()
                self.remote_host.clear()
                self.cmd_handler.add_hosts(self)
                self.out_display.append("added host" + val + "\n")
                return
        if cmd.split(' ')[0] == "cd":
            os.chdir(cmd.split(' ')[1])

        self.out_display.append(val.decode() + "\n")

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
            return str(cmd.split(" ")[2]).lower()
        except:
            return False

    def append_host(self, addr: str) -> bool:
        if is_ipv4(addr):
            with open("./proxy_list.hosts", "a") as f:
                f.write("\n" + addr)
            return True
        else:
            return False

    def add_hosts(self, wid: Jedi):
        with open("./proxy_list.hosts", "r") as f:
            lines = f.read()
            lines = lines.split('\n')
            for line in lines:
                wid.remote_host.addItem(line)
                wid.next_host.addItem(line)


class CMDThread(QThread):
    any_signal = Signal(str)

    def __init__(self, parent: Jedi = None) -> None:
        super().__init__(parent)
        self.jedi = parent

    def run(self):
        while self.jedi.cmd_thread_running:
            if self.jedi.pressed_return:
                self.any_signal.emit(self.jedi.text_input.text())
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
