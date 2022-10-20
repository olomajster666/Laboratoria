x = input("podaj litere: ")
if len(x) > 1 or len(x) == 0:
    print("Niepoprawne dane")
    exit()
if x >= 'a' and x <= 'z':
    print("mala litera")
elif 'A' <= x <= 'Z':
    print("duza litera")
else:
    print("pozostałe znaki")


