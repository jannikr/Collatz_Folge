zahl = int(input("Bitte geben Sie eine natürliche Zahl ein:"))
collatzliste = []

while zahl > 1:
    if zahl % 2 == 0 :
        zahl = zahl //2
        collatzliste.append(zahl)
    elif zahl % 2 == 1 :
        zahl = 3 * zahl + 1
        collatzliste.append(zahl)
    if zahl == 1 :
        break
        collatzliste.append(zahl)

print ("Die Collatzfolge für denangegebenen Wert lautet:", collatzliste)
print ("Es gibt in der Liste", len(collatzliste), "Werte.")





