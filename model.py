




class Machine():
    """
    Maszyna - automat. Obecnie masz tam 500 * 20g (10000gr = 100zł).


    """
    def __init__(self):
        print("ELO TO JA TWOJA MASZYNA")
        self.moneyInMachine = {
            '20gr': 500,
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
        self.keys = ['20gr', '50gr', '1zl', '2zl', '5zl', '10zl', '20zl', '50zl', '100zl', '200zl']
        self.moneyGiventoMachine = 0
        self.multipliers = [20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000]

        """
        Mnożniki od końca i klucze też. Zastosowac .reverse może?
        """
        self.multipliersToReturn = [20000, 10000, 5000, 2000, 1000, 500, 200, 100, 50, 20]
        self.keysReturn = ['200zl', '100zl', '50zl', '20zl', '10zl', '5zl', '2zl', '1zl', '50gr', '20gr']

    """
    Liczenie mone.
    """

    def countMoney(self):
        summ = 0
        for x in range(0, 9):
            summ += self.multipliers[x] * self.moneyInMachine[self.keys[x]]
            print("Stan automatu w groszach to: " + str(summ) + " groszy")
            print("Stan automatu w groszach to: " + str(summ / 100) + " zlotych")
        return (summ)



    """
    Dodawanie monet
    
    KEYS - 0, 9
    0 = 20gr
    1 = 50gr
    etc, patrzeć na multipliers
    
    
    """

    def addMoney(self, n):
        print(str(self.keys[n]))
        self.moneyInMachine[self.keys[n]] += 1
        print("Dodałem monetę. Mam monet " + str(self.moneyInMachine[self.keys[n]]) + " o wartości: " + str(self.keys[n]))
        return (self.countMoneyGivenToMachine(n))

    """
    Oblicz ile klient wrzucil. Zwroc i wyswietl potem w labelce.
    ATM w groszach.

    """
    def countMoneyGivenToMachine(self, m):
        print("Brum brum liczę monety")
        print(str(self.multipliers[m]))
        self.moneyGiventoMachine += self.multipliers[m]
        return str(self.moneyGiventoMachine)

"""
Kasjer. Do przetestowania i zmian.


    def giveRest(self):
        plnRest = 11000
        for i in range(10):
            while (plnRest >= self.multipliersToReturn[i] and self.moneyInMachine[self.keysReturn[i]] > 0) and plnRest > 0:
                print("Reszta jest mniejsza, niż moneta " + str(
                    self.multipliersToReturn[i] / 100) + " mam monety - mogę wydać w monetach " + str(self.keysReturn[i]))
                print(str(self.moneyInMachine[self.keysReturn[i]]) + " monet w automacie o wartosci " + str(self.keysReturn[i]))
                plnRest -= self.multipliersToReturn[i]
                self.moneyInMachine[self.keysReturn[i]] -= 1
                self.moneyToReturn[self.keysReturn[i]] += 1
                print("Pozostała reszta to: " + str(plnRest / 100) + " złotych, monet " + str(
                    self.multipliersToReturn[i] / 100) + "zostało " + str(self.moneyInMachine[self.keysReturn[i]]))
    
        if(plnRest != 0):
            print("Nie da się wydać")
            #restoreState()
        else:
            for i in range(10):
                if(self.moneyToReturn[keysReturn[i]] != 0):
                    print("Zostanie wydanych: " + str(self.moneyToReturn[self.keysReturn[i]]) + "monet o wartości " + str(self.keysReturn[i]))


"""



"""
    Bilety. NYI
"""

class Tickets():
    def __init__(self):
        self.amount = None
        self.type = None


class Zamowienie():
    def __init__(self):
        self.CzyToWogoleJestPotrzebneToJaNieWiemAleSieDomyslam = "Ehhhhhhhhh"
        self.cost = 0
    def addTickets(self):
        print("Dodałem bileta")