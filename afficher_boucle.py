# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 17:59:49 2023

@author: M. Hashas
"""

import time
import sys

# Liste des caractères à faire tourner
caracteres1 = ['/', '-', '\\']
caracteres2 = ['-', '_']

# Temps total d'exécution de la boucle (en secondes)
temps_total = 5

# Début de la boucle
debut = time.time()
while time.time() - debut < temps_total:

    for caractere1 in caracteres1:
        sys.stdout.write('\r' + caractere1)      # Réaffiche sur la même ligne
        sys.stdout.flush()
        time.sleep(0.1)                          # Attente de 0.2 seconde entre chaque caractère

sys.stdout.write('\n')                           # Saut de ligne pour terminer
