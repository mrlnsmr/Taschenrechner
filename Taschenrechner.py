from time import *

while True:
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

    if Fortsetzung.lower == "ja":
        continue
    else:
        print("Auf Wiedersehen!")
    break