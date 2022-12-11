from PyQt5.QtWidgets import *
from PyQt5.QtQml import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QGuiApplication
import sys, os
from Loader import Loader

def main():
    app = QApplication(sys.argv)
    os.environ["QT_QUICK_CONTROLS_STYLE"] = "Material"
    l = Loader()
    l.fix_libs()
    from Program import Program
    p = Program(app)
 
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()