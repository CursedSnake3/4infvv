seconden = int(input("hoeveel seconden tel je tussen de bliksem en de donder?: "))
afstand = seconden*343/1000
print (f"het onweer is ongeveer {afstand:.1f} km ver.")
if afstand < 3:
    print ("Opgelet! Het onweer is dichtbij. Ga snel naar binnen!")