from typing import Optional
from PySide6.QtCore import *

from PySide6.QtWidgets import *
from PySide6.QtGui import *
from ui_mainwindow import Ui_MainWindow
import sys
import time
import paramiko


class SSH_Handle():
    def __init__(self) -> None:
        self.username = None
        self.passwd = None
        self.host = None
        self.client = None
        self.port = 22

    def set_username(self, username: str):
        self.username = username

    def set_passwd(self, passwd: str):
        self.passwd = passwd

    def set_host(self, host: str):
        self.host = host

    def set_port(self, port):
        self.port = port

    def get_session(self):
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            client.connect(self.host, self.port, self.username, self.passwd)
        except paramiko.ssh_exception.NoValidConnectionsError:
            return False
        return client

    def do_connect(self, state: int, arg: str | int):
        match state:
            case 1:
                self.set_username(arg)
            case 2:
                self.set_passwd(arg)
            case 3:
                self.set_host(arg)
            case 4:
                self.set_port(arg)
            case 5:
                self.client = self.get_session()
                if self.client:
                    _, stdout, stderr = self.client.exec_command(arg)
                    return _, stdout, stderr
                else:
                    return False


class ProxyNodesApp(QApplication):
    def __init__(self, args: [] = []) -> None:
        super().__init__(args)
        self.widget = Ui_MainWindow()
        self.threads = {}
        self.threads[1] = ThreadClass(parent=self, index=1)
        self.threads[1].any_signal.connect(self.ssh_command)
        self.widget.setupUi(self.widget)
        self.widget.retranslateUi(self.widget)
        with open("./proxy_list.txt", "r") as f:
            lines = f.read()
            lines = lines.split('\n')
            for line in lines:
                self.widget.ip_cmb.addItem(line)
                self.widget.next_ip_cmb.addItem(line)

        self.widget.ssh_conn.clicked.connect(self.start_ssh_worker)
        self.pressed_return = False
        self.ssh_handle = SSH_Handle()
        self.ssh_stopped = True

    def stop_ssh_service(self):
        if not self.ssh_stopped:
            self.ssh_handle.client.close()
            self.widget.ssh_conn.setText("SSH Connect")
            self.widget.text_out.setText("")
            self.widget.ssh_conn.clicked.disconnect(self.stop_ssh_service)
            self.widget.ssh_conn.clicked.connect(self.start_ssh_worker)
            self.threads[1].stop()
            self.ssh_stopped = True

    def start_ssh_worker(self):
        if self.ssh_stopped:
            self.threads[1].start()
            self.widget.ssh_conn.setText("STOP SSH")
            self.widget.ssh_conn.clicked.disconnect(self.start_ssh_worker)
            self.widget.ssh_conn.clicked.connect(self.stop_ssh_service)
            self.ssh_stopped = False

    def return_pressed(self):
        self.pressed_return = True

    def ssh_command(self, cmd: str):
        self.widget.text_in.returnPressed.connect(self.return_pressed)
        if cmd == "":
            self.widget.text_out.setText("SSH USERNAME..")
            self.widget.text_in.setText("")
        elif self.widget.text_out.toPlainText() == "SSH USERNAME.." and self.widget.text_in.text():
            self.ssh_handle.do_connect(1, self.widget.text_in.text())
            self.widget.text_out.setText("SSH PASSWORD..")
            self.widget.text_in.setText("")
        elif self.widget.text_out.toPlainText() == "SSH PASSWORD.." and self.widget.text_in.text():
            self.ssh_handle.do_connect(2, self.widget.text_in.text())
            self.ssh_handle.do_connect(3, self.widget.ip_cmb.currentText())
            self.ssh_handle.do_connect(4, int(self.widget.port_spin.value()))
            self.widget.text_in.setText("")
            self.widget.text_out.setText("CONNECT? YES/NO..")

        elif self.widget.text_out.toPlainText() == "CONNECT? YES/NO.." and self.widget.text_in.text():
            if self.widget.text_in.text().lower() == "yes":
                self.widget.text_in.setText("")
                self.widget.text_out.setText("CONNECTED\nCOMMAND TO RUN..")
            else:
                self.widget.text_out.setText("DISCONNECTED")

        elif self.widget.text_out.toPlainText() == "CONNECTED\nCOMMAND TO RUN.." and self.widget.text_in.text():
            cmd = self.widget.text_in.text()
            _, stdout, stderr = self.ssh_handle.do_connect(5, cmd)
            output = stdout.readlines() + stderr.readlines()

            if output:
                self.widget.text_out.setText(
                    ''.join(line.strip() + '\n' for line in output))
            else:
                self.widget.text_out.setText("No output..")
        else:
            _, out, err = self.ssh_handle.client.exec_command(cmd)
            output = out.readlines() + err.readlines()

            if output:
                self.widget.text_out.setText(
                    ''.join(line.strip() + '\n' for line in output))
            else:
                self.widget.text_out.setText("No output..")

    def run_app(self):
        self.widget.show()
        return self.exec()


class ThreadClass(QThread):
    any_signal = Signal(str)

    def __init__(self, parent: ProxyNodesApp = None, index=0) -> None:
        super().__init__(parent)
        self.index = index
        self.is_running = True
        self.parent_widget = parent.widget
        self.parent_app = parent

    def run(self):
        self.any_signal.emit("")
        while not self.parent_app.ssh_stopped:
            if self.parent_app.pressed_return:
                self.any_signal.emit(self.parent_widget.text_in.text())
                self.parent_app.pressed_return = False
        print("Exited Thread run!")

    def stop(self):
        self.terminate()
        print("stopped thread, ", self.index)


if __name__ == '__main__':
    app = ProxyNodesApp()

    sys.exit(app.run_app())
