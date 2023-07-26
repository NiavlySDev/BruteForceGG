import requests
from random import choice as random
from time import sleep as wait
from datetime import datetime as current
from params import *

liens_valides = []

def GetLiens():
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    caracteres = []
    for i in range(4):
        caracteres.append(random(alphabet).swapcase()+random(alphabet))
    liens_a_tester = []
    for a in caracteres:
        for b in caracteres:
            if a!=b:
                for c in caracteres:
                    if a!=c and b!=c:
                        for d in caracteres:
                            if a!=d and b!=d and c!=d:
                                liens_a_tester.append(f"https://bit.ly/{a}{b}{c}{d}")
    return liens_a_tester

def Main():
    file = open("BonsLiens.txt","a")
    tests_a_faire = int(input("Tests: "))  # Nombre de Tests a Faire
    test_en_cours = 0
    nombre_avant_anti_TMR = 0
    while test_en_cours <= tests_a_faire:
        for lien in GetLiens():
            test_en_cours+=1
            nombre_avant_anti_TMR+=1
            reponse = requests.get(lien)
            if(reponse.status_code == 429):
                while(VerifyTMR() == True):
                    if(ARRET_SCRIPT_SI_TMR == True):
                        print("Trop de Requêtes! Fin de la Boucle")
                        exit("Fin")
                    else:
                        now = current.now()
                        current_time = now.strftime("%H:%M:%S")
                        file.write(current_time+" - Trop de Requêtes!\n")
                        print("Trop de Requêtes! Attente:")
                        RunTimer(DUREE_ATTENTE_TMR, "TMR")
            if(reponse.ok == True):
                print("Test n°"+str(test_en_cours)+": Lien Fonctionnel! ("+lien+")")
                now = current.now()
                current_time = now.strftime("%H:%M:%S")
                file.write(current_time+" - Test n°"+str(test_en_cours)+": Lien Fonctionnel! ("+lien+")\n")
            if(reponse.ok == False):
                if(AFFICHAGE_ERRONE == True):
                    print("Test n°" + str(test_en_cours) + ": Lien Erroné!")
            if (nombre_avant_anti_TMR == NOMBRE_TEST_AVANT_ANTI_TMR):
                nombre_avant_anti_TMR=0
                print("Anti Too Many Requests: (Tests Réalisés: "+str(test_en_cours)+")")
                RunTimer(DUREE_ANTI_TMR, "ATMR")

def RunTimer(secondes, title):
    while secondes > 0:
        print(title+": "+str(secondes)+"s Restantes.")
        wait(INTERVALLE_AFFICHAGE_TIMER)
        secondes -= INTERVALLE_AFFICHAGE_TIMER

def VerifyTMR():
    reponse = requests.get("https://bit.ly/TestTMR")
    return reponse.status_code == 429
