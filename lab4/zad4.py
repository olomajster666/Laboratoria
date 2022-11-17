imiona=['Kasia', 'Tomek', 'Jan', 'Ola', 'Jerzy', 'Marek', 'Piotr',
'Zuzia', 'Bartek', 'Jacek']

imiona[3]='heniu'
imiona.insert(4,'stasiu')
imiona.remove(imiona[6])

print(imiona)

imiona.insert(0,'kundegunda')
imiona.insert(0,'bogumila')
imiona.insert(0,'grzegorz')

x = input('podaj imie do usuniecia z listy: ')
imiona.remove(x)

