spisok0=["Üks","2","kolm","4","VIIS","6","sEITSE","8","ühEKsa","10"]
spisok1=[]
tehe=""
vastus2=""
print("Praktiline ülesanne loenditega")
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
    while vastus2!=0:
        try:
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
                spisok1.pop(0)
                print(spisok1)            
            elif tehe==9:
                print(len(spisok1))
            elif tehe==10:
                spisok1.clear()
                print(spisok1)
            print("Kas tahate jätkata? (0 - Ei/1 - Jah)")
            while True:
                try:
                    vastus2=int(input("Sisetage vastus - "))
                except ValueError:
                    print("Vale andmetüüp!")
        except ValueError:
            print("Aitäh töötamise eest!")
