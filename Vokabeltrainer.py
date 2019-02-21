import random

class Dicts():
    def __init__(self, id, name, URI, sprache1, sprache2):
        self.id = id
        self.name = name
        self.URI = URI
        self.sprache1 = sprache1
        self.sprache2 = sprache2
    def toDicts(self):
        return str(self.id) + " - " + self.name


class Entry:
    def __init__(self, deutsch, englisch):
        self.deutsch = deutsch
        self.englisch = englisch
    def toString(self):
        return self.deutsch + " - " + self.englisch

dictionarys = [Dicts(1, "Deutsch-Englisch", "C:/Users/Darek/Python_Scripts/Vokabel_Programm/Dictionarys/Deutsch-Englisch.txt", "Deutsch", "Englisch"),
               Dicts(2, "Deutsch-Latein", "C:/Users/Darek/Python_Scripts/Vokabel_Programm/Dictionarys/Deutsch-Latein.txt", "Deutsch", "Latein")]
eintraege = []
#-------------------------------------------------------------------------------
def URI():
    for i in range(len(dictionarys)):
        if input == dictionarys[i].id:
#           i = i
            return dictionarys[i].URI
def dictausgabe():
    for dictionary in dictionarys:
        print(dictionary.toDicts())
def openURI(URI):
    eintraege.append(open(URI)[3:])

#-------------------------------------------------------------------------------
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
        # Wie rum sollen die Vokabel abgefragt werden (Deutsch->Englisch, Englisch->Deutsch, Deutsch<->Englisch)
        abfrageart = input("Wie willst du abgefragt werden? Tippe für Deutsch -> Englisch = 1, für Englisch -> Deutsch = 2, für Deutsch <-> Englisch = 3. ")
        if abfrageart == "#fertig":
            print("-----------------------------------------------------------------------------")
            break
        try:
            abfrageint = int(abfrageart)
            abfrageint <= 3
        except:
            print("Nur die drei angegebenen Möglichkeiten. (1, 2, 3)")

        # 1. Art des Abfragens der Vokabeln (Deutsch->Englisch).
        if abfrageint == 1:
            while True:
                position = random.randint(1, len(eintraege) - 1)
                # Es wird überprüft ob die gewählte Vokabel bei den letzetn 2 mal Abfragen schon vorkam und wenn ja wird die Vokabel geändert.
                if uebersetung == letzte:
                    uebersetzung = eintraege[position + 1]
                if uebersetzung == vorletzte:
                    uebersetzung = eintraege[position + 2]
                uebersetzung = input("Englische Übersetzung von " + eintraege[position].deutsch + ": ")
                if uebersetzung == "#fertig":
                    print("-----------------------------------------------------------------------------")
                    break
                elif eintraege[position].englisch == uebersetzung:
                    print("Korrekt.")
                else:
                    print("Leider Falsch. Korrekt ist: "+ eintrage[position].englisch)

                letzte = uebersetzung
        # 2. Art des Abfragens der Vokabeln (Englisch->Deutsch).
        if abfrageint == 2:
            while True:
                position = random.randint(1, len(eintraege) - 1)
                # Es wird überprüft ob die gewählte Vokabel bei den letzetn 2 mal Abfragen schon vorkam und wenn ja wird die Vokabel geändert.
                if uebersetung == letzte:
                    uebersetzung = eintraege[position + 1]
                if uebersetzung == vorletzte:
                    uebersetzung = eintraege[position + 2]
                uebersetzung = input("Englische Übersetzung von " + eintraege[position].englisch + ": ")
                if uebersetzung == "#fertig":
                    print("-----------------------------------------------------------------------------")
                    break
                elif eintraege[position].deutsch == uebersetzung:
                    print("Korrekt")
                else:
                    print("Leider Falsch. Korrekt ist: "+ eintrage[position].deutsch)
                letzte = uebersetzung
                vorletzte = letzte

        # 3. Art des Abfragens der Vokabeln (Deutsch<->Englisch).
        if abfrageint == 3:
            while True:
                position = random.randint(1, len(eintraege) - 1)
                # Es wird überprüft ob die gewählte Vokabel bei den letzetn 2 mal Abfragen schon vorkam und wenn ja wird die Vokabel geändert.
                if uebersetung == letzte:
                    uebersetzung = eintraege[position + 1]
                if uebersetzung == vorletzte
                    uebersetzung = eintraege[position + 2]
                # Es wird zufällig eine Abfragerichtung ausgwählt.
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
                vorletzte = letzte

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
    dictausgabe()
    input = int(input("welches dict? "))
    eintraege.append(openURI(URI()))
    while True:
        befehl = input("Befehl: ")
        if befehl == "eingabe":
            eingabe()
        if befehl == "abfrage":
            abfrage()
        if befehl == "ausgabe":
            ausgabe()
