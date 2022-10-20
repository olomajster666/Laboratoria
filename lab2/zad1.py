x = int(input("Podaj wiek: "))

if x < 4:
    print("wstęp bezplatny")
elif x>4 and x<=18:
    print("koszt biletu to 10zl")
else:
    print("koszt biletu to 20zl")