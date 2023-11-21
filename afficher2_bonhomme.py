# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 17:59:49 2023

@author: admin
"""
import os
import time

import time
import sys

# Liste des caractères à faire tourner
caracteres = ['/', '-', '\\']

# Temps total d'exécution de la boucle (en secondes)
temps_total = 5

# Début de la boucle
debut = time.time()
while time.time() - debut < temps_total:
    for caractere in caracteres:
        sys.stdout.write(caractere + '\r')  # Utilisation de sys.stdout.write pour un affichage sans retour à la ligne
        sys.stdout.flush()  # Rafraîchissement de la sortie standard
        time.sleep(0.2)  # Attente de 0.2 seconde entre chaque caractère

sys.stdout.write('\n')  # Saut de ligne pour terminer
