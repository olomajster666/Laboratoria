n = int(input("podaj liczbe studentow: "))
x = 1
s = 0
while(n>=x):
    p=int(input("podaj liczbe punktow studenta: "))
    x=x+1
    s =s+p

print("srednia punktow wynosi:", s/n )