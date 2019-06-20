def faculty(a):
    sum = 1;
    for i in range(1, (a+1)):
        sum = sum * i
    return print(sum)

#This implementation is based on the following definition: https://de.wikipedia.org/wiki/Fakult%C3%A4t_%28Mathematik%29
faculty(0) # returns 1
faculty(3) # returns 6
