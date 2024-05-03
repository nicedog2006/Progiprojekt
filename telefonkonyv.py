
import os
os.system('cls')

def Telefonkonyv_listazas():
    print('----------------------')
    print()
    beolvas = open('telefonkonyv.txt','r', encoding='utf-8')
    sorok=beolvas.readlines()
    for i in range(0,len(sorok),3):
        print(sorok[i].strip(),sorok[i+2].strip())
        
    beolvas.close()

def Ujadat_bevitel():
    print('----------------')
    print()
    kiiras = open('telefonkonyv.txt', 'a',encoding='utf-8')
    benev = open('telefonkonyv.txt', 'r',encoding='utf-8')
    benne=False
    print('Kérem írja be,')
    szoveg=input('A nevét:')
    szoveg=input('Az email címét:')
    print(szoveg, file=kiiras),
    szoveg=input('A telefonszámát (30/123 4567):')
    print(szoveg, file=kiiras),
    kiiras.close()
    
def Keresnev():
    print('-------------------')
    nev= input('Kérem adja meg a keresett nevet:')
    beolvas = open('telefonkonyv.txt','r', encoding='utf-8')
    sorok=beolvas.readlines()
    if nev in sorok:
        print('Benne van!')
    else:
        print('Nincs ilyen név a telefonkönyvben!')
        indito()

def Segedlet():
    print('segédlet')
    beolvas = open('segedlet.txt','r', encoding='utf-8')
    beolvas = open('telefonkonyv.txt','r', encoding='utf-8')
    sorok=beolvas.readlines()
    for i in range(sorok):
        print(sorok[i].strip())

def indito():
    print('Telefonkönyv')
    print('-----------------------------------')
    print('1. Telefonkönyv listázása')
    print('2. Új adat bevitele')
    print('3. Keresés név szerint')
    print('4. Kilépés')
    print('5. Segédlet')
    print('-----------------------------------')
    print('')
    valasz=int(input('Válassz a fentiek közül egyet. (1-5-ig) :'))

    if valasz==1:
        print()
        print('Telefonkönyv listázása')
        Telefonkonyv_listazas()
    elif valasz==2:
        print()
        print('Új adat bevitele')
        Ujadat_bevitel()
    elif valasz==3:
        print()
        print('Keresés név szerint')
        Keresnev()
    elif valasz==4:
        print()
        print('Kilépés')
        print('„Ön kilépett a programból.')
        exit()
    elif valasz==5:
        print()
        print('Segédlet')
        Segedlet()
    else:
        print()
        print('Hibás menüpont választás!')
        indito()


#Főeljárás
indito()