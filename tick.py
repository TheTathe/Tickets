import sys
import model as m
import widok as v
from PyQt5 import QtWidgets, QtCore, QtGui
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


maszyna = m.Machine()


def onclick(args):
    if args == 1:
        maszyna.addMoney(1)

class UITwins(object):
    TicketsNormal = 0
    TicketsReduced = 0

    def setupUI(self, MainWindow):


        MainWindow.setGeometry(0, 0, 800, 600)
        MainWindow.setFixedSize(800, 600)
        MainWindow.setWindowTitle("Symulator automatu biletowego")
        self.centralwidget = QWidget(MainWindow)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 40, 691, 101))
        self.label.setObjectName("label")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setText('WYBIERZ RODZAJ BILETU')

        self.LAN_BUTTON = QtWidgets.QPushButton(self.centralwidget)
        self.LAN_BUTTON.setGeometry(QtCore.QRect(40, 400, 291, 161))
        self.LAN_BUTTON.setObjectName("button_1")
        self.LAN_BUTTON.setText('English')
        self.LAN_BUTTON.setProperty("LANG", "1")
        self.LAN_BUTTON.clicked.connect(self.onClickLanguage)


        self.ULG_BUTTON = QtWidgets.QPushButton(self.centralwidget)
        self.ULG_BUTTON.setGeometry(QtCore.QRect(40, 180, 291, 151))
        self.ULG_BUTTON.setObjectName("button_2")
        self.ULG_BUTTON.setText('Bilety ulgowe')
        self.ULG_BUTTON.setProperty("Counter", "0")
        self.ULG_BUTTON.clicked.connect(self.onClickAddTicketReduced)

        self.NOR_BUTTON = QtWidgets.QPushButton(self.centralwidget)
        self.NOR_BUTTON.setGeometry(QtCore.QRect(460, 180, 301, 151))
        self.NOR_BUTTON.setText('Bilety normalne')
        self.NOR_BUTTON.setObjectName("button_3")
        self.NOR_BUTTON.setProperty("Counter", "0")
        self.NOR_BUTTON.clicked.connect(self.onClickAddTicketNormal)





        self.EXIT_BUTTON = QtWidgets.QPushButton(self.centralwidget)
        self.EXIT_BUTTON.setGeometry(QtCore.QRect(460, 400, 301, 161))
        self.EXIT_BUTTON.setObjectName("button_3")
        self.EXIT_BUTTON.setText('Wyjscie')
        #self.EXIT_BUTTON.clicked.connect(self.onClickExit)
        self.EXIT_BUTTON.clicked.connect(lambda: onclick(1))
        MainWindow.setCentralWidget(self.centralwidget)



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
        if(self.LAN_BUTTON.property("LANG") == "1"):
            self.label.setText('Wybrano ' + str(UITwins.TicketsNormal) + "  biletow normalnych" + " oraz " + str(
            UITwins.TicketsReduced) + " ulgowych.")
        elif(self.LAN_BUTTON.property("LANG") == "0"):
            self.label.setText('You have choosen ' + str(UITwins.TicketsNormal) + "  normal tickets" + " and " + str(
            UITwins.TicketsReduced) + " reduced.")

    def onClickLanguage(self, MainWindow):
        if(UITwins.TicketsNormal == 0 & UITwins.TicketsReduced == 0):
            if(self.LAN_BUTTON.property("LANG") == "1"):
                self.LAN_BUTTON.setText("Polski")
                self.LAN_BUTTON.setProperty("LANG", "0")
                self.ULG_BUTTON.setText("Reduced tickets")
                self.NOR_BUTTON.setText("Normal tickets")
                self.EXIT_BUTTON.setText("EXIT")
                self.label.setText("CHOOSE TICKETS TYPE")
            elif(self.LAN_BUTTON.property("LANG") == "0"):
                self.LAN_BUTTON.setText("English")
                self.LAN_BUTTON.setProperty("LANG", "1")
                self.ULG_BUTTON.setText("Bilety ulgowe")
                self.NOR_BUTTON.setText("Normalne bilety")
                self.label.setText("WYBIERZ RODZAJ BILETU")
        else:
            if(self.LAN_BUTTON.property("LANG") == "1"):
                self.LAN_BUTTON.setText("Polski")
                self.LAN_BUTTON.setProperty("LANG", "0")
                self.ULG_BUTTON.setText("Reduced tickets")
                self.NOR_BUTTON.setText("Normal tickets")
                self.EXIT_BUTTON.setText("EXIT")
                self.label.setText('You have choosen ' + str(UITwins.TicketsNormal) + "  normal tickets" + " and " + str(
                UITwins.TicketsReduced) + " reduced.")
            elif(self.LAN_BUTTON.property("LANG") == "0"):
                self.LAN_BUTTON.setText("English")
                self.LAN_BUTTON.setProperty("LANG", "1")
                self.ULG_BUTTON.setText("Bilety ulgowe")
                self.NOR_BUTTON.setText("Normalne bilety")
                self.EXIT_BUTTON.setText("WYJDŹ")
                self.label.setText('Wybrano ' + str(UITwins.TicketsNormal) + "  biletow normalnych" + " oraz " + str(
                UITwins.TicketsReduced) + " ulgowych.")

    def _expand(self):
        self.resize(775, 780)

    def onClickExit(self):
        sys.exit(app.exec_())


class NoMoneyInMachine(Exception):
    print("Transakcja nieudana. Brak pieniędzy w maszynie.")
    #UITwins.label.setText("Transakcja nieudana. Brak pieniędzy w maszynie.")


class Ticket:
    def __init__(self, name, type, price):
        self.name = name
        self.type = type
        self.price = price

class Summary:
    def __init__(self):
        self.ticketList = list()
        self.price = 0
        self.numberOfTickets = 0

    def addTicket(self, ticket):
        if isinstance(ticket, Ticket):
            self.ticketList.append(ticket)
            self.price += ticket.price
            self.numberOfTickets += 1

    def returnMoney(self):
        moneyToReturn = {
            '20gr': 0,
            '50gr': 0,
            '1zl': 0,
            '2zl': 0,
            '5zl': 0,
            '10zl': 0,
            '20zl': 0,
            '50zl': 0,
            '100zl': 0,
            '200zl': 0
        }
        print("a")

    def giveRest(self):
       summaryCost = 0
       moneyInMachine = 10000
       if(summaryCost > moneyInMachine):
           raise NoMoneyInMachine()
       elif (summaryCost == moneyInMachine):
           moneyInMachine = moneyInMachine - summaryCost
           print("Kupiono bilety za podana kwote.")
       else:
           print("Sa pieniadze")


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.UITwins = UITwins()
        self.startUITwins()

    def startUITwins(self):
        self.UITwins.setupUI(self)
        self.show()


if __name__ == '__main__':
    app = QApplication([])
    app.setStyleSheet(StyleSheet)
    w = MainWindow()
    mach = m.Machine()
    sys.exit(app.exec_())