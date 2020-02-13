from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
def start_timera(button):
    x=button.x()
    y= button.y()
    button.move(x+5,y)

if __name__ == "__main__":

    app = QApplication([])

    window = QMainWindow()
    window.setFixedSize(800,800)

    button = QPushButton()
    button.setFixedSize(100,100)
    button.move(100,200)
    window.layout().addWidget(button)


    timer = QTimer()
    timer.setInterval(10)
    timer.timeout.connect(lambda :start_timera(button))
    timer.start()




    window.show()
    app.exec()