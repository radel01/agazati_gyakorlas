import random


def listabaBeir():
    print("II/A, B, C:")
    print("\t", end="")
    lista = []
    for index in range(0, 11, 1):
        szamok = random.randint(-100, 1024)
        print(szamok, end="$")
        lista.append(szamok)
    utolsoSzam = random.randint(-100, 1024)
    print(utolsoSzam)
    lista.append(utolsoSzam)
    return lista


def otteloszthatoak_szama(lista):
    db = 0
    for index in range(0, len(lista)):
        if lista[index] % 5 == 0:
            db += 1
    return db


def konzolra_ir(db):
    print("II/D, E:")
    print(f"\tAz 5-el oszthatóak száma: {db}")


def fajlba_kiir(db):
    beFajl = open("kimutatas.txt", "w", encoding="utf-8")
    print("II/F:", file=beFajl)
    print(f"\tAz 5-el oszthatóak száma: {db}", file=beFajl)
    beFajl.close()


def masodik():
    lista = listabaBeir()
    db = otteloszthatoak_szama(lista)
    konzolra_ir(db)
    fajlba_kiir(db)
