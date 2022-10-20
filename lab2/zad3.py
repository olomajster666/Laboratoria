o = int(input('''Jaką operację chcesz wykonać? 
1)dodawanie 
2)odejmowanie 
3)mnożenie 
4)dzielenie 
5)potęgowanie
'''))
x = float(input("podaj pierwszy argument: "))
y = float(input("podaj drugi argument: "))
if o > 5 or o < 0:
    print("błędny argumant operacji")
    exit()
elif o == 1:
    print("wynik: ",x+y)
elif o == 2:
    print("wynik: ",x-y)
elif o == 3:
    print("wynik: ", x*y)
elif o == 4:
    if y == 0:
        print("nie mozna dzielic przez zero")
        exit()
    print("wynik: ", x/y)
elif o == 5:
    print("wynik: ", x**y)

