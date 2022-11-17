import random
punkty = []
n = 15
for i in range(n):
    p = random.uniform(0, 50)
    punkty.append(round(p, 2))
print()
print(punkty)
print(f'min = {min(punkty)}')
print(f'max = {max(punkty)}')
avg = round(sum(punkty)/len(punkty), 2)
print('avg = ', avg)
p = float(input('Podaj liczbę punktów: '))
if p in punkty:
    print(punkty.index(p))
else:
    print(f'liczba {p} punktów nie występuje na liście')
print()
punkty_w = []
punkty_m = []
for i in range(n):
    if punkty[i] > avg:
        punkty_w.append(punkty[i])
    if punkty[i] < avg:
        punkty_m.append(punkty[i])
print("ilosc powyzej sredniej: ", len(punkty_w))
print("ilosc ponizej sredniej: ", len(punkty_m))




