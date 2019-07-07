#!/usr/bin/env python

import sys

from PyQt5 import Qt
from PyQt5.uic import loadUi

# [ms]
TICK_TIME = 2**6

class StopWatch(Qt.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = loadUi("gui.ui", self) #memanggil gui
        self.reset.clicked.connect(self.do_reset) 
        self.start.clicked.connect(self.do_start)
        self.Stop.clicked.connect(self.do_pause)
        self.Lap.clicked.connect(self.do_set)

        self.timer = Qt.QTimer()
        self.timer.setInterval(TICK_TIME)
        self.timer.timeout.connect(self.tick)

        self.do_reset()

        self.i = "%d:%05.2f" % (self.time // 60, self.time % 60) #tampilan timer
        self.lcd.display(self.i)

    def keyPressEvent(self, event):
        if event.key() == Qt.Qt.Key_Escape:
            self.close()
        else:
            super().keyPressEvent(event)

    def display(self):
        self.lcd.display("%d:%05.2f" % (self.time // 60, self.time % 60))

    @Qt.pyqtSlot() #parameter
    def tick(self):
        self.time += TICK_TIME/1000
        self.display()

    @Qt.pyqtSlot()
    def do_start(self):
        self.timer.start()


    @Qt.pyqtSlot()
    def do_pause(self):
        self.timer.stop()


    @Qt.pyqtSlot()
    def do_reset(self):
        self.time = 0
        self.display()

    @Qt.pyqtSlot()
    def do_set(self):
        k = 0
        k = k+1
        c = self.lineEdit.text() #mengambil isi lineedit
        f = "%d:%05.2f" % (self.time // 60, self.time % 60) #
        A = c +" : "+ f #nampilin nama dan waktu
        self.listWidget.insertItem(k, str(A)) #ngeset ke list widdget

app = Qt.QApplication(sys.argv)

watch = StopWatch()
watch.show()

app.exec_()
