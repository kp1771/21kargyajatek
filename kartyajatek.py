import random
print("Üdvözöllek a 21 kartyajatekban")
jatekmod = input("kivel szeretnéd játszani a játékot gép vagy játékos ellen?:")

def gepellen():
    gep = []
    gep.append(8)
    gep.append(6)
    geposzpontszama = sum(gep)
    jatekoskartya1 = random.randint(2 ,11)
    jatekoskartya2 = random.randint(2 ,11)

    jatekosvegsopontszam = jatekoskartya1 + jatekoskartya2
    print(f"Ez az első kártyád pontszáma: {jatekoskartya1}")
    print(f"Ez a második kártyád pontszáma: {jatekoskartya2}")
    print(f"A gép ennyi pontot szerzett összesen: {geposzpontszama}")
    print(f"Ez az általad összesen elért pontszám: {jatekosvegsopontszam}")
    if jatekosvegsopontszam == 21:
        print(" ")
        print("Gratulálok nyertél")
    elif jatekosvegsopontszam > geposzpontszama:
        print("nyertél")
    elif jatekosvegsopontszam < geposzpontszama:
        print(" ")
        print("vesztettél")
    elif geposzpontszama == 21:
        print(" ")
        print("A gép nyert:(")
def jatekosellen():
    jatekos1 = []
    jatekos1.append(random.randint(2 , 11))
    jatekos1.append(random.randint(2 , 11))
    jatekos1végpontszam = sum (jatekos1)










if jatekmod =="gép":
    gepellen()
else:
    print("Érvénytelen játékmód ")

