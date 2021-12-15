spisok0=["Üks","2","kolm","4","VIIS","6","sEITSE","8","ühEKsa","10"]
spisok1=[]
tehe=""
vastus2=""
slovo0="Portugaalia"
slovo1=""
print("Praktiline ülesanne loenditega")
print("Mina mõtlesin välja sõna Portugaalia")
print("Kas te tahate luua oma loendi, mis koosneb 10 elementist või kasutada minu loendi? (0 - minu /1 - uus)")
while True:
    try:
        vastus=int(input("Palun sisetage oma vastus - "))
        if vastus==0 or vastus==1: break
    except ValueError:
        print("Vale andmetüüp!")
if vastus==1:
    for i in range(3):
        spisok1.append(input("Palun sisetage väärtus - "))
    slovo1=input("Palun mõtle välja sõna - ")
    while vastus2!=0:
        try:
            print("1 - Näidata loendi")
            print("2 - Näidata loendi sortimist")
            print("3 - Näidata loendi suurim arv")
            print("4 - Näidata loendi ümber pööramist")
            print("5 - Loengute ühendamine")
            print("6 - Loengu kopeerimine")
            print("7 - Lisada element loendi lõppu")
            print("8 - Kustutada loendi esimest väärtust")
            print("9 - Näidata loendi pikkust")
            print("10 - Puhastada loendit")
            print(f"11 - Kontroll, kas sõnas {slovo1} on numbrid")
            print(f"12 - Kontroll, kas sõnas {slovo1} on tähed")
            print(f"13 - Kontroll, kas sõna {slovo1} algab suure algustähega")
            print("14 - Teisendada esimest tähte suurtäheks ja kõik teised väiketähtedeks")

            while tehe!=int and tehe not in [1,2,3,4,5,6,7,8,9,10,11,12,13,14]:
                try:
                    tehe=int(input("Palun kirjutage mida tahate teha - "))
                except ValueError:
                    print("Vale andmetüüp!")
            if tehe==1:
                print(spisok1)
            elif tehe==2:                
                print(spisok1.sort())
            elif tehe==3:
                print(max(spisok1))
            elif tehe==4:                
                print(spisok1.reverse())
            elif tehe==5:                
                print(spisok1.extend(spisok0))
            elif tehe==6:               
                print(spisok1.copy())
            elif tehe==7:
                spisok1.append(input("Sisetage element, mis tahate lisada - "))
                print(spisok1)
            elif tehe==8:               
                print(spisok1.pop(0))            
            elif tehe==9:
                print(len(spisok1))
            elif tehe==10:
                spisok1.clear()
                print(spisok1)
            elif tehe==11:
                if slovo1.isdigit()==True:
                    print(f"Sõna {slovo1} sisaldab numbri")
                else:
                    print(f"Sõna {slovo1} ei sisalda numbri")
            elif tehe==12:
                if slovo1.isalpha()==True:
                    print(f"Sõna {slovo1} sisaldab tähti")
                else:
                    print(f"Sõna {slovo1} ei sisalda tähti")
            elif tehe==13:
                if slovo1.istitle()==True:
                    print(f"Sõna {slovo1} algab suure algustähega")
                else:
                    print(f"Sõna {slovo1} algab väikse algustähega")
            elif tehe==14:
                print(slovo1.capitalize())
            print("Kas tahate jätkata? (0 - Ei/1 - Jah)")
            while True:
                try:
                    vastus2=int(input("Sisetage vastus - "))
                    if vastus2==1 or vastus2==0: break
                except ValueError:
                    print("Vale andmetüüp!")
        except ValueError:
            print("Aitäh töötamise eest!")
else:
    while vastus2!=0:
        try:
            print("1 - Näidata loendi")
            print("2 - Näidata loendi sortimist")
            print("3 - Näidata loendi suurim arv")
            print("4 - Näidata loendi ümber pööramist")
            print("5 - Loengute ühendamine")
            print("6 - Loengu kopeerimine")
            print("7 - Lisada element loendi lõppu")
            print("8 - Kustutada loendi esimest väärtust")
            print("9 - Näidata loendi pikkust")
            print("10 - Puhastada loendit")
            print(f"11 - Kontroll, kas sõnas {slovo0} on numbrid")
            print(f"12 - Kontroll, kas sõnas {slovo0} on tähed")
            print(f"13 - Kontroll, kas sõna {slovo0} algab suure algustähega")
            print("14 - Teisendada esimest tähte suurtäheks ja kõik teised väiketähtedeks")
            while tehe!=int and tehe not in [1,2,3,4,5,6,7,8,9,10,11,12,13,14]:
                try:
                   tehe=int(input("Palun kirjutage mida tahate teha - "))
                except ValueError:
                   print("Vale andmetüüp!")
            if tehe==1:
                print(spisok0)
            elif tehe==2:                
                print(spisok0.sort())
            elif tehe==3:
                print(max(spisok0))
            elif tehe==4:                
                print(spisok0.reverse())
            elif tehe==5:                
                print(spisok0.extend(spisok0))
            elif tehe==6:               
                print(spisok0.copy())
            elif tehe==7:
                spisok0.append(input("Sisetage element, mis tahate lisada - "))
                print(spisok0)
            elif tehe==8:               
                print(spisok0.pop(0))            
            elif tehe==9:
                print(len(spisok0))
            elif tehe==10:
                spisok0.clear()
                print(spisok0)
            elif tehe==11:
                if slovo0.isdigit()==True:
                    print(f"Sõna {slovo0} sisaldab numbri")
                else:
                    print(f"Sõna {slovo0} ei sisalda numbri")
            elif tehe==12:
                if slovo0.isalpha()==True:
                    print(f"Sõna {slovo0} sisaldab tähti")
                else:
                    print(f"Sõna {slovo0} ei sisalda tähti")
            elif tehe==13:
                if slovo0.istitle()==True:
                    print(f"Sõna {slovo0} algab suure algustähega")
                else:
                    print(f"Sõna {slovo0} algab väikse algustähega")
            elif tehe==14:
                    print(slovo0.capitalize())
            print("Kas tahate jätkata? (0 - Ei/1 - Jah)")
            while True:
                try:
                    vastus2=int(input("Sisetage vastus - "))
                    if vastus2==1 or vastus2==0: break
                except ValueError:
                    print("Vale andmetüüp!")
        except ValueError:
            print("Aitäh töötamise eest!")