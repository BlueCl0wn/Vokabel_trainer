import random
from Dicts import dicts
from functions import *

version = 1.0





# def open_dict():#!!!!!!!!!!!!!!!!!!!

#-------------------------------------------------------------------------------




# Startanzeige des Programms.
print("Version " + str(version))
print("""Für eine erklärung des Programms siehe README.md
-----------------------------------------------------------------------------
-----------------------------------------------------------------------------
abfrage, entfernen, ausgabe, #fertig""")

while True:
    dictausgabe()
    Eingabe = int(input("welches dict? "))
    while True:
        befehl = input("Befehl: ")
        if befehl == "bearbeiten":
            bearbeiten()
        elif befehl == "abfrage":
            abfrage()
        elif befehl == "ausgabe":
            ausgabe()
        elif befehl == "#fertig":
            Liste = [] # Liste muss gelöscht werden, weil sonst beim Auswählen des nächsten Dictionarys dieses an Liste angehängt werden würde.
            print("-----------------------------------------------------------------------------")
            print("-----------------------------------------------------------------------------")
            break
