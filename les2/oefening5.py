from random import randrange
getal1 = (randrange(10) + 1)
getal2 = (randrange(10) + 1)
uitkomst = getal1 * getal2
watdenkje = int(input(f"Hoeveel is {getal1} x {getal2}?: "))
if watdenkje == uitkomst:
    print("Juist, goed zo!")
else:
    print(f"Fout! Het juiste antwoord is {uitkomst}.")