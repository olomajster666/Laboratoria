import random
punkty=[]
x= 0
for x in range(15):
    punkty.append(round(random.uniform(0, 50),2))
print(punkty)
z=float(input('podaj szukana liczbe: '))
if z in punkty:
    print(z)
else:
    print('nie wystapuje taka iloc puntkow')
avg = round(sum(punkty)/len(punkty),2)
print('srednia listy to ',avg)

print('max punkty to: ',max(punkty))
print('min punkty to: ',min(punkty))
n=0
punkty_2 =[]
for i in range(n):
    if punkty[i]>avg:
        punkty_2.append(i)

punkty_3 =[]
for i in range(n):
    if punkty[i]<avg:
        punkty_3.append(i)

print('powyzej sredniej: ',punkty_2)
print('ponizej sredniej: ',punkty_3)

