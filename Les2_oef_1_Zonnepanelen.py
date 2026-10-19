geldbetaald = float(input("Hoeveel betaalde je voor je zonnepanelen? "))
premie = (1/5 * geldbetaald)
if premie >= 600:
    print (f"Je krijgt een premie van {600} euro.")
if premie <= 600:
    print (f"Je krijgt een premie van {premie} euro.")