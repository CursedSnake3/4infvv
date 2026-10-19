getal1 = float(input("Geef getal 1: "))
getal2 = float(input("Geef getal 2: "))
bewerking = input("Welke bewerking wil je uitvoeren? (+,-,/,*): ")

if bewerking == "+": # == : is gelijk aan; <= : kleiner dan en gelijk aan; < : kleiner dan; != : niet gelijk aan
    print(f"{getal1} + {getal2} is {getal1+getal2}.")

if bewerking == "-":
    print(f"{getal1} - {getal2} = {getal1-getal2}")

if bewerking == "*":
    print(f"{getal1} * {getal2} = {getal1*getal2}")

if bewerking == "/":
    print(f"{getal1} / {getal2} = {getal1/getal2}")