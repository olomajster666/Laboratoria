x = int(input("podaj liczbe: "))
r=2
for y in range(1,x+1,1):
    for z in range(1,r,1):
        print("*", end=" ")
    r= r+1
    print()