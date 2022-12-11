from Connector import Connector
from PyQt5.QtCore import QCoreApplication, QUrl, pyqtSignal, QObject
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtQml import qmlRegisterType, QQmlComponent
from Thread import Thread
from concurrent.futures import ThreadPoolExecutor as cf
import os
from datetime import datetime
from dateutil.parser import parse
class Callback(QObject):
    def __init__(self, program):
        QObject.__init__(self)
        self.program = program
        self.engine = None
        self.connector = Connector(self.program)
        self.threads = []
        self.threadId = 0

    def ManageThread(self, id):
        for pair in self.threads:
            if pair[0] == id:
                pair[1].terminate()
                self.threads.remove(pair)
                break

    @pyqtSlot()
    def Exit(self):
        os._exit(0)

    @pyqtSlot()
    def reset_plot(self):
        self.program.figureDriver.home()

    @pyqtSlot(str)
    def change_station(self, station):
        if self.program.plot == None:
            return
        self.program.plot.clear_station()
        self.program.plot.add_station(station)
        self.program.plot.update_all()
        self.program.figureDriver.update_figure()

    @pyqtSlot(str)
    def add_station(self, station):
        if self.program.plot == None:
            return
        self.program.plot.add_station(station)
        self.program.plot.update_all()
        self.program.figureDriver.update_figure()

    @pyqtSlot(str)
    def remove_station(self, station):
        if self.program.plot == None:
            return
        self.program.plot.remove_station(station)
        self.program.plot.update_all()
        self.program.figureDriver.update_figure()

    @pyqtSlot(str, int)
    def change_plot(self, key, checked):
        self.program.plot.states[key.upper()] = checked
        self.program.plot.update(key.upper())
        self.program.plot.update_all()
        self.program.figureDriver.update_figure()

    @pyqtSlot(str)
    def add_weather(self, weather):
        if self.program.plot == None:
            return
        self.program.plot.add_weather(weather)
        self.program.plot.update_all()
        self.program.figureDriver.update_figure()

    @pyqtSlot(str)
    def remove_weather(self, weather):
        if self.program.plot == None:
            return
        self.program.plot.remove_weather(weather)
        self.program.plot.update_all()
        self.program.figureDriver.update_figure()

    @pyqtSlot(str, int)
    def change_weather_setting(self, key, checked):
        print(key, checked)

    @pyqtSlot(str)
    def update_map_button(self, buttonid):
        print(buttonid)

    @pyqtSlot()
    def update_graph(self):
        if self.program.plot == None:
            return
        self.program.plot.update_all()
        self.program.figureDriver.update_figure()
    
    @pyqtSlot(str, str)
    def set_timeline(self, start, end):
        print(start, end)
        self.program.plot.set_timeline(datetime.fromtimestamp(int(start)/1000 + 3600).strftime("%Y-%m-%d %H:%M"), datetime.fromtimestamp(int(end)/1000).strftime("%Y-%m-%d %H:%M"))
        self.program.plot.update_all()
        self.program.figureDriver.update_figure()