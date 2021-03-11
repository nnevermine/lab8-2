import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *



class Simple_drawing_window(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Drawing")
        self.points = []

        self.resize(400, 300)

        self.label = QLabel(self)
        self.label.setText("Drag mouse to draw")
        self.label.move(140, 240)

        self.button = QPushButton(self)
        self.button.setText("Clear")
        self.button.move(140, 280)
        self.button.clicked.connect(self.clear_points)

    