import random

from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton


def read_file():
    file = open("spisok_kart", "r")
    data = file.read()
    file.close()

    return data


if __name__ == "__main__":
    data = read_file()
    koloda = data.split("\n")  #строка из файла с картами разбивается на раздельный список

    random.shuffle(koloda)  #перемешивание наименований карт из списка
    print(koloda)



    app = QApplication([])

    window = QMainWindow()
    window.setFixedSize(800,800)

    stol = QLabel()
    stol.setFixedSize(600,600)
    stol.move(100,100)
    stol.setStyleSheet("background-color:#48D1CC")
    window.layout().addWidget(stol)

    nabor_kart = QPushButton()
    nabor_kart.setFixedSize(20,20)
    nabor_kart.move(200,700)
    nabor_kart.setStyleSheet("background-color:#48D100")
    window.layout().addWidget(nabor_kart)






    window.show()
    app.exec()
