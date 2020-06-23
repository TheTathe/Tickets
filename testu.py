#multipliers = [20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000]
keys = ['20gr', '50gr', '1zl', '2zl', '5zl', '10zl', '20zl', '50zl', '100zl', '200zl']
plnGivenToMachine = 0
plnInMachine = 0
keysReturn = ['200zl', '100zl', '50zl', '20zl', '10zl', '5zl', '2zl', '1zl', '50gr', '20gr']
multipliersToReturn = [20000, 10000, 5000, 2000, 1000, 500, 200, 100, 50, 20]

moneyGivenToMachine = {
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

moneyInMachine = {
'20gr': 10000,
'50gr': 0,
'1zl': 0,
'2zl': 0,
'5zl': 0,
'10zl': 0,
'20zl': 0,
'50zl': 0,
'100zl': 0,
'200zl': 2
        }



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



saveStateTemplate = {
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

plnRest = 21000
#for x in range(len(moneyGivenToMachine)):
    #plnGivenToMachine += multipliers[x] * moneyGivenToMachine[keys[x]]
    #print(x)
#print(len(multipliersToReturn))


def saveState(self):
    for i in range(10):
        saveStateTemplate[keys[i]] = moneyInMachine[keys[i]]


def restoreState(self):
    for i in range(10):
        moneyInMachine[keys[i]] = saveStateTemplate[keys[i]]

print("Reszta do wydania to: " + str(plnRest/100) + " złotych")

"""
Sprawdź czy dana moneta jest możliwa do wydania ORAZ czy jest moneta w maszynie ORAZ czy reszta 
"""
for i in range(10):
    while (plnRest >= multipliersToReturn[i] and moneyInMachine[keysReturn[i]] > 0) and plnRest > 0:
        print("Reszta jest mniejsza, niż moneta " +  str(multipliersToReturn[i]/100)  + " mam monety - mogę wydać w monetach " + str(keysReturn[i]))
        print(str(moneyInMachine[keysReturn[i]]) + " monet w automacie o wartosci " + str(keysReturn[i]))
        plnRest -= multipliersToReturn[i]
        moneyInMachine[keysReturn[i]] -= 1
        moneyToReturn[keysReturn[i]] += 1
        print("Pozostała reszta to: " + str(plnRest/100) + " złotych, monet " +  str(multipliersToReturn[i]/100) + "zostało " + str(moneyInMachine[keysReturn[i]]))


if(plnRest != 0):
    print("Nie da się wydać")
    restoreState()
else:
    for i in range(10):
        if(moneyToReturn[keysReturn[i]] != 0):
            print("Zostanie wydanych: " + str(moneyToReturn[keysReturn[i]]) + "monet o wartości " + str(keysReturn[i]))





"""
#Sprawdź czy wydasz używając monet z automatu, zacznij od 200zł skończ na 20gr
for i in keysReturn:
    print(i + "KLUCZ")
    for j in multipliersToReturn:
        print(j)
        #Jeśli dana moneta jest większa niż reszta -> jeśli tak, to nie zostanie wykorzystana do wydania reszty
        if j > plnRest:
            print(str(multipliersToReturn) + " groszy jest wieksze")

        #Jeśli jest mniejsza niż reszta - może zostać wykorzystana do wydania reszty
        else:
            print(str(multipliersToReturn[j]) + " jest mniejsze")
            if moneyInMachine[keys[j]] > 0:
                print("Jest moneta o nominale " + str(multipliersToReturn[j]/100) + " złotych")
                print("Jest" + str(moneyInMachine[keys[j]]) + " monet o takim nominale")
                #Sprawdź ile musisz mieć monet tego typu do wydania reszty


            else:
                print("Nie ma monety o nominale " + str(multipliersToReturn[j]/100) + " złotych")

        if(plnRest == 0):
            break

    print(str(plnRest) + " RESZTA")
"""