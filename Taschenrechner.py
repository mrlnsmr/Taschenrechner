from time import *

for i in range(100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000):
    #Rechenart
    rechenart = str(input('Welche Rechenart möchtest du verwenden? :'))

    #Zahlen
    zahl1 = int(input('Gib die erste Zahl ein mit der du Rechnen möchtest? :'))
    zahl2 = int(input('Gib die zweite Zahl ein mit der du Rechnen möchtest? :'))

    #Rechnung
    if rechenart == '+':
        print(f'{zahl1} {rechenart} {zahl2} = {zahl1+zahl2}')
    elif rechenart == '-':
        print(f'{zahl1} {rechenart} {zahl2} = {zahl1-zahl2}')
    elif rechenart == '*':
        print(f'{zahl1} {rechenart} {zahl2} = {zahl1*zahl2}')
    elif rechenart == '/':
        print(f'{zahl1} {rechenart} {zahl2} = {zahl1/zahl2}')
    else:
        print('Keine gültige Antwort.')

    #Fortsetzung
    Fortsetzung = str(input('Möchtest du nochmal rechnen?:'))

    if Fortsetzung.lower == "nein":
        break
print("Auf Wiedersehen!")