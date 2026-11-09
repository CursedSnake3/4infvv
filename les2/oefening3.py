seconden = float(input("hoeveel seconden tel je tussen de bliksem en de donder?: "))
afstand = seconden*343/1000
print (f"het onweer is {afstand} km ver.")
if afstand < 3:
    print (Opgelet!)