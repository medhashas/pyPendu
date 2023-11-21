# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 06:23:07 2023

@author: admin
"""

import random

from colorama import Fore, Style


# Dictionnaire avec les mots et leurs indications
mots_indications = {
    "PYTHON": "Langage de programmation",
    "PROGRAMMATION": "Processus de création de programmes",
    "ORDINATEUR": "Appareil électronique pour traiter des données",
    "DEVELOPPEUR": "Personne créant des logiciels",
    "JEU": "Activité ludique",
    "PENDU": "Jeu où il faut deviner des mots",
    "ALGORITHME": "Suite d'instructions permettant de résoudre un problème",
    "INTERFACE": "Point de contact entre un utilisateur et un système"
}

def choisir_mot_indication():
    mot, indication = random.choice(list(mots_indications.items()))
    return mot.upper(), indication

def afficher_mot_cache(mot, lettres_trouvees):
    mot_cache = ""
    for lettre in mot:
        if lettre in lettres_trouvees:
            mot_cache += lettre + " "
        else:
            mot_cache += "_ "
    return mot_cache

def jeu_pendu():
    mot_a_deviner, indication = choisir_mot_indication()
    lettres_trouvees = set()
    vies_restantes = 6

    print("Bienvenue au Jeu du Pendu!")
    print("Devinez le mot : indication = {}".format(indication))
    print(Fore.WHITE + Style.NORMAL + afficher_mot_cache(mot_a_deviner, lettres_trouvees) + Fore.WHITE)

    while vies_restantes > 0:
        lettre = input("Entrez une lettre: ").upper()

        if len(lettre) == 1 and lettre.isalpha():
            if lettre in lettres_trouvees:
                print(Fore.YELLOW + Style.NORMAL + "Vous avez déjà deviné cette lettre." + Fore.WHITE)
            elif lettre in mot_a_deviner:
                lettres_trouvees.add(lettre)
                mot_cache = afficher_mot_cache(mot_a_deviner, lettres_trouvees)
                print(Fore.GREEN + Style.NORMAL + "C'est la bonne lettre !, encore !" + Fore.WHITE)
                print(mot_cache)
                if "_" not in mot_cache:
                    print(Fore.GREEN + Style.NORMAL + "Félicitations! Vous avez trouvé le mot:" + Fore.WHITE, mot_a_deviner)
                    break
            else:
                vies_restantes -= 1
                print(Fore.RED + Style.NORMAL + "Lettre incorrecte! Il vous reste" , vies_restantes, "vies." + Fore.WHITE)
                if vies_restantes == 0:
                    print(Fore.RED + Style.NORMAL + "Désolé, vous avez perdu. Le mot était:" + Fore.WHITE, mot_a_deviner)
        else:
            print("Veuillez entrer une seule lettre valide.")

if __name__ == "__main__":
    jeu_pendu()
