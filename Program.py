import os
from PyQt5.QtCore import QMetaObject, QUrl, pyqtSignal, pyqtSlot, QObject, Qt
from PyQt5.QtQml import QQmlApplicationEngine, QQmlComponent
from PyQt5 import QtQml
from Callback import Callback
from matplotlib_backend_qtquick.backend_qtquick import NavigationToolbar2QtQuick
from matplotlib_backend_qtquick.backend_qtquickagg import FigureCanvasQtQuickAgg
from matplotlib.figure import Figure
from FigureDriver import FigureDriver
from Plot import Plot
from ThreadWrapper import ThreadWrapper as tw
from CustomStyle import CustomStyle
import sys
import json
import time

class Program(tw):
    def __init__(self, app):
        super().__init__()
        self.engine = None
        self.app = app
        self.fullPath = os.path.dirname(os.path.realpath(__file__))
        self.callback = Callback(self)
        self.figureDriver = None
        self.data = None
        self.weather_data = None
        self.plot = None
        self.Initialize()
        if self.engine != None: self.Run()
        

    def Initialize(self):
        self.engine = QQmlApplicationEngine()
        ctx = self.engine.rootContext()
        ctx.setContextProperty('figureDriver', self.figureDriver)
        ctx.setContextProperty('callback', self.callback)
        ctx.setContextProperty('connector', self.callback.connector)
        QtQml.qmlRegisterType(FigureCanvasQtQuickAgg, 'Backend', 1, 0, 'FigureCanvas')
        QtQml.qmlRegisterType(CustomStyle, 'CustomStyle', 1, 0, 'CustomStyle')
        self.engine.load("main.qml")
        self.callback.connector.Init()

        self.figureDriver = FigureDriver(self)
        self.correlationDriver = FigureDriver(self)
        self.plot = Plot(self)

        

    def Run(self):
        self.load_data()
        self.load_weather_data()
        
        # YYYY-MM-DD HH:MM
        self.plot.set_timeline("2021-01-01 01:00", "2021-03-15 00:00")
        self.figureDriver.createToolbar(self.callback.connector.get_canvas(), self)
        self.figureDriver.updateWithCanvas(self.callback.connector.get_canvas(), self)
        self.figureDriver.zoom()

        self.callback.connector.check_enum()
        #self.figureDriver.updateWithCanvas(self.callback.connector.get_canvas())

    def load_data(self):
        with open(self.fullPath + "/data.json") as f:
            data = json.load(f)
        self.data = data

    def load_weather_data(self):
        with open(self.fullPath + "/weather.json") as f:
            data = json.load(f)
        self.weather_data = data