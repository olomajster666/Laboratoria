x = int(input("podaj pierwsza liczbe: "))
y = int(input("podaj druga liczbe: "))
if x>y:
    x,y = y,x
while x <= y:
    if x%2 == 1:
        x=x+1
        continue
    print(x, end=" ")
    x = x + 1