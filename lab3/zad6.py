n = int(input("podaj liczbe studentow: "))
x = 0
s = 0
while True:
    z=int(input("podaj liczbe punktow studenta: "))
    x=x+1
    s =s+z
    if z>100 or z<0:
        break
    elif x>=n:
        break
    else:
        continue
print("srednia punktow wynosi:", s/n )