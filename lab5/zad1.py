values = ['10','20','30']
keys = ['ten', 'twenty', 'thirty']
D1 = dict(zip(keys,values))
print(D1)

D2 = dict(thirty='30', forty='40', fifty='50')
print(D2)
D3={}

D3=D1.copy()
D3.update(D2)


print(D3)