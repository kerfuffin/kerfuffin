from re import search
from PyQt5.QtCore import *
from Thread import Thread
from ThreadSignals import ThreadSignals

class ThreadCallback(QRunnable):
    def __init__(self, args: list, id: int) -> None:
        QRunnable.__init__(self)
        self.func = args[0]
        self.id = id
        self.signals = ThreadSignals()
        if len(args) > 1:
            self.args = args[1]
        else:
            self.args = []

    def run(self):
        self.Run()

    def Run(self):
        if self.args != []:
            r = self.func(self.args, self.signals.threadSignal)
        else:
            r = self.func(self.signals.threadSignal)
        self.signals.quitSignal.emit(self.id)

    def throw(self):
        self.wait()
        self.terminate()
        self.deleteLater()