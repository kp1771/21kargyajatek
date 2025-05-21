import random

print("🎴 Üdvözöllek a 21 kártyajátékban! 🎉")
print("")
jatekmod = input("Kivel szeretnéd játszani a játékot – gép 🤖 vagy játékos 🧑 ellen?: ")

def gepellen():
    gep = []
    gep.append(8)
    gep.append(6)
    geposzpontszama = sum(gep)
    jatekoskartya1 = random.randint(2, 11)
    jatekoskartya2 = random.randint(2, 11)

    jatekosvegsopontszam = jatekoskartya1 + jatekoskartya2
    print("")
    print(f"🃏 Ez az első kártyád pontszáma: {jatekoskartya1}")
    print("")
    print(f"🃏 Ez a második kártyád pontszáma: {jatekoskartya2}")
    print("")
    print(f"🤖 A gép ennyi pontot szerzett összesen: {geposzpontszama}")
    print("")
    print(f"🔢 Ez az általad összesen elért pontszám: {jatekosvegsopontszam}")
    
    if jatekosvegsopontszam == 21:
        print("")
        print("🎉 Gratulálok, nyertél! 🏆")
    elif jatekosvegsopontszam > geposzpontszama:
        print("🏆 Nyertél!")
    elif jatekosvegsopontszam < geposzpontszama:
        print("")
        print("😢 Vesztettél!")
    elif geposzpontszama == 21:
        print("")
        print("🤖 A gép nyert 😔")

def jatekosellen():
    jatekos1 = [random.randint(2, 11), random.randint(2, 11)]
    jatekos1vegpontszam = sum(jatekos1)
    jatekos2 = [random.randint(2, 11), random.randint(2, 11)]
    jatekos2vegpontszam = sum(jatekos2)

    print("🧑‍🎲 Első Játékos:")
    print(f"🔢 Lapjaid: {jatekos1} | Összpontszám: {jatekos1vegpontszam}")
    print("")
    print("🧑‍🤝‍🧑 Második Játékos:")
    print(f"🔢 Lapjaid: {jatekos2} | Összpontszám: {jatekos2vegpontszam}")
    
    if jatekos1vegpontszam == 21:
        print("\n🏆 Gratulálok Első Játékos, nyertél!")
    elif jatekos2vegpontszam == 21:
        print("\n🏆 Gratulálok Második Játékos, nyertél!")
    elif jatekos1vegpontszam > 21:
        print("\n❌ Első Játékos, sajnos túllépted a 21-et!")
    elif jatekos2vegpontszam > 21:
        print("\n❌ Második Játékos, sajnos túllépted a 21-et!")
    elif jatekos1vegpontszam > jatekos2vegpontszam:
        print("\n🏆 Első Játékos, te nyertél!")
    elif jatekos1vegpontszam < jatekos2vegpontszam:
        print("\n🏆 Második Játékos, te nyertél! 🎉")
    else:
        print("\n🤝 Döntetlen – egyikőtök sem nyert.")

if jatekmod.lower() == "gép":
    gepellen()
elif jatekmod.lower() == "játékos":
    jatekosellen()
else:
    print("⚠️ Érvénytelen játékmód! Kérlek, válassz 'gép' vagy 'játékos' módot.")
#.lower és a /n-t Chatgpt-től kérdeztem mint fejlesztési javaslat és be is építettem aés a füzetbe is leírtam/megtanultam