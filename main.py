# This Python file uses the following encoding: utf-8
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtCore import QResource


code = ("Burning Coder")
app = QApplication([])
engine = QQmlApplicationEngine()
QResource.registerResource("library.rcc")
engine.load('qrc:///ui')
engine.rootContext().setContextProperty('code', code)
engine.quit.connect(app.quit)
sys.exit(app.exec_())
