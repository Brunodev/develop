import random
losowa = random.randint(1, 10)
liczba_prob=1

for i in range(100000):
    wpisana = input("Wprowadz liczbę od 1 do 10: ")
    if "exit" == wpisana:
        print("Koniec")
        break
    else:
        if losowa == int(wpisana):
            print(("Brawo, zgadles! Liczba prób: {}") .format(liczba_prob))
            break
        else:
            liczba_prob += 1
            if losowa > int(wpisana):
                print("Troche za mało")
            else:
                print("Troche za duzo")