from PyQt5 import QtCore, QtWidgets, QtQml
from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal, QUrl, QMetaObject, Qt

class Connector(QtCore.QObject):
    def __init__(self, program, parent=None):
        super(Connector, self).__init__(parent)
        self.program = program

    def Init(self):
        self.root = self.program.engine.rootObjects()[0]

    def get_canvas(self):
        return self.root.findChild(QtCore.QObject, "canvas")

    def get_correlation_canvas(self):
        return self.root.findChild(QtCore.QObject, "correlation_canvas")

    def check_enum(self):
        return self.root.check_enum()

    def set_switch_state(self, key, state):
        self.root.set_switch_state(key, state)

    def set_switch_position(self, key, state):
        self.root.set_switch_position(key, state)

    def get_mode(self):
        return self.root.get_mode()

    def set_button_state(self, key, state):
        self.root.set_button_state(key, state)

    def get_merge_type_combo(self):
        return self.root.get_merge_type_combo()

    def log_model_append(self, data):
        self.root.log_model_append(data)

    def log_model_clear(self):
        self.root.log_model_clear()