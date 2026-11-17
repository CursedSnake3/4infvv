from random import randrange
juistGetal = (randrange(10) + 1)
gegoktGetal = int(input("Raad een getal van 1 tot en met 10: "))
if gegoktGetal == juistGetal:
    print(f"Gewonnen! Het getal was {juistGetal}.")
if gegoktGetal != juistGetal:
    print(f"Helaas! Het getal was {juistGetal}.")