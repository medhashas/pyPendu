# -*- coding: utf-8 -*-
"""
    Created on Sun Nov 19 08:53:32 2023

    Programme Python du jeu "Le Pendu" en version améliorée

    @author : Mohammed Hashas

"""


import time
import random
import sys
from colorama import Fore, Style

#from synonymes import linternaute

global tabl_stats

dico_mots = {
    "PYTHON": "Langage de programmation",
    "PROGRAMMATION": "Processus de création de programmes",
    "ORDINATEUR": "Appareil électronique pour traiter des données",
    "DEVELOPPEUR": "Personne créant des logiciels",
    "JEU": "Activité ludique",
    "PENDU": "Jeu où il faut deviner des mots",
    "ALGORITHME": "Suite d'instructions permettant de résoudre un problème",
    "INTERFACE": "Point de contact entre un utilisateur et un système",
    "GUITARE": "Instrument de musique à cordes",
    "ELEPHANT": "Animal terrestre de grande taille",
    "SOLEIL": "Étoile au centre de notre système solaire",
    "LUNE" : "Planète",
    "KILOGRAMME" : "Unité de mesure",
    "BOMBARDEMENTS" : "Mitraillage",
    "ENREGISTREMENTS" : "Inscription",
    "RÉMUNÉRATION" : "Émolument",
    "MÉSOPOTAMIE" : "Située au proche-orient",
    "VALENCIENNES" : "Commune en France",
    "ILLUSTRATIONS" : "Consécration",
    "RAPPROCHEMENT" : "Entente",
    "FOOTBALL" : "Un sport populaire"

}

potence = [
    '                            ',   # 19
    '    ▓                       ',   # 18
    '   ▀▓▀▀▀▀▀▀▀▀▀▀▀▀▀▓         ',   # 17
    '    ▓             ╚══╗      ',   # 16
    '    ▓                ║      ',   # 15
    '    ▓               ~^~     ',   # 14
    '    ▓              (@|@)    ',   # 13
    '    ▓                ¥\'    ',   # 12
    '    ▓             ╔══╬══╗   ',   # 11
    '    ▓            //(.║.)\\\ ',   # 10
    '    ▓             \ .║.  /  ',   # 9
    '    ▓               .║.     ',   # 8
    '    ▓             //( )\\\  ',   # 7
    '    ▓             //   \\\  ',   # 6
    '    ▓             |     |   ',   # 5
    '    ▓             &     &   ',   # 4
    '    ▓                       ',   # 3
    '    ▓                       ',   # 2
    '    ▓ /                     ',   # 1
    '  __▓/___▄                  ',   # 0
]



"""
    Algo :
        - On fixe un mot choisi dans le dictionnaire dico_mots{} -> motAChercher         expl : 'SOLEIL' (mot caché)
        - On demande à l'utilisateur de saisir une lettre

        - On cherche la lettre dans le mot caché
        - # Si elle est présente,
            . On récupère l'indice de la lettre saisie dans le mot caché                     expl : dans SOLEIL le 'L' a l'indice 2 et 5
            . Si la taille du tableau des indices est > 0 ET la lettre saisie                       ici la taille du tableau des indices = 2
            . On affiche message : "lettre présente"
            . On place le lettre dans le tableau lettres_trouvees exactements aux            expl : le 'L' sera placé à [2] et à [5] du tableau
              mêmes indices trouvés dans le mot caché                                               lettres_trouvees

        - # Si la lettre n'est pas trouvée dans le mot caché
            On inscrit la lettre saisie dans le tableau des lettres non trouvées
            (Ce bloc nous permet d'afficher le bonhomme pendu à une potence)
            Tant que le nb d'erreurs est < à la taille de la potence
            (à chaque fois que le joueur donne une lettre qui n'est pas dans
             le mot caché, on affiche une ligne de la potence)
                . On vérifie si la lettre saisie a été déjà jouée,
                . ou pas,
                pour afficher autant de ligne du bonhomme qu'il y a d'erreurs

                si nb_err == taille de la potence)
                    => PENDU : Fin du jeu !
        - On affiche les lettres trouvées à leurs emplacement dans le squelette du mot caché    expl : _ _ L _ _ L
        - puis on boucle sur la saisie de la lettre suivante.

"""


tabl_stats = []

def afficher_stats(tabl_stats):
    # Recherche de la longueur maximale des éléments dans chaque colonne pour l'alignement
    longueurs_colonnes = [max(len(row[col]) for row in tabl_stats) for col in range(len(tabl_stats[0]))]

    # Affichage du tableau avec un formatage cadré
    for row in tabl_stats:
      if row[-1] == "-1":
        row[-1] = ""
        s = ""
      else:
        s = " "
      print( s.join(row[col].ljust(longueurs_colonnes[col]) for col in range(len(row))))
    return tabl_stats


def boucle_patienter(t):
    # Liste des caractères à faire tourner
    caracteres1 = ['/', '-', '\\']
    caracteres2 = ['-', '_']

    # Temps total d'exécution de la boucle (en secondes)
    temps_total = t

    # Début de la boucle
    debut = time.time()
    while time.time() - debut < temps_total:

        for caractere1 in caracteres1:
            sys.stdout.write('\r' + caractere1)      # Réaffiche sur la même ligne
            sys.stdout.flush()
            time.sleep(0.1)                          # Attente de 0.2 seconde entre chaque caractère

    sys.stdout.write('\n')

def afficher_bonhomme_pendu(etapes):
    for etape in etapes:
        print(etape)

def tirer_mot_O_hasard():
    mot, indication = random.choice(list(dico_mots.items()))
    return mot.upper(), indication

def remplir_traces_vide(mot, lettres_trouvees):
    print("type l t : {}, taille l t : {}, len mot : {}".format(type(lettres_trouvees), len(lettres_trouvees), len(mot)))
    s = "_"
    for k in range(len(mot)):
        lettres_trouvees.append(s)

    return lettres_trouvees

def chercher_indices_lettre(lettre, mot):
    indices = [index for index, char in enumerate(mot) if char == lettre]

    return indices

def imprimer_mot_trace(lettres_trouvees):
    s_mot = ""
    for indx in range(len(lettres_trouvees)):
        s_mot += lettres_trouvees[indx] + " "
    print("progression de remplissage : {}".format(s_mot))

def jouer_O_pendu():
    motAChercher, indication = tirer_mot_O_hasard()
    lettres_trouvees = []
    lettres_non_trouvees = []

    #nb_jeux = 3

    print("________Bienvenue au Jeu du Pendu !________")
    print("Devinez le mot : indication = {}".format(indication))
    print(remplir_traces_vide(motAChercher, lettres_trouvees))   # affiche trace vide

    taille_mot = 0
    nb_err = 1
    ss =""
    tabl_stats = [
        ["┌─────────────┐", "", "", ""],
        ["│ ■ Stats jeu │", "", "", ""],
        ["├─────────────┼", "───┐", "", "-1"]
    ]
    while motAChercher != lettres_trouvees :
        lettre_saisie = input("Entrez une lettre : ").upper()

        # On cherche la lettre dans le mot caché
        indices = chercher_indices_lettre(lettre_saisie, motAChercher)

        # Si la lettre est trouvée dans le mot caché
        if ( len(indices) > 0 and lettre_saisie not in lettres_trouvees):
            print(Fore.GREEN + "Lettre {} présente dans le mot.".format(lettre_saisie) + Style.RESET_ALL)
            for j in range(len(indices)):
                taille_mot += 1
                lettres_trouvees[int(indices[j])] = lettre_saisie

        # Si la lettre n'est pas trouvée dans le mot caché
        else:
            nb_err += 1
            lettres_non_trouvees.append(lettre_saisie)
            while nb_err < len(potence):
                if lettre_saisie in lettres_trouvees:
                    print(Fore.LIGHTRED_EX + "Lettre {} déjà jouée.".format(lettre_saisie) + Style.RESET_ALL)
                else:
                    print(Fore.MAGENTA + "Lettre {} ne fait pas partie du mot.".format(lettre_saisie) + Style.RESET_ALL)

                for i in range(nb_err):
                    ss += potence[(nb_err)] + "\n"
                    print(Fore.CYAN + ss + Style.RESET_ALL)
                    break
                break

            if nb_err == len(potence):
                print("PENDU : Fin du jeu !")
                break

        imprimer_mot_trace(lettres_trouvees)

        nb_essais = nb_err + len(motAChercher)
        if( taille_mot == len(motAChercher)):
            print("Mot complété, Bravo !")
            boucle_patienter(10)

            #print("\nGAGNÉ : Mot trouvé : {}".format(lettres_trouvees))

            tabl_stats.append(["│Nb. d'essais │" , str(nb_essais-1) + " " , "" , ""])
            tabl_stats.append(["│Nb. d'erreur │" , str(nb_err-1) + "  " , "" , ""])
            tabl_stats.append(["└─────────────┴" , "───┘" , "" , "-1"])

            afficher_stats(tabl_stats)

            break


if __name__ == "__main__":
    jouer_O_pendu()
