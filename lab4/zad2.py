import random

zestaw_1=[]
x=int(input("podaj liczbe elemetow listy: "))
y=0
for y in range(x):
    zestaw_1.append(random.randint(1,10))
print(zestaw_1)

zestaw_2=[]
z=int(input("podaj liczbe elemetow listy: "))
y=0
for y in range(z):
    zestaw_2.append(random.randint(1,15))
print(zestaw_2)

c=int(input('podaj liczbe: '))

if c in zestaw_1:
    print('liczba jest w zestawie 1')

if c in zestaw_2:
    print('liczba jest w zestawie 2')

else:
    print('liczby nie ma w zestawach')


zestaw_1_2=[]
zestaw_1_2 = zestaw_1 + zestaw_2
zestaw_1_2.sort()
print(zestaw_1_2)



