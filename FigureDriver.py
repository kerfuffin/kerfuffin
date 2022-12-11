from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtQuick import QQuickView
from PyQt5.QtCore import QMetaObject, QUrl, pyqtSignal, pyqtSlot, QObject, Qt
from PyQt5.QtQml import QQmlApplicationEngine
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar2QtQuick
import numpy as np


class FigureDriver(QtCore.QObject):
    coordinatesChanged = QtCore.Signal(str)

    def __init__(self, app, parent=None):
        super().__init__(parent)
        self.app = app
        self.figure = None
        self.toolbar = None
        self._coordinates = ""
        
    def createToolbar(self, canvas, app):
        self.toolbar = NavigationToolbar2QtQuick(canvas=canvas, parent=None)

    def updateWithCanvas(self, canvas, app):
        
        self.axes = app.plot.axes
        app.plot.plot()
        canvas.draw_idle()

        canvas.figure.canvas.mpl_connect('motion_notify_event', self.on_motion)

    def getCoordinates(self):
        return self._coordinates
    
    def setCoordinates(self, coordinates):
        self._coordinates = coordinates
        self.coordinatesChanged.emit(self._coordinates)
    
    coordinates = QtCore.Property(str, getCoordinates, setCoordinates,
                                  notify=coordinatesChanged)

    def zoom(self, *args):
        self.toolbar.zoom(*args)

    def home(self, *args):
        self.toolbar.home(*args)

    def clear(self, *args):
        self.toolbar.clear(*args)

    def on_motion(self, event):
        """
        Update the coordinates on the display
        """
        if event.inaxes == self.axes:
            self.coordinates = f"({event.xdata:.2f}, {event.ydata:.2f})"

    def update_figure(self):
        self.home()
        self.updateWithCanvas(self.app.callback.connector.get_canvas(), self.app)
        self.clear()