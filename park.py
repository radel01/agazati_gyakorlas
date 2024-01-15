import Park_o


def beolvas():
    adatokListaja = []
    beFajl = open("park1.txt", "r", encoding="utf-8")
    beFajl.readline()
    adatok = beFajl.readlines()
    for index in range(0, len(adatok), 1):
        daraboltSor = adatok[index].strip().split("@")
        peldany = Park_o.Park(daraboltSor[0], daraboltSor[1], daraboltSor[2], daraboltSor[3])
        adatokListaja.append(peldany)
    beFajl.close()
    return adatokListaja

def evekSzama(adatokListaja):
    szam=len(adatokListaja)
    print("III/A, B:")
    print(f"\tA vizsgált évek száma: {szam} db")

def atlagEv(adatokListaja):
    osszeg=0
    for index in range(0,len(adatokListaja),1):
        osszeg += adatokListaja[index].aszam

    atlag= osszeg/len(adatokListaja)
    print("III/C:")
    print(f"\tA 23 év alatt átlagos állatkert, vadaspark, kultúrpark száma: {atlag:.2f} db")
    return atlag
def legnagyobb(adatokListaja):
    maxIndex=0
    for index in range(0, len(adatokListaja), 1):
        if adatokListaja[index].latogatas>adatokListaja[maxIndex].latogatas:
            maxIndex=index
    szam= adatokListaja[maxIndex].latogatas
    ev= adatokListaja[maxIndex].ev
    print("III/D:")
    print(f"\tA legnagyobb látogatás szám: {szam*1000}, éve: {ev}")


def harmadik():
    adatokListaja=beolvas()
    evekSzama(adatokListaja)
    atlagEv(adatokListaja)
    legnagyobb(adatokListaja)
