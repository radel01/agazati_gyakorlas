import random


def elso():
    print(f"I/A, B: ")
    kod = input("\tItal kódja: ")
    int(input("\tDarabszáma: "))

    lehetsegesBetu = ["A", "B", "C", "D", "H"]
    lehetsegesSzam = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print("I/C:")

    if len(kod) == 2:
        if kod[0] in lehetsegesBetu:
            if int(kod[1]) in lehetsegesSzam:
                if kod[0] == "A":
                    print("\tKiadott ital: Fanta")
                elif kod[0] == "B":
                    print("\tKiadott ital: Lipton")
                elif kod[0] == "C":
                    print("\tKiadott ital: Sprite")
                elif kod[0] == "D":
                    print("\tKiadott ital: Víz")
                elif kod[0] == "H":
                    print("\tKiadott ital: Coca-cola")
            else:
                print("\tNincs ilyen oszlop.")
        else:
            print("\tNincs ilyen sor.")
    elif len(kod) == 3:
        if kod[0] in lehetsegesBetu:
            if int(kod[2]) == 0:
                if kod[0] == "A":
                    print("\tKiadott ital: Fanta")
                elif kod[0] == "B":
                    print("\tKiadott ital: Lipton")
                elif kod[0] == "C":
                    print("\tKiadott ital: Sprite")
                elif kod[0] == "D":
                    print("\tKiadott ital: Víz")
                elif kod[0] == "H":
                    print("\tKiadott ital: Coca-cola")
            else:
                print("\tNincs ilyen oszlop.")
        else:
            print("\tNincs ilyen sor.")

    szam = random.randint(0, 10)
    if szam == 10:
        print(f"\tNyerőszám: {szam} -> Ön nyert: Vendégünk az üdítőre")
    else:
        print(f"\tNyerőszám: {szam} -> Ma sajnos nem nyert ingyen üdítőt!")
