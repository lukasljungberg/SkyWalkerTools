from ui_mainwindow import Ui_MainWindow
import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

import threading
import subprocess
import time


class Master(QObject):

    command = Signal(str)

    def __init__(self):
        super().__init__()


class Worker(QObject):

    def __init__(self):
        super().__init__()

    def do_something(self, text):

        print('in thread {} message {}'.format(
            QThread.currentThread(), text))


def handle_input(input: str, widget: Ui_MainWindow):
    proc = subprocess.Popen(input.split(
        ' '), stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    output, err = proc.communicate()
    print(output, err)
    if err:
        widget.text_out.setText(err.decode())
    else:
        widget.text_out.setText(output.decode())
    widget.text_in.setText("")


def start_threads(widget: Ui_MainWindow):

    thread = QThread()
    thread.start()

    # create a worker and move it to our extra thread
    worker = Worker()
    worker.moveToThread(thread)

    # create a master object and connect it to the worker
    master = Master()
    master.command.connect(worker.do_something)

    # call a method of the worker directly (will be executed in the actual thread)
    widget.text_in.returnPressed.connect(
        lambda: worker.do_something('in main thread'))

    # communicate via signals, will execute the method now in the extra thread
    master.command.emit('in worker thread')


if __name__ == '__main__':
    app = QApplication([])
    widget = Ui_MainWindow()
    widget.setupUi(widget)
    widget.retranslateUi(widget)
    start_threads(widget)
    widget.show()
    sys.exit(app.exec())
