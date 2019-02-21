import random

class Dicts():
    def __init__(self, id, name, URI, sprache1, sprache2):
        self.id = id
        self.name = name
        self.URI = URI
        self.sprache1 = sprache1
        self.sprache2 = sprache2
    def toDicts(self):
        return str(self.id) + " | " + self.name


class Entry:
    def __init__(self, deutsch, englisch):
        self.deutsch = deutsch
        self.englisch = englisch
    def toString(self):
        return self.deutsch + " - " + self.englisch

dictionarys = [Dicts(1, "Deutsch-Englisch", "Dictionarys/Deutsch-Englisch.txt", "Deutsch", "Englisch"),
               Dicts(2, "Deutsch-Latein", "Dictionarys/Deutsch-Latein.txt", "Deutsch", "Latein")]
Liste = []

#-------------------------------------------------------------------------------
# Funktionen für das Auswählen eines Dictionarys.
def dictausgabe():
    for dictionary in dictionarys:
        print(dictionary.toDicts())
    print("-----------------------------------------------------------------------------")
def URI():
    for i in range(len(dictionarys)):
        if Eingabe == dictionarys[i].id:
            return dictionarys[i].URI
def openURI(URI, mode):
    f = open(URI)
    file = f.read()
    raw_list = file.split("\n")
    raw_list.pop()
    for string in raw_list:
        Liste.append(string.split(":"))
    del(f, file, raw_list)

#-------------------------------------------------------------------------------
# Funktionen für das Abfragen der Vokabeln und und bearbeiten der Dictionarys.
#def while_letzte():
#    while Vokabel1 or Vokabel2 == letzte or vorletzte:
#        position = random.randint(1, len(Liste) - 1)
#        Vokabel1 = Liste[position][0]
#        Vokabel2 = Liste[position][1]

def ausgabe():
    print("-----------------------------------------------------------------------------")
    for eintrag in range(len(Liste)):
        print("".join(Liste[eintrag]))
    print("-----------------------------------------------------------------------------")

def eingabe():
    while True:
        file = open(URI(), "a")
        deutsch = input("deutsches Wort: ")
        if deutsch == "#fertig":
            break
        englisch = input("englisches Wort: ")
        if englisch == "#fertig":
            break
        file.write(deutsch + ", " + englisch + "\n")
        file.close()
        del(deutsch, englisch)

def entfernen():
    while True:
        f = open(URI(),"r")
        lines = f.readlines()
        print(lines)
        f.close()
        zuentfernen = input(" Tippe den kompletten Namen der zu entfernenden Vokabel ein. ")
        if zuentfernen == "#fertig":
            break
        f = open(URI(), "w")
        for line in lines:
            if line != "zuentfernen"+ "\n":
                f.write(line)
        f.close()



def abfrage():
    while True:
        # Wie rum sollen die Vokabel abgefragt werden (Deutsch->Englisch, Englisch->Deutsch, Deutsch<->Englisch).
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
            letzte = ""
            vorletzte = ""
            while True:
                # Vokabel wird ausgewählt
                position = random.randint(1, len(Liste) - 1)
                Vokabel1 = Liste[position][0]
                Vokabel2 = Liste[position][1]
                # Es wird überprüft ob die gewählte Vokabel bei den letzetn 2 mal Abfragen schon vorkam und wenn ja wird die Vokabel geändert.
                if Vokabel1 == letzte:
                    Vokabel1 = Liste[position+1][0]
                    Vokabel2 = Liste[position+1][1]
                elif Vokabel1 == vorletzte:
                    Vokabel1 = Liste[position+2][0]
                    Vokabel2 = Liste[position+2][1]
                uebersetzung = input("Englische Übersetzung von " + Vokabel1 + ": ")
                if uebersetzung == "#fertig":
                    print("-----------------------------------------------------------------------------")
                    break
                elif Vokabel2 == uebersetzung:
                    print("Korrekt.")
                else:
                    print("Leider Falsch. Korrekt ist: "+ Vokabel2)
                letzte = Vokabel1
                vorletzte = letzte
        # 2. Art des Abfragens der Vokabeln (Englisch->Deutsch).
        if abfrageint == 2:
            letzte = ""
            vorletzte = ""
            while True:
                # Vokabel wird ausgewählt
                position = random.randint(1, len(Liste) - 1)
                Vokabel1 = Liste[position][0]
                Vokabel2 = Liste[position][1]
                # Es wird überprüft ob die gewählte Vokabel bei den letzten 2 mal Abfragen schon vorkam, wenn ja wird die Vokabel geändert.
                if Vokabel1 == letzte:
                    Vokabel1 = Liste[position+1][0]
                    Vokabel2 = Liste[position+1][1]
                elif Vokabel1 == vorletzte:
                    Vokabel1 = Liste[position+2][0]
                    Vokabel2 = Liste[position+2][1]
                uebersetzung = input("Englische Übersetzung von " + Vokabel2 + ": ")
                #
                if uebersetzung == "#fertig":
                    print("-----------------------------------------------------------------------------")
                    break
                elif DeutschVokabel == uebersetzung:
                    print("Korrekt")
                else:
                    print("Leider Falsch. Korrekt ist: "+ Vokabel1)
                letzte = Vokabel1
                vorletzte = letzte
        # 3. Art des Abfragens der Vokabeln (Deutsch<->Englisch).
        if abfrageint == 3:
            letzte = ""
            vorletzte = ""
            while True:
                # Vokabel wird ausgewählt
                position = random.randint(1, len(Liste) - 1)
                Vokabel1 = Liste[position][0]
                Vokabel2 = Liste[position][1]
                # Es wird überprüft ob die gewählte Vokabel bei den letzetn 2 mal Abfragen schon vorkam und wenn ja wird die Vokabel geändert.
                if Vokabel1 or Vokabel2 == letzte:
                    Vokabel1 = Liste[position+1][0]
                    Vokabel2 = Liste[position+1][1]
                elif Vokabel1 or Vokabel2 == vorletzte:
                    Vokabel1 = Liste[position+2][0]
                    Vokabel2 = Liste[position+2][1]
                # Es wird zufällig eine Abfragerichtung ausgwählt.
                richtung = random.randint(0,1)
                if richtung == 0:
                    uebersetzung = input("Englische Übersetzung von " + Vokabel1 + ": ")
                    if uebersetzung == "#fertig":
                        print("-----------------------------------------------------------------------------")
                        break
                    elif Vokabel2 == uebersetzung:
                        print("Korrekt")
                    else:
                        print("Leider Falsch. Korrekt ist: "+ Vokabel2)
                elif richtung == 1:
                    uebersetzung = input("Englische Übersetzung von " + Vokabel2 + ": ")
                    if uebersetzung == "#fertig":
                        print("-----------------------------------------------------------------------------")
                        break
                    elif Vokabel1 == uebersetzung:
                        print("Korrekt")
                    else:
                        print("Leider Falsch. Korrekt ist: "+ Vokabel1)
                letzte = Vokabel1
                vorletzte = letzte



# Start anzeige des Programms.
print("""Mögliche Befehle sind:
#fertig um ein Menu zurückzugehen
#menu um in Hauptmenu zu gelangen
eingabe um Vokabeln zum dictionary hinzuzufügen,
abfrage um abgefragt zu werden,
ausgabe um alle gespeicherten Vokabeln auszugeben
-----------------------------------------------------------------------------
-----------------------------------------------------------------------------""")

while True:
    dictausgabe()
    Eingabe = int(input("welches dict? "))
    openURI(URI(), "r")
    while True:
        befehl = input("Befehl: ")
        if befehl == "bearbeiten":
            while True:
                befehl2 = input("eingabe oder entfernen? ")
                if befehl2 == "eingabe":
                    eingabe()
                elif befehl2 == "entfernen":
                    entfernen()
                elif befehl2 == "#fertig":
                    break
        elif befehl == "abfrage":
            abfrage()
        elif befehl == "ausgabe":
            ausgabe()
        elif befehl == "#fertig":
            print("-----------------------------------------------------------------------------")
            print("-----------------------------------------------------------------------------")
            break
