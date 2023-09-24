
# pyside6-uic ./GUI/graphics.ui -o jedi_ui.py
from typing import Optional
from PySide6.QtCore import *
import PySide6.QtCore
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from jedi_ui import Ui_MainWindow
import time
import os
import paramiko
import handlers
import workers


class KeyPressFilter(QObject):

    def __init__(self, func, parent: QObject | None = ...) -> None:
        super().__init__(parent)
        self.fn = func
        self.parent = parent

    def eventFilter(self, widget, event: QEvent):
        if event.type() == QEvent.KeyRelease:
            self.parent.input_password += event.text()
            self.fn()
        return False


class Jedi(Ui_MainWindow):
    emitted_ssh_cmd = Signal(str)

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.init_ui()

    def init_ui(self):
        self.pressed_return = False
        self.text_input.returnPressed.connect(self.pressReturnCMD)
        self.ignite_ls.clicked.connect(self.ignite_ligntsaber)
        self.ssh_proto.pressed.connect(self.ssh_init)
        self.cmd_thread = workers.CMDThread(self)
        self.cmd_thread.start()
        self.cmd_thread_running = True
        self.cmd_thread.any_signal.connect(self.enter_cmd)
        self.cmd_handler = handlers.CMDHandler()
        self.input_password = ""
        self.ssh_connection = None
        self.ssh_client = {}
        self.scp_client = {}
        self.scp_pp_init.clicked.connect(self.init_pp_brute)
        self.init_hosts_file()

    def init_hosts_file(self):
        if os.path.isfile("./proxy_list.hosts"):
            self.cmd_handler.add_hosts(self)
        else:
            with open("./proxy_list.hosts", "w") as f:
                f.write("127.0.0.1")
            self.cmd_handler.add_hosts(self)

    def init_pp_brute(self, cmd):
        self.cmd_thread.init_counter()
        try:
            self.cmd_thread.any_signal.disconnect(self.enter_cmd)
            self.cmd_thread.any_signal.disconnect(self.ssh_)
        except:
            pass
        self.out_display.setText("[***] SCP PING + PONG brute [***]")
        self.output("Enter target username: ...")
        self.cmd_thread.any_signal.connect(self.init_pp_brute)
        if cmd:
            cmd = eval(cmd)
            counter = cmd[1]
            cmd = cmd[0]
            if counter == 1:
                self.scp_client["hostname"] = self.remote_host.currentText()
                self.output("Enter password...")
                self.text_input.eventFilter = KeyPressFilter(
                    parent=self, func=self.type_password)

                self.text_input.installEventFilter(self.text_input.eventFilter)
                self.text_input.returnPressed.connect(self.exit_type_password)
                self.scp_client["username"] = cmd

    # TODO: fix this
    def type_password(self):
        txt = self.text_input.text()
        stars = ''.join(['*' for i in range(len(txt))])
        self.text_input.setText(''.join(stars))

    def exit_type_password(self):
        self.text_input.removeEventFilter(self.text_input.eventFilter)
        self.text_input.eventFilter = None
        self.input_password = ""
        self.text_input.returnPressed.connect(self.exit_type_password)

    def start_ssh(self):
        self.ssh_thread = workers.SSHThread(self.remote_host.currentText(),
                                            self.remote_port.value(),
                                            self.ssh_client['username'],
                                            self.ssh_client['password'])
        self.emitted_ssh_cmd.connect(self.ssh_thread.run)
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

    def ignite_ligntsaber(self):
        self.ssh_thread.ignite_ligntsaber("lightsaber.py", "lightsaber.py")
        self.ignite_ls.setText("Shutdown lightsaber")
        self.ignite_ls.clicked.connect(self.shutdown_lightsaber)

    def shutdown_lightsaber(self):
        hosts = [self.remote_host.itemText(i)
                 for i in range(self.remote_host.count())]
        self.ssh_thread.shutdown_ligntsaber(hosts)
        self.ignite_ls.setText("Ignite lightsaber")
        self.ignite_ls.clicked.connect(self.ignite_ligntsaber)

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
            except paramiko.AuthenticationException:
                self.output("Connection failed!\nWrong credentials.")
                self.ssh_thread.finished_signal.connect(self.output)
                try:
                    self.cmd_thread.any_signal.disconnect(self.running_ssh)
                except:
                    pass
                self.cmd_thread.any_signal.connect(self.enter_cmd)
                return

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
