from PyQt5 import QtWidgets, QtCore
from PyQt5.Qt import *

StyleSheet = '''
QPushButton {
    border: 3px solid black; 
    background-color: #00ccff;
}

QPushButton:hover {
    background-color: lightblue;
}

QPushButton:pressed {
    background-color: gray;
}

QLabel {
    border: 1px solid black; 
    border-radius: 5px; 
    background-color: silver;
}
'''

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()

        """
        Definiowanie GUI - okno -> buttony + labelki
        """
        self.setObjectName("MainWindow")
        self.setGeometry(0, 0, 1100, 600)
        self.setFixedSize(1100, 600)
        self.setWindowTitle("Symulator automatu biletowego")
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)

        self.labelShowMainText = QtWidgets.QLabel(self)
        self.labelShowMainText.setGeometry(QtCore.QRect(50, 40, 691, 101))
        self.labelShowMainText.setObjectName("labelShowMainText")
        self.labelShowMainText.setAlignment(Qt.AlignCenter)
        self.labelShowMainText.setText('WYBIERZ RODZAJ BILETU')

        self.labelShowPrice = QtWidgets.QLabel('label', self)
        self.labelShowPrice.setGeometry(QtCore.QRect(850, 40, 221, 101))
        self.labelShowPrice.setObjectName("label_2")
        self.labelShowPrice.setAlignment(Qt.AlignCenter)
        self.labelShowPrice.setText('Wyświetlenie wrzuconej kwoty')


        self.buttonLeftDown = QtWidgets.QPushButton('button', self)
        self.buttonLeftDown.setGeometry(QtCore.QRect(40, 400, 291, 161))
        self.buttonLeftDown.setObjectName("button_1")
        self.buttonLeftDown.setText('English')
        self.buttonLeftDown.setProperty("LANG", "1")

        self.buttonLeftUpper = QtWidgets.QPushButton('button', self)
        self.buttonLeftUpper.setGeometry(QtCore.QRect(40, 180, 291, 151))
        self.buttonLeftUpper.setObjectName("button_2")
        self.buttonLeftUpper.setText('Bilety ulgowe')
        self.buttonLeftUpper.setProperty("Counter", "0")

        self.buttonRightUpper = QtWidgets.QPushButton('button', self)
        self.buttonRightUpper.setGeometry(QtCore.QRect(460, 180, 301, 151))
        self.buttonRightUpper.setText('Bilety normalne')
        self.buttonRightUpper.setObjectName("button_3")
        self.buttonRightUpper.setProperty("Counter", "0")

        self.buttonRightDown = QtWidgets.QPushButton('button', self)
        self.buttonRightDown.setGeometry(QtCore.QRect(460, 400, 301, 161))
        self.buttonRightDown.setObjectName("button_3")
        self.buttonRightDown.setText('Wyjscie')

        self.button20gr = QtWidgets.QPushButton('button', self)
        self.button20gr.setGeometry(QtCore.QRect(840, 180, 111, 41))
        self.button20gr.setObjectName("pushButton_5")
        self.button20gr.setText('20 gr')

        self.button50gr = QtWidgets.QPushButton('button', self)
        self.button50gr.setGeometry(QtCore.QRect(840, 250, 111, 41))
        self.button50gr.setObjectName("pushButton_6")
        self.button50gr.setText('50 gr')

        self.button1zl = QtWidgets.QPushButton('button', self)
        self.button1zl.setGeometry(QtCore.QRect(840, 320, 111, 41))
        self.button1zl.setObjectName("pushButton_7")
        self.button1zl.setText('1 zł')

        self.button2zl = QtWidgets.QPushButton('button', self)
        self.button2zl.setGeometry(QtCore.QRect(840, 390, 111, 41))
        self.button2zl.setObjectName("pushButton_8")
        self.button2zl.setText('2 zł')

        self.button5zl = QtWidgets.QPushButton('button', self)
        self.button5zl.setGeometry(QtCore.QRect(840, 460, 111, 41))
        self.button5zl.setObjectName("pushButton_9")
        self.button5zl.setText('5 zł')

        self.button10zl = QtWidgets.QPushButton('button', self)
        self.button10zl.setGeometry(QtCore.QRect(960, 180, 111, 41))
        self.button10zl.setObjectName("pushButton_13")
        self.button10zl.setText('10 zł')

        self.button20zl = QtWidgets.QPushButton('button', self)
        self.button20zl.setGeometry(QtCore.QRect(960, 250, 111, 41))
        self.button20zl.setObjectName("pushButton_14")
        self.button20zl.setText('20 zł')

        self.button50zl = QtWidgets.QPushButton('button', self)
        self.button50zl.setGeometry(QtCore.QRect(960, 320, 111, 41))
        self.button50zl.setObjectName("pushButton_15")
        self.button50zl.setText('50 zł')

        self.button100zl = QtWidgets.QPushButton('button', self)
        self.button100zl.setGeometry(QtCore.QRect(960, 390, 111, 41))
        self.button100zl.setObjectName("pushButton_16")
        self.button100zl.setText('100 zł')

        self.button200zl = QtWidgets.QPushButton('button', self)
        self.button200zl.setGeometry(QtCore.QRect(960, 460, 111, 41))
        self.button200zl.setObjectName("pushButton_17")
        self.button200zl.setText('200 zł')



"""
class UITwins(object):
    TicketsNormal = 0
    TicketsReduced = 0

    def onClickLanguage(self, MainWindow):
        if(UITwins.TicketsNormal == 0 & UITwins.TicketsReduced == 0):

            if(self.buttonLeftDown.property("LANG") == "1"):

                self.buttonLeftDown.setText("Polski")
                self.buttonLeftDown.setProperty("LANG", "0")
                self.buttonLeftUpper.setText("Reduced tickets")
                self.buttonRightUpper.setText("Normal tickets")
                self.buttonRightDown.setText("EXIT")
                self.labelShowMainText.setText("CHOOSE TICKETS TYPE")
                self.labelShowPrice.setText('Wyświetlenie wrzuconej kwoty')



            elif(self.buttonLeftDown.property("LANG") == "0"):

                self.buttonLeftDown.setText("English")
                self.buttonLeftDown.setProperty("LANG", "1")
                self.buttonLeftUpper.setText("Bilety ulgowe")
                self.buttonRightUpper.setText("Normalne bilety")
                self.labelShowMainText.setText("WYBIERZ RODZAJ BILETU")
                self.labelShowPrice.setText('Wyświetlenie wrzuconej kwoty')

        else:
            if(self.buttonLeftDown.property("LANG") == "1"):
                self.buttonLeftDown.setText("Polski")
                self.buttonLeftDown.setProperty("LANG", "0")
                self.buttonLeftUpper.setText("Reduced tickets")
                self.buttonRightUpper.setText("Normal tickets")
                self.buttonRightDown.setText("EXIT")
                self.labelShowMainText.setText('You have choosen ' + str(UITwins.TicketsNormal) + "  normal tickets" + " and " + str(
                UITwins.TicketsReduced) + " reduced.")
                self.labelShowPrice.setText('Wyświetlenie wrzuconej kwoty')

            elif(self.buttonLeftDown.property("LANG") == "0"):

                self.buttonLeftDown.setText("English")
                self.buttonLeftDown.setProperty("LANG", "1")
                self.buttonLeftUpper.setText("Bilety ulgowe")
                self.buttonRightUpper.setText("Normalne bilety")
                self.buttonRightDown.setText("WYJDŹ")
                self.labelShowMainText.setText('Wybrano ' + str(UITwins.TicketsNormal) + "  biletow normalnych" + " oraz " + str(
                UITwins.TicketsReduced) + " ulgowych.")
                self.labelShowPrice.setText('Wyświetlenie wrzuconej kwoty')


    def onClickAddTicketNormal(self):
        self.ticketCounter(1)

    def onClickAddTicketReduced(self):
        self.ticketCounter(2)

    def bah(cls):
        print(str(cls.TicketsNormal))

    def ticketCounter(self, typ):
        if(typ == 1):
            UITwins.TicketsNormal += 1
        elif(typ == 2):
            UITwins.TicketsReduced += 1
        if(self.buttonLeftDown.property("LANG") == "1"):
            self.labelShowMainText.setText('Wybrano ' + str(UITwins.TicketsNormal) + "  biletow normalnych" + " oraz " + str(
            UITwins.TicketsReduced) + " ulgowych.")
        elif(self.buttonLeftDown.property("LANG") == "0"):
            self.labelShowMainText.setText('You have choosen ' + str(UITwins.TicketsNormal) + "  normal tickets" + " and " + str(
            UITwins.TicketsReduced) + " reduced.")
"""