from PyQt5.QtCore import Qt, pyqtSignal, QObject

class ThreadEscape(QObject):
    threadSignal = pyqtSignal()
    threadSignal_with_arg = pyqtSignal(object)

    def __init__(self, func, *args):
        QObject.__init__(self)
        if args:
            self.threadSignal_with_arg.connect(func)
            self.threadSignal_with_arg.emit(*args)
        else:
            self.threadSignal.connect(func)
            self.threadSignal.emit()