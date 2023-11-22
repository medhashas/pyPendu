# pyPendu : en python
Jeu (le fameux jeu du pendu), il est toujours joué par les colégiens lors des heures de permanences.
```
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
```
## Sommaire / Table of Contents
***
1. [Description](#Description-générale-du-programme)
2. [Algorithme](#Algo) 
3. [Statut](#statuts) du programme : développement - test 
4. [Modifications prévues](#Modifs) 
5. [Objectif du développement ](#) 
6. [Les exigences](#exigences) concernant l’environnement de développement  
7. [Installation](#installation) et Utilisation. 
8. [Technologies](#technologies) utilisées  
9. [Collaboration](#colaboration) souhaitée ? 
10. [Comment contourner un problème ?](#contourner-pb) 
11. [Comment appliquer les modifications ?](#appliquer-modifs) 
12. [Bugs connus](#bugs) 
13. [Corrections](#correction) éventuelles
14. [FAQ](#faq) 
15. [Droits d’auteurs](#Droits-dauteur) et informations sur la licence.

### Description
***
>Created on Sun Nov 19 08:53:32 2023
>>*Programme Python du jeu "Le Pendu" en version améliorée*
>>>@author : Mohammed Hashas

## Algorithme
***
- On fixe un mot choisi dans le dictionnaire dico_mots{} -> motAChercher         expl : 'SOLEIL' (mot caché)
- On demande à l'utilisateur de saisir une lettre
- On cherche la lettre dans le mot caché
   - Si elle est présente,
     . On récupère l'indice de la lettre saisie dans le mot caché                 expl : dans SOLEIL le 'L' a l'indice 2 et 5
     . Si la taille du tableau des indices est > 0 ET la lettre saisie                   ici la taille du tableau des indices = 2
     n'est pas parmis les lettres trouvées alors  On affiche message : "lettre présente"
     . On place le lettre dans le tableau lettres_trouvees exactements aux        expl : le 'L' sera placé à [2] et à [5] du tableau
       mêmes indices trouvés dans le mot caché                                               lettres_trouvees
```
        #Si la lettre est trouvée dans le mot caché
        if ( len(indices) > 0 and lettre_saisie not in lettres_trouvees):
            print(Fore.GREEN + "Lettre {} présente dans le mot.".format(lettre_saisie) + Style.RESET_ALL)
            for j in range(len(indices)):
                taille_mot += 1
                lettres_trouvees[int(indices[j])] = lettre_saisie
```
  - Si la lettre n'est pas trouvée dans le mot caché
     . On inscrit la lettre saisie dans le tableau des lettres non trouvées
     (Ce bloc nous permet d'afficher le bonhomme pendu à une potence)
     . Tant que le nb d'erreurs est < à la taille de la potence
     (à chaque fois que le joueur donne une lettre qui n'est pas dans
     . le mot caché, on affiche une ligne de la potence)
          . On vérifie si la lettre saisie a été déjà jouée,
          . ou pas,
          pour afficher autant de ligne du bonhomme qu'il y a d'erreurs

    si nb_err == taille de la potence) => PENDU : Fin du jeu !
```
        # Si la lettre n'est pas trouvée dans le mot caché        
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
```
- On affiche les lettres trouvées à leurs emplacement dans le squelette du mot caché    expl : _ _ L _ _
- puis on boucle sur la saisie de la lettre suivante.

## Statut
***  
En développement et test

## Modifications prévues
***
Les modifications prévues c'est d'écrire une version graphique, avec Tkinter

## Objectif du développement
Mon objectif premier, c'est de se perfectionner en Python en s'amusant :)



