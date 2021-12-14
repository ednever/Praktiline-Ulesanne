spisok0=["Üks","2","kolm","4","VIIS","6","sEITSE","8","ühEKsa","10"]
spisok1=[]
tehe=""
print("Praktiline ülesanne järjenditega")
print("Kas te tahate luua oma loendi, mis koosneb 10 elementist või kasutada minu loendi? (0 - minu /1 - uus)")
while True:
    try:
        vastus=int(input("Palun sisetage oma vastus - "))
        if vastus==0 or vastus==1: break
    except ValueError:
        print("Vale andmetüüp!")
if vastus==1:
    for i in range(10):
        spisok1.append(input("Palun sisetage väärtust - "))
    while True:
        print("1 - Näidata loendi")
        print("2 - Kontroll, kas loend sisaldab nubri")
        print("3 - Kontroll, kas loend sisaldab tähti")
        print("4 - Näidata loendi ümber pööramist")
        print("5 - Näidata loendi, mis koosneb suurte algustähtedest")
        print("6 - Näidata loendi, mis koosneb väikste algustähtedest")
        print("7 - Lisada element loendi lõppu")
        print("8 - Kustutada loendi esimest väärtust")
        print("9 - Näidata loendi pikkust")
        print("10 - Puhastada loendit")
        while tehe!=int and tehe not in [1,2,3,4,5,6,7,8,9,10]:
            try:
                tehe=int(input("Palun kirjutage mida tahate teha - "))
            except ValueError:
                print("Vale andmetüüp!")
        if tehe==1:
            print(spisok1)
        elif tehe==2:
            spisok1.isdigit()
            print(spisok1)
        elif tehe==3:
            spisok1.isalpha()
            print(spisok1)
        elif tehe==4:
            spisok1.reverse()
            print(spisok1)
        elif tehe==5:
            spisok1.isupper()
            print(spisok1)
        elif tehe==6:
            spisok1.islower()
            print(spisok1)
        elif tehe==7:
            spisok1.append(input("Sisetage element, mis tahate lisada - "))
            print(spisok1)
        elif tehe==8:
            spisok1.pop(1)
            print(spisok1)            
        elif tehe==9:
            print(len(spisok1))
        elif tehe==10:
            spisok1.clear()
        print("Kas te soovite jätkata? (0 - Ei/1 - Jah)")
        while True:
            try:
                vastus2=int(input("Palun sisetage oma vastus - "))
                if vastus2==0 or vastus2==1: break
            except ValueError:
                print("Vale andmetüüp!")
        if vastus2==1:
            continue
        else:
            quit()
#else:
#    while True:
#        print("1-Посмотреть список")
#        print("2-Добавить элемент в конец списка")
#        print("3-Удалить элемент в конце списка")
#        print("4-Развернуть список")
#        print("5-Сортировать список от меньшего к большему")
#        print("6-Показывает наибольшое значение в списке")
#        print("7-Преобразовать строку в верхней регистр")
#        print("8-Преобразовать строку в нижний регистр")
#        print("9-Посмотреть длину списка")
#        print("10-Очистить список")
#        while tehe!=int and tehe not in [1,2,3,4,5,6,7,8,9,10]:
#            try:
#                tehe=int(input("Введите номер=> "))
#            except:
#                TypeError
#        if tehe==1:
#            print(spisok0)
#        elif tehe==2:
#            spisok0.append(input("Введите элемент, который хотите добавить=> "))
#            print(spisok0)
#        elif tehe==3:
#            spisok0.pop()
#            print(spisok0)
#        elif tehe==4:
#            spisok0.reverse()
#            print(spisok0)
#        elif tehe==5:
#            spisok0.sort()
#            print(spisok0)
#        elif tehe==6:
#            print(max(spisok0))
#        elif tehe==7: #Не работает со списками, потом переделаю :(
#            spisok0.upper()
#            print(spisok0)
#        elif tehe==8: #Не работает со списками, потом переделаю :(
#            spisok0.lower()
#            print(spisok0)
#        elif tehe==9:
#            print(len(spisok0))
#        elif tehe==10:
#            spisok0.clear()