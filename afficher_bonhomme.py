# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 17:47:36 2023

@author: admin
"""

import os
import time

def afficher_bonhomme_pendu(potence):
    for element, representation in potence.items():
        os.system('cls' if os.name == 'nt' else 'clear')  # Efface l'écran de la console
        print(f"{element}: {representation}")  # Affiche l'élément actuel du bonhomme pendu
        time.sleep(1)  # Attend 1 seconde avant de passer à l'étape suivante

# Exemple de potence du bonhomme pendu
potence2 = {
    'p_head1': '#                   ┌──┐     ',
    'p_head2': '#                  /┘  ║     ',
    'p_yeaux': '#                 /  (@|@)   ',
    'p_bouche': '#               /    (┴)    ',
    'p_corde_cou': '#           /      ¥     ',
    'p_bras_hauts': '#         /     / ║ \\  ',
    'p_bras_avant': '#        /      \ ║ //  ',
    'p_tronc': '#            /         ║     ',
    'p_cuisses': '#         /        // \\   ',
    'p_jambes': '#         /        //   \\  ',
    'p_chaussures': '#    /         &     &  ',
    'p_socle': '#      __/__                 ',
}

# Affichage progressif du bonhomme pendu
afficher_bonhomme_pendu(potence)
