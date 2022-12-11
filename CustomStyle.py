from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal, QUrl, QMetaObject, Qt, Q_ENUMS, pyqtProperty

class CustomStyle(QObject):
    varChanged = pyqtSignal()
    def __init__(self, parent=None):
        super().__init__(parent)

    @pyqtProperty(str, notify=varChanged)
    def RED(self):
        return "#FF0000"

    @pyqtProperty(str, notify=varChanged)
    def BLUE(self):
        return "#0000FF"

    @pyqtProperty(str, notify=varChanged)
    def color_left_menu(self):
        return "#000000"

    @pyqtProperty(str, notify=varChanged)
    def color_background(self):
        return "#1D1D1D" 
    
    @pyqtProperty(str, notify=varChanged)
    def color_side_menu(self):
        return "#292929"
    
    @pyqtProperty(str, notify=varChanged)
    def color_icon(self):
        return "#9A9A9A"

    @pyqtProperty(str, notify=varChanged)
    def color_kerf(self):
        return "#2697FF"
    
    @pyqtProperty(str, notify=varChanged)
    def color_dark_kerf(self):
        return "#176DBC"
    
    @pyqtProperty(str, notify=varChanged)
    def color_line_break(self):
        return "#3D3D3D"