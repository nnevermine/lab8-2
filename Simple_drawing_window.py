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
        self.button.move(160, 260)
        self.button.clicked.connect(self.clear_points)

    def clear_points(self):
        self.points.clear()

    def mouseMoveEvent(self, event):
        self.points.append(event.pos())


def main():
    app = QApplication(sys.argv)

    w = Simple_drawing_window()
    w.show()

    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())

    