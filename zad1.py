x = int(input("podaj pierwsza liczbe: "))
y = int(input("podaj druga liczbe: "))
'''if x<y:
    for x in range(x,y+1):
        print(x)
elif y>x:
    for y in range(y,x+1):
        print(y)
elif x==y :
    print("liczby sa równe")

else:
    print("niepoprawne liczby")'''
if x>y:
    x,y = y,x
while x <= y:
    print(x, end=" ")
    x = x + 1