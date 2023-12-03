#PyLotto and Coinflip by Castro
#
from random import randint

print("CCCCC   AAAAA   SSSSS   TTTTT   RRRRR   OOOOO")
print("CC      AAAAA   S         T     R   R   O   O")
print("CC      A   A   S         T     R  RR   O   O")
print("CC      AA AA   SSSSS     T     RRRR    O   O")
print("CC      AA AA       S     T     R  R    O   O")
print("CC      A   A       S     T     R   R   O   O")
print("CCCCC   A   A   SSSSS     T     R   R   OOOOO")

print("-----------------------------------------------------")
print("Coded by Castro for Holznudel <3")
print("#####################################################")

print("Willkommen bei PyLotto, dem Spiel das Sie nicht Gewinnen werden!")
Spielerzahl = input("Bitte Wählen Sie ihre 7 LottoZahlen:")

Gzahl = randint(1111111, 9999999)

if Spielerzahl == Gzahl:
    print("Du Hast gewonnen!")
else:
    print("Du hast verloren, nur Idioten spielen Lotto!")

print("Die Gewinnzahlen lauten:")
print(randint(1111111, 9999999))


print("Weitere Chance: Castros Glückliches Raten")
Gedacht = input("Wähle Kopf (1) oder Zahl (2)")

kopf = 1
Zahl = 2

Wurf = randint(1,2)

print(Wurf)

if int(Wurf) == int(Gedacht):
    print("Du hast Gewonnen")
else:
    print("Du hast Verloren")

print("Vielen Dank fürs Spielen :)")
