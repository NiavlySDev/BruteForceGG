import requests
from random import choice as random
from time import sleep as wait
from datetime import datetime as current
from params import *

liens_valides = []

def GetLiens():
    alphabetM = ["t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n","o", "p", "q", "r", "s"]
    alphabetm = ["s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                 "n", "o", "p", "q", "r"]
    nombres = str(input("Nombres: "))
    separateur = str(input("Séparateur: "))
    nombresliste = nombres.split(separateur)
    lettres = []
    for nombre in nombresliste:
        lettres.append(int(nombre))
    caracteres = []
    liste_liens = []
    a = 0
    for lettre in lettres:
        if a % 2 == 0:
            if lettre < 26: caracteres.append(alphabetM[lettre].swapcase())
            if lettre >= 26 and lettre < 52: caracteres.append(alphabetM[lettre - 26].swapcase())
            if lettre >= 52: caracteres.append(alphabetM[lettre - 52].swapcase())
        else:
            if lettre < 26: caracteres.append(alphabetm[lettre])
            if lettre >= 26 and lettre < 52: caracteres.append(alphabetm[lettre - 26])
            if lettre >= 52: caracteres.append(alphabetm[lettre - 52])
        a += 1
    caracteres = [caracteres[0] + caracteres[1], caracteres[2] + caracteres[3], caracteres[4] + caracteres[5],
                  caracteres[6] + caracteres[7]]
    for a in caracteres:
        for b in caracteres:
            if a != b:
                for c in caracteres:
                    if a != c and b != c:
                        for d in caracteres:
                            if a != d and b != d and c != d:
                                liste_liens.append("https://bit.ly/" + a + b + c + d)
                                liste_liens.append(
                                    "https://bit.ly/" + a.swapcase() + b.swapcase() + c.swapcase() + d.swapcase())
    return liste_liens

def Main():
    file = open("BonsLiens.txt","a")
    test_en_cours = 0
    for lien in GetLiens():
        test_en_cours+=1
        reponse = requests.get(lien)
        if(reponse.status_code == 409):
            while(reponse.status_code == 409):
                if (ARRET_SCRIPT_SI_TMR == True):
                    print("Trop de Requêtes! Fin de la Boucle")
                    exit("Fin")
                else:
                    now = current.now()
                    current_time = now.strftime("%H:%M:%S")
                    file.write(current_time + " - Trop de Requêtes!\n")
                    print("Trop de Requêtes! Attente:")
                    timer = DUREE_ATTENTE_TMR
                    while timer > 0:
                        print("TMR: " + str(timer) + "s Restantes")
                        wait(INTERVALLE_AFFICHAGE_TIMER)
                        timer -= INTERVALLE_AFFICHAGE_TIMER
                reponse = requests.get(lien)
        if(reponse.ok == True):
            print("Test n°"+str(test_en_cours)+": Lien Fonctionnel! ("+lien+")")
            now = current.now()
            current_time = now.strftime("%H:%M:%S")
            file.write(current_time+" - Test n°"+str(test_en_cours)+": Lien Fonctionnel! ("+lien+")\n")
        if(reponse.ok == False):
            if(AFFICHAGE_ERRONE == True):
                print("Test n°" + str(test_en_cours) + ": Lien Erroné! ("+lien+")")