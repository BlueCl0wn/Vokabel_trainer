from Dicts import dicts

# Class für die Dictionarys und Informationen über diese.

dictionarys = [dicts(1, "Deutsch-Englisch", "Dictionarys/Deutsch-Englisch.txt", "Deutsch", "Englisch"),
               dicts(2, "Deutsch-Latein", "Dictionarys/Deutsch-Latein.txt", "Deutsch", "Latein")]
Liste = []

#-------------------------------------------------------------------------------
# Funktionen für das Auswählen eines Dictionarys.
def dictausgabe():
    for dictionary in dictionarys:
        print(dictionary.toDicts())
    print("-----------------------------------------------------------------------------")

def URI() -> str:
    for i in range(len(dictionarys)):
        if Eingabe == dictionarys[i].id:
            return dictionarys[i].URI

def openURI(URI : str, mode : str):
    f = open(URI)
    file = f.read()
    raw_list = file.split("\n")
    raw_list.pop()
    f.close()
    for string in raw_list:
        Liste.append(string.split(":"))
    del f, file, raw_list




    # Funktionen für die verschiedenen Möglichkeiten im Menu.
def bearbeiten(): # Öffnet das menu zum Auswählen ob man Vokebln hinzufügen oder entfernen möchte.
    while True:
        befehl2 = input("eingabe oder entfernen? ")
        if befehl2 == "eingabe":
            eingabe()
        elif befehl2 == "entfernen":
            entfernen()
        elif befehl2 == "#fertig":
            break


def eingabe(): # Menu in dem man Vokabeln zum ausgweählten Dictionary hinzufügen kann.
    while True:
        file = open(URI(), "a")
        deutsch = input("deutsches Wort: ")
        if deutsch == "#fertig":
            break
        englisch = input("englisches Wort: ")
        if englisch == "#fertig":
            break
        file.write(deutsch + ":" + englisch + "\n")
        file.close()
        del deutsch, englisch


def entfernen(): # Menu in dem man Vokabeln aus dem ausgweählten Dictionary entfernen kann.
    while True:
        f = open(URI(),"r")
        line = f.read()
        lines = line.split("\n")
        f.close()
        line = str(lines)
        print(line)
        zuentfernen = input(" Tippe den kompletten Namen der zu entfernenden Vokabel ein. ")
        if zuentfernen == "#fertig":
            break
        else:
            if zuentfernen in line:
                line = line.replace(zuentfernen, "")
                print("---------------")
            else:
                print("Diese Vokabel ist nicht verhanden.")
                print("---------------")
        del f, zuentfernen
        line = line.replace("[", "")
        line = line.replace("'", "")
        line = line.replace("]", "")
        line = line.replace(", ", "\n")
        line = line.replace("\n\n", "\n")
        f = open(URI(), "w")
        f.write(line)
        f.close()
        del lines, f, line
        print("-----------------------------------------------------------------------------")

def ausgabe(): # Gibt alle Vokabeln aus dem ausgwähltem Dictionary aus.
    print("-----------------------------------------------------------------------------")
    f = open(URI(),"r")
    line = f.read()
    lines = line.split("\n")
    lines.pop()
    f.close()
    for eintrag in range(len(lines)):
        Eintrag = lines[eintrag].split(":")
        print("".join(Eintrag[0] + " - " + Eintrag[1]))
    print("-----------------------------------------------------------------------------")
    del line, lines

def abfrage(): # Startet das Abfragen der Vokebeln.
    openURI(URI(), "r")
    while True:
        # Es wird abgefragt wie rum die Vokabel abgefragt werden sollen (Deutsch->Englisch, Englisch->Deutsch, Deutsch<->Englisch).
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
            vorvorletzte = ""
            while True:
                # Vokabel wird ausgewählt
                position = random.randint(1, len(Liste) - 1)
                Vokabel1 = Liste[position][0]
                Vokabel2 = Liste[position][1]
                # Es wird überprüft ob die gewählte Vokabel bei den letzetn 2 mal Abfragen schon vorkam, wenn ja wird die Vokabel geändert.
                if Vokabel1 == letzte or Vokabel1 == vorletzte or Vokabel1 == vorvorletzte:
                    while True:
                        position = random.randint(1, len(Liste) - 1)
                        Vokabel1 = Liste[position][0]
                        Vokabel2 = Liste[position][1]
                        if Vokabel1 != letzte and Vokabel1 != vorletzte and Vokabel1 != vorvorletzte:
                            break
                # Es wird die ausgewählte Vokabel ausgegeben und die Übersetzung soll eingetippt werden.
                uebersetzung = input("Übersetzung von " + Vokabel1 + ": ")
                if uebersetzung == "#fertig":
                    print("-----------------------------------------------------------------------------")
                    break
                elif Vokabel2 == uebersetzung:
                    print("Korrekt.")
                else:
                    print("Leider Falsch. Korrekt ist: "+ Vokabel2)
                vorvorletzte = vorletzte
                vorletzte = letzte
                letzte = Vokabel1
                del Vokabel1, Vokabel2

        # 2. Art des Abfragens der Vokabeln (Englisch->Deutsch).
        if abfrageint == 2:
            letzte = ""
            vorletzte = ""
            vorvorletzte = ""
            while True:
                # Vokabel wird ausgewählt
                position = random.randint(1, len(Liste) - 1)
                Vokabel1 = Liste[position][0]
                Vokabel2 = Liste[position][1]
                # Es wird überprüft ob die gewählte Vokabel bei den letzten 2 mal Abfragen schon vorkam, wenn ja wird die Vokabel geändert.
                if Vokabel1 == letzte or Vokabel1 == vorletzte or Vokabel1 == vorvorletzte:
                    while True:
                        position = random.randint(1, len(Liste) - 1)
                        Vokabel1 = Liste[position][0]
                        Vokabel2 = Liste[position][1]
                        if Vokabel1 != letzte and Vokabel1 != vorletzte and Vokabel1 != vorvorletzte:
                            break
                # Es wird die ausgewählte Vokabel ausgegeben und die Übersetzung soll eingetippt werden.
                uebersetzung = input("Übersetzung von " + Vokabel2 + ": ")
                #
                if uebersetzung == "#fertig":
                    print("-----------------------------------------------------------------------------")
                    break
                elif Vokabel1 == uebersetzung:
                    print("Korrekt")
                else:
                    print("Leider Falsch. Korrekt ist: "+ Vokabel1)
                vorvorletzte = vorletzte
                vorletzte = letzte
                letzte = Vokabel1
                del Vokabel1, Vokabel2

        # 3. Art des Abfragens der Vokabeln (Deutsch<->Englisch).
        if abfrageint == 3:
            letzte = ""
            vorletzte = ""
            vorvorletzte = ""
            while True:
                # Vokabel wird ausgewählt
                position = random.randint(1, len(Liste) - 1)
                Vokabel1 = Liste[position][0]
                Vokabel2 = Liste[position][1]
                # Es wird überprüft ob die gewählte Vokabel bei den letzetn 2 mal Abfragen schon vorkam und wenn ja wird die Vokabel geändert.
                if Vokabel1 == letzte or Vokabel1 == vorletzte or Vokabel1 == vorvorletzte:
                    while True:
                        position = random.randint(1, len(Liste) - 1)
                        Vokabel1 = Liste[position][0]
                        Vokabel2 = Liste[position][1]
                        if Vokabel1 != letzte and Vokabel1 != vorletzte and Vokabel1 != vorvorletzte:
                            break
                # Es wird zufällig eine Abfragerichtung ausgwählt.
                richtung = random.randint(0,1)
                if richtung == 0:
                    # Es wird die ausgewählte Vokabel ausgegeben und die Übersetzung soll eingetippt werden.
                    uebersetzung = input("Übersetzung von " + Vokabel1 + ": ")
                    if uebersetzung == "#fertig":
                        print("-----------------------------------------------------------------------------")
                        break
                    elif Vokabel2 == uebersetzung:
                        print("Korrekt")
                    else:
                        print("Leider Falsch. Korrekt ist: "+ Vokabel2)
                elif richtung == 1:
                    # Es wird die ausgewählte Vokabel ausgegeben und die Übersetzung soll eingetippt werden.
                    uebersetzung = input("Übersetzung von " + Vokabel2 + ": ")
                    if uebersetzung == "#fertig":
                        print("-----------------------------------------------------------------------------")
                        break
                    elif Vokabel1 == uebersetzung:
                        print("Korrekt")
                    else:
                        print("Leider Falsch. Korrekt ist: "+ Vokabel1)
                vorvorletzte = vorletzte
                vorletzte = letzte
                letzte = Vokabel1
                del Vokabel1, Vokabel2
