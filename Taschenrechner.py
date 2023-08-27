#Rechenart
rechenart = str(input("Welche Rechenart möchtest du verwenden? :"))

#Zahlen
zahl1 = int(input("Gib die erste Zahl ein mit der du Rechnen möchtest? :"))

zahl2 = int(input("Gib die zweite Zahl ein mit der du Rechnen möchtest? :"))

#Addition
if rechenart == "+" ():
    print(f"{zahl1} {rechenart} {zahl2} = {zahl1+zahl2}")
#Subtraktion
elif rechenart == "-" ():
    print(f"{zahl1} {rechenart} {zahl2} = {zahl1-zahl2}")
#Multiplikation
elif rechenart == "*" ():
    print(f"{zahl1} {rechenart} {zahl2} = {zahl1*zahl2}")
#Division
elif rechenart == "/" ():
    print(f"{zahl1} {rechenart} {zahl2} = {zahl1/zahl2}")
#Nicht möglich
else:
    print("Keine gültige Antwort.")