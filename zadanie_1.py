#sprawdzenie parzystosci
liczba = int(input("Wprowadź numer: "))
if (liczba % 2 == 0):
    print("Liczba jest parzysta")
else:
    print("Liczba jest nieparzysta")

#sprawdzenie wielokrotnosci 4
if (liczba % 4 == 0):
    print("Hej ta liczba jest wielokrotnością 4!")

#wprowadzenie num1 i num2 & sprawdzenie podzielnosci przez siebie
num1 = int(input("Wprowadź pierwszy numer: "))
num2 = int(input("Wprowadź drugi numer: "))
if (num1 % num2 == 0):
    print("Pierwsza liczba podzielona przez drugą jest wynikiem bez reszty")