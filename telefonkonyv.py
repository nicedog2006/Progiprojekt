
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
    beolvas = open('telefonkonyv.txt','r', encoding='utf-8')
    sorok=beolvas.readlines()
    print('Kérem írja be,')
    szoveg=input('A nevét:')
    for i in range(0,len(sorok),3):
        if szoveg in sorok[i]:
            print()
            print('Van már ilyen név a telefonkönyvben!')
            indito()
        
        else:
            i=i+3
    
    print(szoveg, file=kiiras)
    szoveg=input('Az email címét (valaki@gmail.com):')
    print(szoveg, file=kiiras)
    szoveg=input('A telefonszámát (30/123 4567):')
    print(szoveg, file=kiiras)
    kiiras.close()
    exit()
    
def Keresnev():
    print('-------------------')
    nev= input('Kérem adja meg a keresett nevet:')
    beolvas = open('telefonkonyv.txt','r', encoding='utf-8')
    sorok=beolvas.readlines()
    for i in range(0,len(sorok),3):
        if nev in sorok[i]:
            print()
            print(f'| {sorok[i].strip()} | {sorok[i+2].strip()} | {sorok[i+1].strip()} |')
            exit()
        
        else:
            i=i+3
    print('Nincs ilyen név a telefonkönyvben!')
    indito()
            


def Segedlet():
    print()
    beolvas = open('segedlet.txt','r', encoding='utf-8')
    sorok=beolvas.readlines()
    for i in range(len(sorok)):
        print(sorok[i].strip())
    beolvas.close

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