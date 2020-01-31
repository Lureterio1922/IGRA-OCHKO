import random

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QLayout

def startovaya_razdacha(koloda,window):

    print(koloda[0])
    print(koloda[1])
    print(koloda[2])
    print(koloda[3])

    karta1=QLabel()
    karta1.setFixedSize(50, 90)
    karta1.move(300,600)
    pixmap = getPixmap(koloda[0])
    karta1.setPixmap(pixmap)
    window.layout().addWidget(karta1)

    karta2=QLabel()
    karta2.setFixedSize(50, 90)
    karta2.move(360,600)
    pixmap = getPixmap(koloda[1])
    karta2.setPixmap(pixmap)
    window.layout().addWidget(karta2)

    karta3=QLabel()
    karta3.setFixedSize(50, 90)
    karta3.move(300,100)
    pixmap = getPixmap(koloda[2])
    karta3.setPixmap(pixmap)
    window.layout().addWidget(karta3)

    karta4=QLabel()
    karta4.setFixedSize(50, 90)
    karta4.move(360,100)
    pixmap = QPixmap('1399413.jpg')
    karta4.setPixmap(pixmap)
    window.layout().addWidget(karta4)




def getPixmap(karta):


    result=karta.replace(' ','_').replace('черви','chervi.png')
    print(result)
    # result="2_chervi.png"
    return QPixmap(result)














def read_file():
    file = open("spisok_kart", "r")
    data = file.read()
    file.close()

    return data


if __name__ == "__main__":
    app= QApplication([])

    window = QMainWindow()
    window.setFixedSize(800, 800)

    data = read_file()
    koloda = data.split("\n")  # строка из файла с картами разбивается на раздельный список


    stol = QLabel()
    stol.setFixedSize(600, 600)
    stol.move(100, 100)
    stol.setStyleSheet("background-color:#48D1CC")
    window.layout().addWidget(stol)

    random.shuffle(koloda)  # перемешивание наименований карт из списка
    print(koloda)
    startovaya_razdacha(koloda,window)





    nabor_kart = QPushButton()
    nabor_kart.setText('Взять')
    nabor_kart.setFixedSize(40, 40)
    nabor_kart.move(200, 700)
    nabor_kart.setStyleSheet("background-color:#48D100")
    window.layout().addWidget(nabor_kart)

    ostanovka_nabora = QPushButton()
    ostanovka_nabora.setText('Стоп')
    ostanovka_nabora.setFixedSize(40, 40)
    ostanovka_nabora.move(250, 700)
    ostanovka_nabora.setStyleSheet("background-color:#48D100")
    window.layout().addWidget(ostanovka_nabora)

    okoshko_dlya_stavok = QPushButton()
    okoshko_dlya_stavok.setText('Ставка')
    okoshko_dlya_stavok.setFixedSize(50, 20)
    okoshko_dlya_stavok.move(300, 700)
    okoshko_dlya_stavok.setStyleSheet("background-color:#48D100")
    window.layout().addWidget(okoshko_dlya_stavok)

    okoshko_balansa = QPushButton()
    okoshko_balansa.setText("баланс")
    okoshko_balansa.setFixedSize(50, 30)
    okoshko_balansa.move(380, 700)
    okoshko_balansa.setStyleSheet("background-color:#48D100")
    window.layout().addWidget(okoshko_balansa)

    rubashka_kart = QLabel()
    rubashka_kart.setFixedSize(50, 90)
    rubashka_kart.move(150, 300)
    pixmap = QPixmap('main_50020_original.jpg')
    rubashka_kart.setPixmap(pixmap)
    window.layout().addWidget(rubashka_kart)

    otboinik_kart = QLabel()
    otboinik_kart.setFixedSize(50, 90)
    otboinik_kart.move(600, 300)
    pixmap = QPixmap('1399413.jpg')
    otboinik_kart.setPixmap(pixmap)
    window.layout().addWidget(otboinik_kart)

    window.show()
    app.exec()
