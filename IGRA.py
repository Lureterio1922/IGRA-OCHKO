import random
import sys

from PyQt5.QtCore import QTimer, QUrl, QSize
from PyQt5.QtGui import QPixmap
from PyQt5.QtMultimedia import QMediaPlaylist, QMediaContent, QMediaPlayer
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QLineEdit, QMessageBox
from qtpy import QtGui

music = "Выключенная музыка"
x = 420
karta4=None
khod = "Мой ход"
balansik = "Открытый баланс"
stavochka = "Открытая ставочка"
karty_dilera = []
x1 = 420
timer =None
karty_igroka=[]
karty_igroka_na_stole=[]
karty_dilera_na_stole=[]
stavka_jigroka = None
balans_igroka1=1000
player=None
def pobeda():
    global balans_igroka1
    buttonReply = QMessageBox.question(window,'PyQt5 message', "Хотите ли Вы, сударь, начать игру заново? Вам удалось победить в нашем лохотроне", QMessageBox.Yes | QMessageBox.No )
    print(int(buttonReply))
    if buttonReply == QMessageBox.Yes:
        print('Yes clicked.')
        new_game()
    if buttonReply == QMessageBox.No:
        print('No clicked.')
        sys.exit()
    stavka_jigroka=int(stavka_igroka.text())
    balans_igroka1=balans_igroka1 +(stavka_jigroka*2)
    balans_igroka.setText(str(balans_igroka1))
def porazhenie():
    buttonReply = QMessageBox.question(window,'PyQt5 message', "Хотите ли Вы, сударь, начать игру заново? К сожалению Вам не удалось выиграть в нашем лохотроне", QMessageBox.Yes | QMessageBox.No )
    print(int(buttonReply))
    if buttonReply == QMessageBox.Yes:
        print('Yes clicked.')
        new_game()
    if buttonReply == QMessageBox.No:
        print('No clicked.')
        sys.exit()

def new_game():
    global karty_dilera_na_stole
    global x
    global x1
    global khod
    global karty_igroka_na_stole
    global karty_igroka
    global nabor_kart
    global ostanovka_nabora
    for kart in karty_dilera_na_stole:
        kart.setParent(None)
    for kart in karty_igroka_na_stole:
        kart.setParent(None)


    karty_igroka_na_stole=[]
    karty_igroka=[]
    karty_dilera_na_stole=[]
    karty_dilera=[]
    x=420
    x1 = 420
    data = read_file()
    koloda = data.split("\n")  # строка из файла с картами разбивается на раздельный список
    random.shuffle(koloda)  # перемешивание наименований карт из списка
    print(koloda)
    startovaya_razdacha(koloda,window)
    print(karty_dilera)
    khod="Мой ход"
    nabor_kart.setEnabled(True)
    ostanovka_nabora.setEnabled(True)
    balans()
    global stavochka
    if stavochka=="Открытая ставочка":
        stavka_igroka.hide()
        stavochka = "Закрытая ставочка"
    else:
        stavka_igroka.show()
        stavochka = "Открытая ставочка"



def vzyat(koloda):
    global x
    global nabor_kart
    global window
    if khod=="Мой ход":
        karta5 = QLabel()
        karta5.setFixedSize(50,90)
        karta5.move(x,570)
        pixmap= getPixmap(koloda[0])
        karta5.setPixmap(pixmap)
        window.layout().addWidget(karta5)
        karty_igroka_na_stole.append(karta5)
        karty_igroka.append(koloda[0])
        koloda.pop(0)
        x = x+60


    if podschet(karty_igroka)>=21:

            print('you lose')
            nabor_kart.setEnabled(False)
            # buttonReply = QMessageBox.question(window,'PyQt5 message', "Хотите ли Вы, сударь, начать игру заново?", QMessageBox.Yes | QMessageBox.No )
            # print(int(buttonReply))
            # if buttonReply == QMessageBox.Yes:
            #     print('Yes clicked.')
            #     new_game()
            # if buttonReply == QMessageBox.No:
            #     print('No clicked.')
            #     sys.exit()
            # if buttonReply == QMessageBox.Cancel:
            #     print('Cancel')


    # app= QApplication([])
            #
            # window1 = QMainWindow()
            # window1.setFixedSize(500,500)
            #
            # window1.show()
            # app.exec()


def dop_karty():
    global x1
    global khod
    global koloda
    if khod =="Чужой ход":
        karta6 = QLabel()
        karta6.setFixedSize(50,90)
        karta6.move(x1,210)
        pixmap= getPixmap(koloda[0])
        karta6.setPixmap(pixmap)
        window.layout().addWidget(karta6)
        karty_dilera_na_stole.append(karta6)
        karty_dilera.append(koloda[0])
        koloda.pop(0)

    x1 = x1+60
    if podschet(karty_igroka)<podschet(karty_dilera) and podschet(karty_dilera)<=21:
        print('У дилера больше сумма карт')
        print(podschet(karty_dilera))
        print(podschet(karty_igroka))
        timer.stop()
        porazhenie()
    elif podschet(karty_dilera)>21 and podschet(karty_igroka)<=21:
        print('Перебор суммы карт у дилера')
        print(podschet(karty_igroka))
        print(podschet(karty_dilera))
        timer.stop()
        pobeda()
    elif podschet(karty_igroka)>21 and podschet(karty_dilera)<=21:
        print('Перебор суммы карт у игрока')
        print(podschet(karty_igroka))
        print(podschet(karty_dilera))
        timer.stop()
        sys.exit()
    elif podschet(karty_dilera)<podschet(karty_igroka) and podschet(karty_igroka)<=21:
        print('У игрока больше сумма карт')
        print(podschet(karty_igroka))
        print(podschet(karty_dilera))
        timer.stop()
        pobeda()
    elif podschet(karty_dilera)>21 and podschet(karty_igroka)>21:
        timer.stop()
        sys.exit()








def ostanovka():
    global khod
    global karta4
    global name_karta
    global timer
    global ostanovka_nabora
    pixmap=getPixmap(name_karta)
    karta4.setPixmap(pixmap)
    khod = "Чужой ход"
    nabor_kart.setEnabled(False)
    ostanovka_nabora.setEnabled(False)





    timer = QTimer()
    timer.setInterval(1500)
    timer.timeout.connect(lambda :dop_karty())
    timer.start()




def balans():
    global balansik
    if balansik == "Открытый баланс":
        balans_igroka.hide()
        balansik = "Закртый баланс"
    else:
        balans_igroka.setText(str(balans_igroka1))
        balans_igroka.show()
        balansik = "Открытый баланс"



def mousePressEvent():
    global music
    global player
    if music == "Выключенная музыка":
        player.play()
        music_play.setIcon(QtGui.QIcon('Unknown.jpeg'))
        music_play.setStyleSheet('opacity:.3')
        music_play.setIconSize(QSize(100, 100))
        window.layout().addWidget(music_play)

        music="Включенная музыка"
    else:
        player.pause()
        music="Выключенная музыка"
        music_play.setIcon(QtGui.QIcon('i.png'))
        music_play.setIconSize(QSize(100, 100))
        window.layout().addWidget(music_play)







def startovaya_razdacha(koloda,window):

    print(koloda[0])
    print(koloda[1])
    print(koloda[2])
    print(koloda[3])

    karta1=QLabel()
    karta1.setFixedSize(50, 90)
    karta1.move(300,570)
    pixmap = getPixmap(koloda[0])
    karta1.setPixmap(pixmap)
    window.layout().addWidget(karta1)
    karty_igroka.append(koloda[0])
    karty_igroka_na_stole.append(karta1)
    koloda.pop(0)

    karta2=QLabel()
    karta2.setFixedSize(50, 90)
    karta2.move(360,570)
    pixmap = getPixmap(koloda[0])
    karta2.setPixmap(pixmap)
    window.layout().addWidget(karta2)
    karty_igroka.append(koloda[0])
    karty_igroka_na_stole.append(karta2)
    koloda.pop(0)

    karta3=QLabel()
    karta3.setFixedSize(50, 90)
    karta3.move(300,210)
    pixmap = getPixmap(koloda[0])
    karta3.setPixmap(pixmap)
    window.layout().addWidget(karta3)
    karty_dilera.append(koloda[0])
    karty_dilera_na_stole.append(karta3)
    koloda.pop(0)

    global karta4
    global name_karta
    name_karta = koloda[0]
    karta4=QLabel()
    karta4.setFixedSize(50, 90)
    karta4.move(360,210)
    pixmap = QPixmap('1399413.jpg')
    karta4.setPixmap(pixmap)
    window.layout().addWidget(karta4)
    karty_dilera.append(koloda[0])
    karty_dilera_na_stole.append(karta4)
    koloda.pop(0)





def getPixmap(karta):


    result=karta.replace(' ','_').replace('черви','chervi.png').replace('буби','bubi.png').replace('крести','kresti.png').replace ('пики','piki.png')

    return QPixmap(result)






# def vzyatie_karty(koloda):
#     koloda[0]
    








def read_file():
    file = open("spisok_kart", "r")
    data = file.read()
    file.close()

    return data

def stavka():
    global stavochka
    global stavka_jigroka
    global balans_igroka1
    print("stavka")
    balans()
    if stavochka=="Открытая ставочка":
        stavka_igroka.hide()
        stavochka = "Закрытая ставочка"
    else:
        stavka_igroka.show()
        stavochka = "Открытая ставочка"
    stavka_jigroka=int(stavka_igroka.text())
    balans_igroka1=balans_igroka1-stavka_jigroka
    balans_igroka.setText(str(balans_igroka1))



def podschet(spisok_kart):

    sum = 0

    for karta in spisok_kart:
        sum += kart_value(karta)
    return sum

def kart_value(karta):

    if "2" in karta:
        return 2

    if "3" in karta:
        return 3

    if "4" in karta:
        return 4

    if "5" in karta:
        return 5

    if "6" in karta:
        return 6

    if "7" in karta:
        return 7

    if "8" in karta:
        return 8

    if "9" in karta:
        return 9

    if "10" in karta:
        return 10

    if "J" in karta:
        return 2

    if "Q" in karta:
        return 3

    if "K" in karta:
        return 4

    if "A" in karta:
        return 11






if __name__ == "__main__":
    app= QApplication([])
    window = QMainWindow()
    window.setFixedSize(800, 800)


    playlist = QMediaPlaylist()
    tracks=[
        QMediaContent(QUrl.fromLocalFile("/Users/compus/IdeaProjects/IGRA OCHKO/Intro.mp3")),
        QMediaContent(QUrl.fromLocalFile("/Users/compus/IdeaProjects/IGRA OCHKO/лали.mp3")),
        QMediaContent(QUrl.fromLocalFile("/Users/compus/IdeaProjects/IGRA OCHKO/музыка.mp3")),
        QMediaContent(QUrl.fromLocalFile("/Users/compus/IdeaProjects/IGRA OCHKO/каспий.mp3")),
        QMediaContent(QUrl.fromLocalFile("/Users/compus/IdeaProjects/IGRA OCHKO/даром.mp3")),
        QMediaContent(QUrl.fromLocalFile("/Users/compus/IdeaProjects/IGRA OCHKO/ненадо.mp3")),
        QMediaContent(QUrl.fromLocalFile("/Users/compus/IdeaProjects/IGRA OCHKO/стакан.mp3")),
        QMediaContent(QUrl.fromLocalFile("/Users/compus/IdeaProjects/IGRA OCHKO/белом.mp3")),
        QMediaContent(QUrl.fromLocalFile("/Users/compus/IdeaProjects/IGRA OCHKO/суд.mp3")),

    ]

    random.shuffle(tracks)

    for track in tracks:
        playlist.addMedia(track)


    # url=QUrl.fromLocalFile("/Users/compus/IdeaProjects/IGRA OCHKO/Intro.mp3")
    # playlist.addMedia(QMediaContent(url))
    #
    # url=QUrl.fromLocalFile("/Users/compus/IdeaProjects/IGRA OCHKO/лали.mp3")
    # playlist.addMedia(QMediaContent(url))
    #
    # url=QUrl.fromLocalFile("/Users/compus/IdeaProjects/IGRA OCHKO/музыка.mp3")
    # playlist.addMedia(QMediaContent(url))
    #
    # url=QUrl.fromLocalFile("/Users/compus/IdeaProjects/IGRA OCHKO/каспий.mp3")
    # playlist.addMedia(QMediaContent(url))
    #
    # url=QUrl.fromLocalFile("/Users/compus/IdeaProjects/IGRA OCHKO/даром.mp3")
    # playlist.addMedia(QMediaContent(url))
    #
    # url=QUrl.fromLocalFile("/Users/compus/IdeaProjects/IGRA OCHKO/ненадо.mp3")
    # playlist.addMedia(QMediaContent(url))
    #
    # url=QUrl.fromLocalFile("/Users/compus/IdeaProjects/IGRA OCHKO/стакан.mp3")
    # playlist.addMedia(QMediaContent(url))
    #
    # url=QUrl.fromLocalFile("/Users/compus/IdeaProjects/IGRA OCHKO/белом.mp3")
    # playlist.addMedia(QMediaContent(url))
    #
    # url=QUrl.fromLocalFile("/Users/compus/IdeaProjects/IGRA OCHKO/суд.mp3")
    # playlist.addMedia(QMediaContent(url))

    player=QMediaPlayer()
    player.setPlaylist(playlist)
    player.playlist().setCurrentIndex(0)
    player.play()

    data = read_file()
    koloda = data.split("\n")  # строка из файла с картами разбивается на раздельный список


    stol = QLabel()
    stol.setFixedSize(800, 800)
    stol.move(0, 0)
    pixmap=QPixmap('stol_dlya_igry.jpg')
    stol.setPixmap(pixmap)
    window.layout().addWidget(stol)

    random.shuffle(koloda)  # перемешивание наименований карт из списка
    print(koloda)
    startovaya_razdacha(koloda,window)
    print(karty_dilera)

    balans_igroka=QLabel()
    balans_igroka.setText("                     1000$")
    balans_igroka.move(300,325)
    balans_igroka.setFixedSize(200,100)
    balans_igroka.setStyleSheet("background-color:#DCDCDC")
    window.layout().addWidget(balans_igroka)


    stavka_igroka = QLineEdit()
    stavka_igroka.move(360,450)
    stavka_igroka.setFixedSize(80,50)
    stavka_igroka.setStyleSheet("background-color:#FAE7B5")
    window.layout().addWidget(stavka_igroka)
    stavka_igroka.returnPressed.connect(lambda: stavka())



    nabor_kart = QPushButton()
    nabor_kart.setText('Взять')
    nabor_kart.setFixedSize(40, 40)
    nabor_kart.move(200, 700)
    nabor_kart.setStyleSheet("background-color:#48D100")
    window.layout().addWidget(nabor_kart)
    nabor_kart.clicked.connect(lambda: vzyat(koloda))


    ostanovka_nabora = QPushButton()
    ostanovka_nabora.setText('Стоп')
    ostanovka_nabora.setFixedSize(40, 40)
    ostanovka_nabora.move(250, 700)
    ostanovka_nabora.setStyleSheet("background-color:#48D100")
    window.layout().addWidget(ostanovka_nabora)
    ostanovka_nabora.clicked.connect(lambda: ostanovka())

    okoshko_dlya_stavok = QPushButton()
    okoshko_dlya_stavok.setText('Ставка')
    okoshko_dlya_stavok.setFixedSize(50, 40)
    okoshko_dlya_stavok.move(320, 700)
    okoshko_dlya_stavok.setStyleSheet("background-color:#48D100")
    window.layout().addWidget(okoshko_dlya_stavok)

    okoshko_balansa = QPushButton()
    okoshko_balansa.setText("Баланс")
    okoshko_balansa.setFixedSize(50, 40)
    okoshko_balansa.move(380, 700)
    okoshko_balansa.setStyleSheet("background-color:#48D100")
    window.layout().addWidget(okoshko_balansa)
    okoshko_balansa.clicked.connect(lambda :balans())


    rubashka_kart = QLabel()
    rubashka_kart.setFixedSize(50, 90)
    rubashka_kart.move(150, 350)
    pixmap = QPixmap('main_50020_original.jpg')
    rubashka_kart.setPixmap(pixmap)
    window.layout().addWidget(rubashka_kart)

    otboinik_kart = QLabel()
    otboinik_kart.setFixedSize(50, 90)
    otboinik_kart.move(600, 350)
    pixmap = QPixmap('1399413.jpg')
    otboinik_kart.setPixmap(pixmap)
    window.layout().addWidget(otboinik_kart)

    new_game1 = QPushButton()
    new_game1.setText('Новая игра')
    new_game1.setFixedSize(80,40)
    new_game1.move(450,700)
    new_game1.setStyleSheet("background-color:#48D100")
    window.layout().addWidget(new_game1)
    new_game1.clicked.connect(lambda :new_game())

    music_play=QPushButton()
    music_play.move(700,0)
    music_play.setFixedSize(100,100)
    # music_play.setStyleSheet("background-color:#76A090")
    music_play.setIcon(QtGui.QIcon('Unknown.jpeg'))
    music_play.setIconSize(QSize(100, 100))
    window.layout().addWidget(music_play)
    music_play.clicked.connect(lambda:mousePressEvent())






    



    window.show()
    app.exec()
