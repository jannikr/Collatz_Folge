#Dieses Programm berechnet einen beliebigen Modulo einer beliebigen Zahl ohne den Modulo-Operator
#in Python zu werdenen. 

#In der Variable n wird eine Zahl gespeichert, durch die später modulo gerechnet werden soll
n = int(input("Bitte geben Sie eine Zahl ein, die mit Modulo berechnet werden soll:"))

#In der Variable mod wird eine Zahl gespeichert, mit der geteilt wird.
mod = int(input("Bitte geben sie eine beliebige Zahl für den Modulo-Wert an:"))
     


#Fallunterscheidung: N ist kleiner als Null = Negativ und mod ist größer als Null = Positiv
if n < 0 and mod > 0:
    while n <= 0:
        n = n + mod
    else:
        print ("Der Rest der anhand ihrer Zahlenauswahl berechnet wurde beträgt", (n))
#1. Wenn n Negativ ist und Mod Positiv, dann wird in der Variablen n solange modulo addiert, bis n größer 0.
#Dieses n wird ausgegeben.


#Fallunterscheidung: N ist größer als Null = Positiv und mod ist kleiner als Null = Negativ
elif n > 0 and mod < 0:
    while n > 0:
        n = n + mod
    else:
        print ("Der Rest der anhand ihrer Zahlenauswahl berechnet wurde beträgt", (n))
#Siehe Kommentar 1.


        
#Fallunterscheidung: Beide Variablen n und mod sind positiv
elif n > 0 and mod > 0:
    while n >= mod:
        n = n - mod
    else:
        print ("Der Rest der anhand ihrer Zahlenauswahl berechnet wurde beträgt", (n))
#2. Wenn n Positiv ist und Mod Positiv, dann wird mod solange von n abgezogen, bis n kleiner als mod ist.
#Dieses n wird augegeben.



#Fehlerbehandlung: Error bei mod = 0. Durch Null teilen nicht erlaubt.
elif mod == 0:
        print ("Nicht durch 0 teilen!")



#Fallunterscheidung: N ist kleiner als Null = Negativ und mod ist kleiner als Null = Negativ
else:
    while n <= mod:
        n = n - mod
    else:
        print ("Der Rest der anhand ihrer Zahlenauswahl berechnet wurde beträgt", (n))
#Siehe Kommentar 2.
