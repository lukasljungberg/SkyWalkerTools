import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from app import Jedi

if __name__ == '__main__':
    app = QApplication(sys.argv)
    file = QFile("./GUI/dark.qss")
    file.open(QFile.ReadOnly | QFile.Text)
    stream = QTextStream(file)
    app.setStyleSheet(stream.readAll())
    jedi = Jedi()
    jedi.show()
    sys.exit(app.exec())
