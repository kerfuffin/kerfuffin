from PyQt5.QtCore import *

class ThreadSignals(QObject):
    threadSignal = pyqtSignal(object)
    quitSignal = pyqtSignal(object)