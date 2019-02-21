import random

dictionarys = open("C:/Users/Darek/Python_Scripts/Vokabel Programm/dictionarys.txt", "r")
print(dictionarys)
URI = dictionarys[input("Name of the dictionary you want to work with.")]
eintraege = open(URI)

#fgdfadfgfghfghhgfhgfhhsfhgfhfshgfhssghgfhsghsfghssghgadfgfghfghhgfhgfhhsfhgfhfshgfhssghgfhsghsfghssghg
#ydfbgsdgsadfgfghfghhgfhgfhhsfhgfhfshgfhssghgfhsghsfghssghgadfgfghfghhgfhgfhhsfhgfhfshgfhssghgfhsghsfghssghg
#adfgfghfghhgfhgfhhsfhgfhfshgfhssghgfhsghsfghssghgadfgfghfghhgfhgfhhsfhgfhfshgfhssghgfhsghsfghssghg
#gfgasdgadfgfghfghhgfhgfhhsfhgfhfshgfhssghgfhsghsfghssghgadfgfghfghhgfhgfhhsfhgfhfshgfhssghgfhsghsfghssghg
#sdfgsgsgfgadfgfghfghhgfhgfhhsfhgfhfshgfhssghgfhsghsfghssghgadfgfghfghhgfhgfhhsfhgfhfshgfhssghgfhsghsfghssghg
#agadfgfghfghhgfhgfhhsfhgfhfshgfhssghgfhsghsfghssghgadfgfghfghhgfhgfhhsfhgfhfshgfhssghgfhsghsfghssghg

class Entry:
    def __init__(self, deutsch, englisch):
        self.deutsch = deutsch
        self.englisch = englisch
    def toString(self):
        return self.deutsch + " - " + self.englisch

def eingabe():
    while True:
        deutsch = input("deutsches Wort: ")
        if deutsch == "#fertig":
            break
        englisch = input("englisches Wort: ")
        if englisch == "#fertig":
            break
        eintraege.append(Entry(deutsch, englisch))

def abfrage():
    while True:
        abfrageart = input("Wie willst du abgefragt werden? Tippe für Deutsch -> Englisch = 1, für Englisch -> Deutsch = 2, für Deutsch <-> Englisch = 3. ")
        if abfrageart == "#fertig":
            print("-----------------------------------------------------------------------------")
            break
        try:
            abfrageint = int(abfrageart)
            abfrageint <= 3
        except:
            print("Nur die drei angegebenen Möglichkeiten. (1, 2, 3)")
        if abfrageint == 1:
            while True:
                position = random.randint(1, len(eintraege) - 1)
                if uebersetung == letzte:
                    uebersetzung = eintraege[position + 1]
                uebersetzung = input("Englische Übersetzung von " + eintraege[position].deutsch + ": ")
                if uebersetzung == "#fertig":
                    print("-----------------------------------------------------------------------------")
                    break
                elif eintraege[position].englisch == uebersetzung:
                    print("Korrekt.")
                else:
                    print("Leider Falsch. Korrekt ist: "+ eintrage[position].englisch)
                letzte = uebersetzung
        if abfrageint == 2:
            while True:
                position = random.randint(1, len(eintraege) - 1)
                if uebersetung == letzte:
                    uebersetzung = eintraege[position + 1]
                uebersetzung = input("Englische Übersetzung von " + eintraege[position].englisch + ": ")
                if uebersetzung == "#fertig":
                    print("-----------------------------------------------------------------------------")
                    break
                elif eintraege[position].deutsch == uebersetzung:
                    print("Korrekt")
                else:
                    print("Leider Falsch. Korrekt ist: "+ eintrage[position].deutsch)
                letzte = uebersetzung
        if abfrageint == 3:
            while True:
                position = random.randint(1, len(eintraege) - 1)
                if uebersetung == letzte:
                    uebersetzung = eintraege[position + 1]
                richtung = random.randint(0,1)
                if richtung == 0:
                    uebersetzung = input("Englische Übersetzung von " + eintraege[position].deutsch + ": ")
                    if uebersetzung == "#fertig":
                        print("-----------------------------------------------------------------------------")
                        break
                    elif eintraege[position].englisch == uebersetzung:
                        print("Korrekt")
                    else:
                        print("Leider Falsch. Korrekt ist: "+ eintrage[position].englisch)
                elif richtung == 1:
                    uebersetzung = input("Englische Übersetzung von " + eintraege[position].englisch + ": ")
                    if uebersetzung == "#fertig":
                        print("-----------------------------------------------------------------------------")
                        break
                    elif eintraege[position].deutsch == uebersetzung:
                        print("Korrekt")
                    else:
                        print("Leider Falsch. Korrekt ist: "+ eintrage[position].deutsch)
                letzte = uebersetzung

def ausgabe():
    for eintrag in eintraege:
        print(eintrag.toString())

print("""Mögliche Befehle sind:
#fertig um ein Menu zurückzugehen
#menu um in Hauptmenu zu gelangen
eingabe um Vokabeln zum dictionary hinzuzufügen,
abfrage um abgefragt zu werden,
ausgabe um alle gespeicherten Vokabeln auszugeben
----------------------------------------------------------------------------""")

while True:
    befehl = input("Befehl: ")
    if befehl == "eingabe":
        eingabe()
    if befehl == "abfrage":
        abfrage()
    if befehl == "ausgabe":
        ausgabe()
