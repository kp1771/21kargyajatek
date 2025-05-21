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
    jatekos1vegpontszam = sum (jatekos1)
    jatekos2 = []
    jatekos2.append(random.randint(2 , 11))
    jatekos2.append(random.randint(2 , 11))
    jatekos2vegpontszam = sum (jatekos2)

    print("Első Játékos:")
    print(" ")
    print(f"Ez az általad összesen elért pontszám: {jatekos1}")

    print("Második Játékos:")
    print(" ")
    print(f"Ez az általad összesen elért pontszám: {jatekos2}")
    if jatekos1vegpontszam == 21:
        print(" ")
        print("Gratulálok Első Játékos nyertél")
    elif jatekos2vegpontszam == 21:
        print("Gratulálok Második Játékos nyertél")
    elif jatekos1vegpontszam > 21:
        print("Első Játékos sajnos vesztettál túléptél 21-en")
    elif jatekos2vegpontszam > 21:
        print("Második Játékos sajnos vesztettál túléptél 21-en")
    elif jatekos1vegpontszam > jatekos2vegpontszam:
        print("Játékos1 nyertél")
    elif jatekosvegsopontszam < geposzpontszama:
        print("Játékos2 nyertél")
        print("vesztettél")
    elif geposzpontszama == 21:
        print(" ")
        print("A gép nyert:(")










if jatekmod =="gép":
    gepellen()
else:
    print("Érvénytelen játékmód ")

