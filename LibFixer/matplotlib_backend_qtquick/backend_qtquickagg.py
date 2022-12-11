import numpy as np
from matplotlib.backends.backend_agg import FigureCanvasAgg
from .backend_qtquick import (
    QtCore, QtGui, FigureCanvasQtQuick)


class FigureCanvasQtQuickAgg(FigureCanvasAgg, FigureCanvasQtQuick):

    def __init__(self, figure=None, parent=None):
        super().__init__(figure=figure, parent=parent)
        self.blitbox = None

    def paint(self, p):

        self._draw_idle()  # Only does something if a draw is pending.

        if not hasattr(self, 'renderer'):
            return

        if self.blitbox is None:

            if QtCore.QSysInfo.ByteOrder == QtCore.QSysInfo.LittleEndian:

                stringBuffer = np.asarray(self.renderer._renderer).tobytes()
            else:
                stringBuffer = self.renderer.tostring_argb()

            # convert the Agg rendered image -> qImage
            qImage = QtGui.QImage(stringBuffer, int(self.renderer.width),
                                  int(self.renderer.height),
                                  QtGui.QImage.Format_RGBA8888)
            if hasattr(qImage, 'setDevicePixelRatio'):
                # Not available on Qt4 or some older Qt5.
                qImage.setDevicePixelRatio(self.dpi_ratio)
            # get the rectangle for the image
            rect = qImage.rect()
            # p = QtGui.QPainter(self)
            # reset the image area of the canvas to be the back-ground color
            p.eraseRect(rect)
            # draw the rendered image on to the canvas
            p.drawPixmap(QtCore.QPoint(0, 0), QtGui.QPixmap.fromImage(qImage))

            # draw the zoom rectangle to the QPainter
            self._draw_rect_callback(p)

        else:
            bbox = self.blitbox
            # repaint uses logical pixels, not physical pixels like the renderer.
            l, b, w, h = [pt / self._dpi_ratio for pt in bbox.bounds]
            t = b + h
            reg = self.copy_from_bbox(bbox)
            stringBuffer = reg.to_string_argb()
            qImage = QtGui.QImage(stringBuffer, w, h,
                                  QtGui.QImage.Format_RGBA8888)

            if hasattr(qImage, 'setDevicePixelRatio'):
                # Not available on Qt4 or some older Qt5.
                qImage.setDevicePixelRatio(self.dpi_ratio)
            pixmap = QtGui.QPixmap.fromImage(qImage)

            p.drawPixmap(QtCore.QPoint(l, self.renderer.height-t), pixmap)

            # draw the zoom rectangle to the QPainter
            self._draw_rect_callback(p)

            self.blitbox = None

    def blit(self, bbox=None):
        # If bbox is None, blit the entire canvas. Otherwise
        # blit only the area defined by the bbox.
        if bbox is None and self.figure:
            bbox = self.figure.bbox

        self.blitbox = bbox
        # repaint uses logical pixels, not physical pixels like the renderer.
        l, b, w, h = [pt / self._dpi_ratio for pt in bbox.bounds]
        t = b + h
        self.repaint(l, self.renderer.height-t, w, h)

    def print_figure(self, *args, **kwargs):
        super().print_figure(*args, **kwargs)
        self.draw()


# The first one is a standard name; The second not so
FigureCanvas = FigureCanvasQtQuickAgg