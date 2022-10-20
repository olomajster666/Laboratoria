o = int(input("Jaką operację chcesz wykonać? 1)dodawanie 2)odejmowanie 3)mnożenie 4)dzielenie 5)potęgowanie : "))
x = int(input("podaj pierwszy argument: "))
y = int(input("podaj drugi argument: "))

if o == 1:
    w = x+y
    print("wynik: ",w)
elif o == 2:
    w = x-y
    print("wynik: ",w)
elif o == 3:
    w = x*y
    print("wynik: ", w)
elif o == 4:
    w = x/y
    print("wynik: ", w)
elif o == 5:
    w = x**y
    print("wynik: ", w)
else:
    print("błędny argument operacji")
