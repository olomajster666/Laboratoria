import random

x=int(input("podaj liczbe elemetow listy: "))
zestaw_1=[]
y=0
for y in range(0,x+1,1):
    zestaw_1= random.randint(1,10)
print(zestaw_1)