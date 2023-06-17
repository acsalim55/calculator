from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

app = QApplication([])
main_win = QWidget()

main_win.setWindowTitle("Python Application")
main_win.resize(800, 500)

def power(x, y):
    pass

def sin(x):
    pass

def pytag(x, y):
    pass

box = QVBoxLayout()
box.addWidget(QWidget, alignment=Qt.AlignCenter) # Add widget to window

main_win.setLayout(box)
main_win.show()
app.exec_()