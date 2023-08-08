
# This Python file uses the following encoding: utf-8
from typing import Optional
import PySide6.QtCore
from ui_mainwindow import Ui_MainWindow
import sys
from pathlib import Path
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
import random
import time
import threading
import os
import subprocess
import asyncio
# Subclass QMainWindow to customize your application's main window
import multiprocessing.pool
import functools
import paramiko
import socket


def run(widget):
    widget.text_out.setText("Type in username..")
    entered_text = False
    # def set_entered(self):
    #    self.entered_text = True
    while not entered_text:
        pass
    username = widget.text_in.text()
    print(username)
    return
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(self.ipv4, port=self.port,
                   username=username, password=passwd)

    ssh_session = client.get_transport().open_session()
    if ssh_session.active:
        ssh_session.send(self.command)


def connect_(ipv4: str, port: int, out_board: QTextBrowser, command: str = ""):
    username = input("Username")
    print(username)
    return
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ipv4, port=port, username=username, password=passwd)

    ssh_session = client.get_transport().open_session()
    if ssh_session.active:
        ssh_session.send(command)


def _excec_command(command_arr: list, out_board: QTextBrowser):

    proc = subprocess.Popen(
        command_arr, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    out, err = proc.communicate()
    if err:
        out_board.setText(err.decode())
    else:
        out_board.setText(out.decode())
    errcode = proc.returncode


def _ping(host):
    proc = subprocess.Popen(['ping', '-c', '1', host])
    time.sleep(1)
    if proc.poll() is None:
        proc.kill()
        return f"Host {host} is unreachable! :("
    else:
        return f"Host {host} is reachable! :)"


def add_tab(w: Ui_MainWindow):
    wid = Ui_MainWindow()
    wid.setupUi(wid)
    wid.retranslateUi(wid)
    w.tabWidget.insertTab(w.tabWidget.currentIndex(),
                          wid.tab, w.enter_tab_name.text())
    w.enter_tab_name.setText("")


def main():

    widget = Ui_MainWindow()
    widget.setupUi(widget)
    widget.retranslateUi(widget)

    with open("./proxy_list.txt", "r") as f:
        lines = f.read()
        lines = lines.split('\n')
        for line in lines:
            widget.ip_cmb.addItem(line)
            widget.next_ip_cmb.addItem(line)

    widget.enter_tab_name.returnPressed.connect(
        lambda: add_tab(widget))
    widget.ping_btn.clicked.connect(lambda: widget.text_out.setText(_ping(
        widget.ip_cmb.currentText())))
    widget.text_in.returnPressed.connect(
        lambda: _excec_command(widget.text_in.text().split(' '), widget.text_out))
    thread_pool = QThreadPool()
    w = ConnectWorker(widget.ip_cmb.currentText(), 22, widget)
    widget.ssh_conn.clicked.connect(lambda: run(widget))
    widget.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    main()
