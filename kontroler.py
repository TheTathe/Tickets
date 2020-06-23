import sys
from state_machine import (State, Event, acts_as_state_machine, after, before, InvalidStateTransition)


@acts_as_state_machine
class TicketState:
    arrived = State(initial=True)
    waiting = State()
    running = State()
    stopped = State()

    wait = Event(from_states=(arrived, running, stopped), to_state=waiting)
    run = Event(from_states=waiting, to_state=running)
    stop = Event(from_states=(running, waiting, arrived), to_state=stopped)

    def __init__(self, name):
        self.name = name

    @after('wait')
    def wait_info(self):
        print(f'{self.name}  WAITINGUJE')


    @after('run')
    def run_info(self):
        print(f'{self.name}  RUNNINGUJE')

    @after('terminate')
    def block_info(self):
        print(f'{self.name}  TERMINATORUJE')


def transition(process, event, event_name):
    try:
        event()
    except InvalidStateTransition as err:
        print(f'Error: TRANZYCJA JEBLA  {process.name} Z {process.current_state} DO {event_name} NIESTETY')


def state_info(process):
    print(f'STAN PROCESA {process.name}: {process.current_state}')


class Controler():
    def __init__(self, w, m):
        self.widok = w
        self.automat = m

        self.RUNNING = 'running'
        self.WAITING = 'waiting'
        self.STOPPED = 'stopped'
        self.p1, self.p2 = TicketState('ticket1'), TicketState('ticket2')
        [state_info(p) for p in (self.p1, self.p2)]
        """
        Ukrywanie "menu monet" po prawej stronie. Przypisać do czegoś, wykorzystać.
        """

        #self.widok.areButtonsHidden = 0
        #self.hideMoneyButtons(0)
        #self.widok.buttonLeftDown.clicked.connect(self.onClickLanguage)


        self.widok.buttonLeftUpper.clicked.connect(lambda: self.hideMoneyButtons(self.widok.areButtonsHidden))
        self.widok.buttonRightUpper.clicked.connect(self.onClickAddTicketNormal)
        #self.widok.buttonRightDown.clicked.connect(self.onClickExit)
        #self.widok.buttonRightDown.clicked.connect(self.fun1)
        #self.widok.buttonRightDown.clicked.connect(self.fun2)
        self.widok.buttonRightDown.clicked.connect(lambda: self.stanZmiana(1))
        self.widok.button20gr.clicked.connect(lambda: self.onClickMoneyButton(0))
        self.widok.button50gr.clicked.connect(lambda: self.onClickMoneyButton(1))
        self.widok.button1zl.clicked.connect(lambda: self.onClickMoneyButton(2))
        self.widok.button2zl.clicked.connect(lambda: self.onClickMoneyButton(3))
        self.widok.button5zl.clicked.connect(lambda: self.onClickMoneyButton(4))
        self.widok.button10zl.clicked.connect(lambda: self.onClickMoneyButton(5))
        self.widok.button20zl.clicked.connect(lambda: self.onClickMoneyButton(6))
        self.widok.button50zl.clicked.connect(lambda: self.onClickMoneyButton(7))
        self.widok.button100zl.clicked.connect(lambda: self.onClickMoneyButton(8))
        self.widok.button200zl.clicked.connect(lambda: self.onClickMoneyButton(9))

        """
        Bilety ulgowe
        """

    def stanZmiana(self, n):
        #print(state_info(p) for p in (self.p1, self.p2))
        if n == 1:
            print("1")
            transition(self.p1, self.p1.wait, self.WAITING)
            transition(self.p2, self.p2.stop, self.STOPPED)
            [state_info(p) for p in (self.p1, self.p2)]
            self.widok.button1zl.clicked.disconnect()
            self.widok

        elif n == 2:
            print("2")
            transition(self.p1, self.p1.run, self.RUNNING)
            transition(self.p2, self.p2.wait, self.WAITING)
            [state_info(p) for p in (self.p1, self.p2)]

        elif n == 3:
            print("3")
            transition(self.p2, self.p2.run, self.RUNNING)
            [state_info(p) for p in (self.p1, self.p2)]

        elif n == 4:
            print("4")
            transition(self.p2, self.p2.run, self.RUNNING)
            [state_info(p) for p in (self.p1, self.p2)]

        else:
            print("otha side")
            [transition(p, p.stop, self.STOPPED) for p in (self.p1, self.p2)]
            [state_info(p) for p in (self.p1, self.p2)]



    def onClickAddTicketReduced(self):
        print("X")

        """
        Funkcja od chowania menu monet
        
        Na ten moment przypisana do buttonLeftUpper
        """

    def hideMoneyButtons(self, n):
        if n == 1:
            self.widok.labelShowPrice.show()
            self.widok.button20gr.show()
            self.widok.button50gr.show()
            self.widok.button1zl.show()
            self.widok.button2zl.show()
            self.widok.button5zl.show()
            self.widok.button10zl.show()
            self.widok.button20zl.show()
            self.widok.button50zl.show()
            self.widok.button100zl.show()
            self.widok.button200zl.show()
            self.widok.areButtonsHidden = 0
        else:
            self.widok.labelShowPrice.hide()
            self.widok.button20gr.hide()
            self.widok.button50gr.hide()
            self.widok.button1zl.hide()
            self.widok.button2zl.hide()
            self.widok.button5zl.hide()
            self.widok.button10zl.hide()
            self.widok.button20zl.hide()
            self.widok.button50zl.hide()
            self.widok.button100zl.hide()
            self.widok.button200zl.hide()
            self.widok.areButtonsHidden = 1


        """
        Wywołanie metody Liczenie monet + wyświetlanie na labelce
        """
    def onClickMoneyButton(self, n):
        print("X")
        x = self.automat.addMoney(n)
        print(x)
        self.widok.labelShowPrice.setText("Do automatu włożono:  " + x + " groszy.")

        """
        Testowe liczenie monet
        """
    def onClickAddTicketNormal(self):
        print("Licze monety")
        self.automat.countMoney()


        """
        Wyjscie
        """



    def fun1(self):
        print("jebany")
        self.widok.labelShowMainText.setText("CO TAM SOPATA")

    def fun2(self):
        print("debil")
        self.widok.labelShowPrice.setText("NIE DA SIĘ XD")


        """
        Wyjscie
        """

    def onClickExit(self):
        sys.exit()