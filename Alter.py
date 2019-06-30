import datetime
now = datetime.datetime.now()

def alter(jahr):
    if (jahr <= now.year):
        print("Du bist: " + str(now.year - (jahr+1)) + " Jahre jung.")
    else:
        print("Gebe einen Wert kleiner als " + str(now.year) + " an.")

alter(1994) #Du bist 24 Jahre alt. (now.year = 2019).
alter(2020) #Gebe einen Wert kleiner als (now.year = 2019) an.
