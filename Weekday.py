"""
Dieses Programm soll den Benutzer dazu auffordern, ein beliebig von ihm gewähltes Datum einzugeben
(in der Form: zunächst Eingabe des Tages, dann Eingabe des Monats und abschließend Eingabe des Jahres).
Im Anschluss daran soll es den jeweils dazugehörigen Wochentag berechnen und für den Benutzer sichtbar ausgeben.
"""

day  = int(input("Hier können Sie sich zu einem beliebigen Datum den dazugehörigen Wochentag bestimmen lassen. Geben Sie dafür zunächst den Tag des gewünschten Monats als Zahl ein:")) # Definiert die Eingabe für den Tag

"""
Es wird angenommen, dass der Benutzer einen integer eingibt.
Es folgt die Fehlerbehandlung für falsche Wertebereiche in der Eingabe des Tages (>31), die mittels while-Schleife 
für wiederholte Fehlereingaben durchgeführt wird.
Nicht berücksichtigt bleibt hierbei die fälschliche Eingabe eines in bestimmten Monaten nicht existenten Tages, zum Beispiel eines 31.Februars.
"""

while day > 31 : 
    print("Bitte geben Sie einen gültigen Tag ein.")
    day  = int(input("Geben Sie den Tag als Zahl ein:"))
    
month  = int(input("Geben Sie nun den gewünschten Monat in Form einer Zahl ein:")) # Definiert die Eingabe für den Monat

"""
Es folgt die Fehlerbehandlung für falsche Wertebereiche in der Eingabe des Monats (>12), die mittels while-Schleife 
für wiederholte Fehlereingaben durchgeführt wird.
"""
while month > 12 :
    print("Bitte geben Sie einen gültigen Monat ein.")
    month  = int(input("Geben Sie den Monat in Form einer Zahl ein:"))
    
    
year  = int(input("Geben Sie als letztes noch das Jahr, ebenfalls als Zahl, ein:")) # Definiert die Eingabe für das Jahr

"""
Berechnung des Wochentags mit Hilfe der vor dem Quelltext genannten Formel.
Die Variablen year, month und day stammen dabei aus der Eingabe des Benutzers, die Variablen x und y fungieren als Zwischenspeicher.
"""
y = year - (14 - month) // 12
x = y + (y // 4) - (y // 100) + (y // 400)
m = month + 12 * ((14 - month) // 12) - 2
Name = ((day + x + (31 * m) // 12) % 7)

# Ermittlung des Wochentags durch den nach Berechnung der Formel ermittelten Wert
if Name==0 :
    tag = ("Sonntag")
elif Name==1 :
    tag = ("Montag")
elif Name==2 :
    tag = ("Dienstag")
elif Name==3 :
    tag = ("Mittwoch")
elif Name==4 :
    tag = ("Donnerstag")
elif Name==5 :
    tag = ("Freitag")
else:
    tag = ("Samstag")
  
# Ausgabe des Wochentages  
print ("Der gesuchte Wochentag ist", tag)

