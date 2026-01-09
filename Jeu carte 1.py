from tkinter import *
import random
import Class_jeu_1
from os import chdir
import time
import numpy as np
from PIL import Image
chdir('C:\\Users\\trist\\OneDrive\\Bureau\\nécessaire_de_programmation')


current_key = None
movement_active = False


# Fonctions déplacement carte


def clavierbis(event):
    global current_key, movement_active, coords

    if event.type == "2":  # KeyPress event
        current_key = event.keysym
        if not movement_active:
            movement_active = True
            move_rectangle()
        handle_action_key(current_key) # On appelle la fonction d'interaction ici
    elif event.type == "3":  # KeyRelease event
        current_key = None
        movement_active = False


def move_rectangle():
    global current_key, movement_active, coords
    active_fenetre = affiche_canvas_carte()
    if current_key is None:
        movement_active = False
        return
    touche = current_key
    test = True
    if touche == "Up" or touche == "Down" or touche == "Right" or touche == 'Left':
        global repousse_var
        if repousse_var != (0, 0):
            repousse_var = (repousse_var[0] + 1, repousse_var[1])
            if repousse_var[0] >= repousse_var[1]:
                vartextupdate_carte("Votre repousse a cessé de faire effet !")
                repousse_var = (0, 0)
                time.sleep(0.1)
        else:
            hautes_hrbes(liste_canvas_obstacles_herbes_capteurs[affiche_reste_carte()][2])

    if touche == "Up":
        if affiche_canvas_carte().coords(liste_canvas_obstacles_herbes_capteurs[affiche_reste_carte()][4])[1] >= 0:
            for i in range(len(liste_capteurss())):
                if verif_collision_carte(liste_canvas_obstacles_herbes_capteurs[affiche_reste_carte()][4], liste_capteurss(), affiche_canvas_carte())[i][0]:
                    if capteur_collision(liste_capteurss()[i]):
                        test = False
                        affiche_canvas_carte().unbind('<KeyPress>')
                        affiche_canvas_carte().unbind('<KeyRelease>')
                        changement_carte()
                        if coords[0] >= 700:
                            coords = (coords[0] - 690, coords[1])
                        if coords[0] <= 0:
                            coords = (coords[0] + 690, coords[1])
                        if coords[1] >= 550:
                            coords = (coords[0], coords[1] - 540)
                        if coords[1] <= 0:
                            coords = (coords[0], coords[1] + 540)
                        affiche_canvas_carte().bind('<KeyPress>', clavierbis)
                        affiche_canvas_carte().bind('<KeyRelease>', clavierbis)
                        move_rectangle()
                        break
            for obstacle in liste_canvas_obstacles_herbes_capteurs[affiche_reste_carte()][1]:
                if verif_collision_carte(liste_canvas_obstacles_herbes_capteurs[affiche_reste_carte()][4], [obstacle], affiche_canvas_carte())[0][0]:
                    if affiche_canvas_carte().coords(liste_canvas_obstacles_herbes_capteurs[affiche_reste_carte()][4])[1] == affiche_canvas_carte().coords(obstacle)[3]:
                        test = False
                        break
            if test:
                coords = (coords[0], coords[1] - 10)
    elif touche == "Down":
        if affiche_canvas_carte().coords(liste_canvas_obstacles_herbes_capteurs[affiche_reste_carte()][4])[3] < affiche_canvas_carte().winfo_height():
            for i in range(len(liste_capteurss())):
                if verif_collision_carte(liste_canvas_obstacles_herbes_capteurs[affiche_reste_carte()][4], liste_capteurss(), affiche_canvas_carte())[i][0]:
                    if capteur_collision(liste_capteurss()[i]):
                        test = False
                        affiche_canvas_carte().unbind('<KeyPress>')
                        affiche_canvas_carte().unbind('<KeyRelease>')
                        changement_carte()
                        if coords[0] >= 700:
                            coords = (coords[0] - 690, coords[1])
                        if coords[0] <= 0:
                            coords = (coords[0] + 690, coords[1])
                        if coords[1] >= 550:
                            coords = (coords[0], coords[1] - 540)
                        if coords[1] <= 0:
                            coords = (coords[0], coords[1] + 540)
                        affiche_canvas_carte().bind('<KeyPress>', clavierbis)
                        affiche_canvas_carte().bind('<KeyRelease>', clavierbis)
                        move_rectangle()
                        break
            for obstacle in liste_canvas_obstacles_herbes_capteurs[affiche_reste_carte()][1]:
                if verif_collision_carte(liste_canvas_obstacles_herbes_capteurs[affiche_reste_carte()][4], [obstacle], affiche_canvas_carte())[0][0]:
                    if affiche_canvas_carte().coords(liste_canvas_obstacles_herbes_capteurs[affiche_reste_carte()][4])[3] == affiche_canvas_carte().coords(obstacle)[1]:
                        test = False
                        break
            if test:
                coords = (coords[0], coords[1] + 10)
    elif touche == "Right":
        if affiche_canvas_carte().coords(liste_canvas_obstacles_herbes_capteurs[affiche_reste_carte()][4])[2] < affiche_canvas_carte().winfo_width():
            for i in range(len(liste_capteurss())):
                if verif_collision_carte(liste_canvas_obstacles_herbes_capteurs[affiche_reste_carte()][4], liste_capteurss(), affiche_canvas_carte())[i][0]:
                    if capteur_collision(liste_capteurss()[i]):
                        test = False
                        affiche_canvas_carte().unbind('<KeyPress>')
                        affiche_canvas_carte().unbind('<KeyRelease>')
                        changement_carte()
                        if coords[0] >= 700:
                            coords = (10, coords[1])
                        if coords[0] <= 0:
                            coords = (690, coords[1])
                        if coords[1] >= 550:
                            coords = (coords[0], 10)
                        if coords[1] <= 0:
                            coords = (coords[0], 540)
                        affiche_canvas_carte().bind('<KeyPress>', clavierbis)
                        affiche_canvas_carte().bind('<KeyRelease>', clavierbis)
                        move_rectangle()
                        break
            for obstacle in liste_canvas_obstacles_herbes_capteurs[affiche_reste_carte()][1]:
                if verif_collision_carte(liste_canvas_obstacles_herbes_capteurs[affiche_reste_carte()][4], [obstacle], affiche_canvas_carte())[0][0]:
                    if affiche_canvas_carte().coords(liste_canvas_obstacles_herbes_capteurs[affiche_reste_carte()][4])[2] == affiche_canvas_carte().coords(obstacle)[0]:
                        test = False
                        break
            if test:
                coords = (coords[0] + 10, coords[1])
    elif touche == "Left":
        if affiche_canvas_carte().coords(liste_canvas_obstacles_herbes_capteurs[affiche_reste_carte()][4])[0] >= 0:
            for i in range(len(liste_capteurss())):
                if verif_collision_carte(liste_canvas_obstacles_herbes_capteurs[affiche_reste_carte()][4], liste_capteurss(), affiche_canvas_carte())[i][0]:
                    if capteur_collision(liste_capteurss()[i]):
                        test = False
                        affiche_canvas_carte().unbind('<KeyPress>')
                        affiche_canvas_carte().unbind('<KeyRelease>')
                        changement_carte()
                        if coords[0] >= 700:
                            coords = (10, coords[1])
                        if coords[0] <= 0:
                            coords = (690, coords[1])
                        if coords[1] >= 550:
                            coords = (coords[0], 10)
                        if coords[1] <= 0:
                            coords = (coords[0], 540)
                        affiche_canvas_carte().bind('<KeyPress>', clavierbis)
                        affiche_canvas_carte().bind('<KeyRelease>', clavierbis)
                        move_rectangle()
                        break
            for obstacle in liste_canvas_obstacles_herbes_capteurs[affiche_reste_carte()][1]:
                if verif_collision_carte(liste_canvas_obstacles_herbes_capteurs[affiche_reste_carte()][4], [obstacle], affiche_canvas_carte())[0][0]:
                    if affiche_canvas_carte().coords(liste_canvas_obstacles_herbes_capteurs[affiche_reste_carte()][4])[0] == affiche_canvas_carte().coords(obstacle)[2]:
                        test = False
                        break
            if test:
                coords = (coords[0] - 10, coords[1])
    elif touche == "z":
        menu_fonction()

    affiche_canvas_carte().coords(liste_canvas_obstacles_herbes_capteurs[affiche_reste_carte()][4], coords[0], coords[1], coords[0] + 50, coords[1] + 50)

    if current_key is not None and fenetre.focus_get() == active_fenetre:
        affiche_canvas_carte().after(16, move_rectangle)


def handle_action_key(touche):
    """Gère les interactions déclenchées par la touche 'a'."""
    if touche == 'a':
        # Interaction avec le magasin
        if len(liste_canvas_obstacles_herbes_capteurs[affiche_reste_carte()][5]) != 0:
            if verif_collision_carte(liste_canvas_obstacles_herbes_capteurs[affiche_reste_carte()][4], liste_canvas_obstacles_herbes_capteurs[affiche_reste_carte()][5], affiche_canvas_carte())[0][0]:
                magasin_fonction()

        # Interaction avec les PNJ
        if len(liste_canvas_obstacles_herbes_capteurs[affiche_reste_carte()][6]) != 0:
            for i in range(len(liste_canvas_obstacles_herbes_capteurs[affiche_reste_carte()][6])):
                if verif_collision_carte(liste_canvas_obstacles_herbes_capteurs[affiche_reste_carte()][4], [liste_canvas_obstacles_herbes_capteurs[affiche_reste_carte()][6][i][0]], affiche_canvas_carte())[0][0]:
                    dialogue_perso(i)
        # Interaction avec le campement
        if len(liste_canvas_obstacles_herbes_capteurs[affiche_reste_carte()][7]) != 0:
            if verif_collision_carte(liste_canvas_obstacles_herbes_capteurs[affiche_reste_carte()][4], liste_canvas_obstacles_herbes_capteurs[affiche_reste_carte()][7], affiche_canvas_carte())[0][0]:
                campement_fonction()


def dialogue_perso(numero):
    # ... (le reste de la fonction dialogue_perso reste inchangé)
    pass


def verif_collision_carte(objet1, liste_objets2, canva):
    """Vérifie la collision entre objet1 et une liste d'autres objets."""
    liste = []
    coords1 = canva.coords(objet1)
    for objet2 in liste_objets2:
        coords2 = canva.coords(objet2)
        # Condition de non-collision
        if coords1[2] < coords2[0] or coords1[0] > coords2[2] or coords1[3] < coords2[1] or coords1[1] > coords2[3]:
            liste.append([False, objet2])
        else:
            liste.append([True, objet2])
    return liste


def mouvement_pnjs():
    if fenetre.focus_get() == affiche_canvas_carte():
        print('salut')


def capteur_collision(capteur):
    coord1 = affiche_canvas_carte().coords(capteur)
    coord2 = affiche_canvas_carte().coords(liste_canvas_obstacles_herbes_capteurs[affiche_reste_carte()][4])
    distance_x = abs(coord1[0] - coord1[2])
    distance_y = abs(coord1[1] - coord1[3])
    if distance_x <= distance_y:
        if coord2[2] == coord1[2]:
            return True
        else:
            return False
    if distance_y <= distance_x:
        if coord2[3] == coord1[3]:
            return True
        else:
            return False


def vartextupdate_carte(texte):
    limite_texte = texte[0:1]
    for i in range(2, len(texte)):
        time.sleep(0.01)
        vartext.set(limite_texte)
        label_narration_carte.update()
        limite_texte = texte[0:i]
    vartext.set(texte)
    label_narration_carte.update()


def varlabel_texte_soin_combat(texte):
    limite_texte = texte[0:1]
    for i in range(2, len(texte)):
        time.sleep(0.01)
        vartexte_soin_combat.set(limite_texte)
        label_texte_soin_combat.update()
        limite_texte = texte[0:i]
    vartexte_soin_combat.set(texte)
    label_texte_soin_combat.update()


def varlabel_texte_mana_combat(texte):
    limite_texte = texte[0:1]
    for i in range(2, len(texte)):
        time.sleep(0.01)
        vartexte_mana_combat.set(limite_texte)
        label_texte_mana_combat.update()
        limite_texte = texte[0:i]
    vartexte_mana_combat.set(texte)
    label_texte_mana_combat.update()


def vartextupdate_combat(texte):
    limite_texte = texte[0:1]
    for i in range(2, len(texte)):
        time.sleep(0.01)
        vartext_combat.set(limite_texte)
        texte_frame_menu_combat.update()
        limite_texte = texte[0:i]
    vartext_combat.set(texte)
    texte_frame_menu_combat.update()


def hautes_hrbes(liste):
    test = False
    rectangle = liste_canvas_obstacles_herbes_capteurs[affiche_reste_carte()][4]
    for i in range(len(liste_canvas_obstacles_herbes_capteurs[affiche_reste_carte()][2])):
        if verif_collision_carte(rectangle, liste, affiche_canvas_carte())[i][0]:
            coords1 = affiche_canvas_carte().coords(rectangle)
            coords2 = affiche_canvas_carte().coords(liste[i])
            distancex = (coords1[2] - coords1[0]) + (coords2[2] - coords2[0])
            distancey = (coords1[3] - coords1[1]) + (coords2[3] - coords2[1])
            if abs(coords1[2] - coords2[0]) == distancex or abs(coords2[2] - coords1[0]) == distancex:
                test = False
            elif abs(coords1[3] - coords2[1]) == distancey or abs(coords2[3] - coords1[1]) == distancey:
                test = False
            else:
                test = True
    if test:
        nbr_alea = random.randint(0, 20)
        if nbr_alea == 5:
            combat_sauvage()


def combat_sauvage():
    affiche_canvas_carte().pack_forget()
    label_narration_carte.pack_forget()
    if menu.winfo_ismapped() == 1:
        menu.unbind('<Key>')
        menu.place_forget()
    else:
        affiche_canvas_carte().after_cancel(move_rectangle)
        affiche_canvas_carte().unbind('<KeyPress>')
        affiche_canvas_carte().unbind('<KeyRelease>')
    canva_combat.pack()
    frame_menu_combat.pack()
    init_combat()


def campement_fonction():
    print("tru")


# Fonctions du magasin


def magasin_fonction():
    magasin_menu.place(relx=0.5, rely=0.45, anchor=CENTER)
    affiche_canvas_carte().tk.call('raise', magasin_menu)
    affiche_canvas_carte().unbind('<KeyPress>')
    affiche_canvas_carte().unbind('<KeyRelease>')
    magasin_menu.focus_set()
    magasin_menu.bind('<Key>', curseur_magasin)


def curseur_magasin(event):
    touche = event.keysym
    if touche == 'Down':
        if magasin_menu.coords(bouton_choix_magasin) == [8, 8, 347, 102]:
            magasin_menu.coords(bouton_choix_magasin, 8, 101, 347, 194)
        elif magasin_menu.coords(bouton_choix_magasin) == [8, 101, 347, 194]:
            magasin_menu.coords(bouton_choix_magasin, 8, 192, 347, 287)
    if touche == 'Up':
        if magasin_menu.coords(bouton_choix_magasin) == [8, 192, 347, 287]:
            magasin_menu.coords(bouton_choix_magasin, 8, 101, 347, 194)
        elif magasin_menu.coords(bouton_choix_magasin) == [8, 101, 347, 194]:
            magasin_menu.coords(bouton_choix_magasin, 8, 8, 347, 102)
    if touche == 'z':
        magasin_menu.coords(bouton_choix_magasin, 8, 8, 347, 102)
        magasin_menu.unbind('<Key>')
        magasin_menu.place_forget()
        affiche_canvas_carte().focus_set()
        affiche_canvas_carte().bind('<KeyPress>', clavierbis)
        affiche_canvas_carte().bind('<KeyRelease>', clavierbis)
        changement_route()
    if touche == 'a' and magasin_menu.coords(bouton_choix_magasin) == [8, 8, 347, 102]:
        magasin_fenetre()
    if touche == 'a' and magasin_menu.coords(bouton_choix_magasin) == [8, 192, 347, 287]:
        magasin_menu.coords(bouton_choix_magasin, 8, 8, 347, 102)
        magasin_menu.unbind('<Key>')
        magasin_menu.place_forget()
        affiche_canvas_carte().focus_set()
        affiche_canvas_carte().bind('<KeyPress>', clavierbis)
        affiche_canvas_carte().bind('<KeyRelease>', clavierbis)
        changement_route()
    #if touche == 'a' and magasin_menu.coords(bouton_choix_menu) == [8, 101, 347, 194]:
     #   menu_equipement()
    if touche == 'a' and magasin_menu.coords(bouton_choix_magasin) == [8, 101, 347, 194]:
        vente_magasin_fenetre()


def magasin_fenetre():
    magasin_menu.place_forget()
    frame_menu_combat.pack_forget()
    canva_combat.pack_forget()
    magasin_menu.unbind('<Key>')
    affiche_canvas_carte().pack_forget()
    label_narration_carte.pack_forget()
    label_narration_carte.pack()
    frame_magasin.pack()
    liste_mana_magasin.grid_forget()
    liste_objet_magasin.grid_forget()
    liste_soins_magasin.grid()
    frame_texte_magasin.grid_forget()
    frame_texte_magasin.grid()
    liste_soins_magasin.focus_set()
    keyboard_player_magasin(liste_soins_magasin)
    vartextupdate_carte('Quel objet voulez vous acheter ?')


def keyboard_player_magasin(fonction):
    liste_soins_magasin.unbind('<Key>')
    liste_mana_magasin.unbind('<Key>')
    liste_objet_magasin.unbind('<Key>')
    fonction.focus_set()
    fonction.selection_clear(0, 'end')
    fonction.select_set(0)
    fonction.activate(0)
    fonction.bind('<Key>', fonction_keyboard_player_magasin)


def fonction_keyboard_player_magasin(event):
    touche = event.keysym
    if touche == "Right":
        if liste_soins_magasin.winfo_ismapped() == 1:
            liste_soins_magasin.grid_forget()
            frame_texte_magasin.grid_forget()
            liste_mana_magasin.grid()
            frame_texte_magasin.grid()
            keyboard_player_magasin(liste_mana_magasin)
        if liste_mana_magasin.winfo_ismapped() == 1:
            liste_mana_magasin.grid_forget()
            frame_texte_magasin.grid_forget()
            liste_objet_magasin.grid()
            frame_texte_magasin.grid()
            keyboard_player_magasin(liste_objet_magasin)
    if touche == 'Left':
        if liste_objet_magasin.winfo_ismapped() == 1:
            liste_objet_magasin.grid_forget()
            frame_texte_magasin.grid_forget()
            liste_mana_magasin.grid()
            frame_texte_magasin.grid()
            keyboard_player_magasin(liste_mana_magasin)
        if liste_mana_magasin.winfo_ismapped() == 1:
            liste_mana_magasin.grid_forget()
            frame_texte_magasin.grid_forget()
            liste_soins_magasin.grid()
            frame_texte_magasin.grid()
            keyboard_player_magasin(liste_soins_magasin)
    if touche == 'z':
        back_magasin_to_menu()
    if touche == 'a':
        if liste_soins_magasin.winfo_ismapped() == 1:
            soins_magasin_objet()
        if liste_mana_magasin.winfo_ismapped() == 1:
            mana_magasin_objet()
        if liste_objet_magasin.winfo_ismapped() == 1:
            utilitaire_magasin_objet()


def utilitaire_magasin_objet():
    if liste_objet_magasin.curselection() != 0:
        nombre = liste_objet_magasin.curselection()[0]
        item = liste_objet_magasin.get(nombre)
        mot = item_finding(item)
        for i in range(len(liste_utilitaire_objet)):
            if liste_utilitaire_objet[i].nom == mot:
                if liste_utilitaire_objet[i].prix <= Perso1.argent:
                    liste_utilitaire_objet[i].quantite += 1
                    Perso1.argent -= liste_utilitaire_objet[i].prix
                    test = False
                    for j in range(len(sac_liste[2])):
                        if mot == sac_liste[2][j][0]:
                            sac_liste[2][j][1] += 1
                            test = True
                    if not test:
                        sac_liste[2].append([liste_utilitaire_objet[i].nom, liste_utilitaire_objet[i].quantite])
                        liste_menu_utilitaires_carte.insert(liste_menu_utilitaires_carte.size(), str(liste_utilitaire_objet[i].nom) + '    x ' + str(liste_utilitaire_objet[i].quantite))
                    else:
                        valeurs = liste_menu_utilitaires_carte.get(0, 'end')
                        for l in range(len(valeurs)):
                            objet = item_finding(valeurs[l])
                            if objet == mot:
                                liste_menu_utilitaires_carte.delete(l)
                                liste_menu_utilitaires_carte.insert(l, str(liste_utilitaire_objet[i].nom) + '    x ' + str(liste_utilitaire_objet[i].quantite))
                    dev_update()
                    vartextupdate_carte("Vous avez acheté l'objet " + str(liste_utilitaire_objet[i].nom))


def soins_magasin_objet():
    if liste_soins_magasin.curselection() != ():
        nombre = liste_soins_magasin.curselection()[0]
        item = liste_soins_magasin.get(nombre)
        mot = item_finding(item)
        for i in range(len(liste_soins_objets)):
            if liste_soins_objets[i].nom == mot:
                if liste_soins_objets[i].prix <= Perso1.argent:
                    liste_soins_objets[i].quantite += 1
                    Perso1.argent -= liste_soins_objets[i].prix
                    test = False
                    for j in range(len(sac_liste[0])):
                        if mot == sac_liste[0][j][0]:
                            sac_liste[0][j][1] += 1
                            test = True
                    if not test:
                        sac_liste[0].append([liste_soins_objets[i].nom, liste_soins_objets[i].quantite])
                        liste_menu_soins_carte.insert(liste_menu_soins_carte.size()+1, str(liste_soins_objets[i].nom) + '    x ' + str(liste_soins_objets[i].quantite))
                        liste_soins_combat.insert(liste_menu_soins_carte.size() + 1, str(liste_soins_objets[i].nom) + '    x ' + str(liste_soins_objets[i].quantite))
                    else:
                        valeurs = liste_menu_soins_carte.get(0, 'end')
                        for l in range(len(valeurs)):
                            objet = item_finding(valeurs[l])
                            if objet == mot:
                                liste_menu_soins_carte.delete(l)
                                liste_soins_combat.delete(l)
                                liste_menu_soins_carte.insert(l, str(liste_soins_objets[i].nom) + '    x ' + str(liste_soins_objets[i].quantite))
                                liste_soins_combat.insert(l, str(liste_soins_objets[i].nom) + '    x ' + str(liste_soins_objets[i].quantite))
                    dev_update()
                    vartextupdate_carte("Vous avez acheté l'objet " + str(liste_soins_objets[i].nom))


def mana_magasin_objet():
    if liste_mana_magasin.curselection() != ():
        nombre = liste_mana_magasin.curselection()[0]
        item = liste_mana_magasin.get(nombre)
        mot = item_finding(item)
        for i in range(len(liste_mana_objet)):
            if liste_mana_objet[i].nom == mot:
                if liste_mana_objet[i].prix <= Perso1.argent:
                    liste_mana_objet[i].quantite += 1
                    Perso1.argent -= liste_mana_objet[i].prix
                    test = False
                    for j in range(len(sac_liste[1])):
                        if mot == sac_liste[1][j][0]:
                            sac_liste[1][j][1] += 1
                            test = True
                    if not test:
                        sac_liste[1].append([liste_mana_objet[i].nom, liste_mana_objet[i].quantite])
                        liste_mana_combat.insert(liste_menu_mana_carte.size()+1, str(liste_mana_objet[i].nom) + '    x ' + str(liste_mana_objet[i].quantite))
                        liste_menu_mana_carte.insert(liste_menu_mana_carte.size()+1, str(liste_mana_objet[i].nom) + '    x ' + str(liste_mana_objet[i].quantite))
                    else:
                        valeurs = liste_menu_mana_carte.get(0, 'end')
                        for l in range(len(valeurs)):
                            objet = item_finding(valeurs[l])
                            if objet == mot:
                                liste_menu_mana_carte.delete(l)
                                liste_mana_combat.delete(l)
                                liste_mana_combat.insert(l, str(liste_mana_objet[i].nom) + '    x ' + str(liste_mana_objet[i].quantite))
                                liste_menu_mana_carte.insert(l, str(liste_mana_objet[i].nom) + '    x ' + str(liste_mana_objet[i].quantite))
                    dev_update()
                    vartextupdate_carte("Vous avez acheté l'objet " + str(liste_mana_objet[i].nom))


def clavier_listes_magasin(event):
    touche = event.keysym
    if touche == 'Right' and liste_soins_magasin.winfo_ismapped() == 1:
        liste_soins_magasin.grid_forget()
        frame_texte_magasin.grid_forget()
        liste_soins_magasin.unbind('<Key>')
        liste_mana_magasin.grid()
        frame_texte_magasin.grid()
        liste_mana_magasin.focus_set()
        liste_mana_magasin.bind('<Key>', clavier_listes_magasin)
    if touche == 'Right' and liste_mana_magasin.winfo_ismapped() == 1:
        liste_mana_magasin.grid_forget()
        frame_texte_magasin.grid_forget()
        liste_mana_magasin.unbind('<Key>')
        liste_objet_magasin.grid()
        frame_texte_magasin.grid()
        liste_objet_magasin.focus_set()
        liste_objet_magasin.bind('<Key>', clavier_listes_magasin)
    if touche == 'Left' and liste_mana_magasin.winfo_ismapped() == 1:
        liste_mana_magasin.grid_forget()
        frame_texte_magasin.grid_forget()
        liste_mana_magasin.unbind('<Key>')
        liste_soins_magasin.grid()
        frame_texte_magasin.grid()
        liste_soins_magasin.focus_set()
        liste_soins_magasin.bind('<Key>', clavier_listes_magasin)
    if touche == 'Left' and liste_objet_magasin.winfo_ismapped() == 1:
        liste_objet_magasin.grid_forget()
        frame_texte_magasin.grid_forget()
        liste_objet_magasin.unbind('<Key>')
        liste_mana_magasin.grid()
        frame_texte_magasin.grid()
        liste_mana_magasin.focus_set()
        liste_mana_magasin.bind('<Key>', clavier_listes_magasin)
    if touche == 'z':
        back_magasin_to_menu()


def back_magasin_to_menu():
    liste_mana_magasin.unbind('<Key>')
    liste_objet_magasin.unbind('<Key>')
    liste_soins_magasin.unbind('<Key>')
    frame_magasin.pack_forget()
    label_narration_carte.pack()
    affiche_canvas_carte().pack()
    magasin_menu.place(relx=0.5, rely=0.45, anchor=CENTER)
    magasin_menu.focus_set()
    magasin_menu.bind('<Key>', curseur_magasin)


def bouton_magasin_objet():
    if liste_soins_magasin.winfo_ismapped() == 1:
        frame_texte_magasin.grid_forget()
        liste_soins_magasin.grid_forget()
        liste_soins_magasin.unbind('<Key>')
        liste_objet_magasin.grid()
        liste_objet_magasin.select_set(0)
        frame_texte_magasin.grid()
        liste_objet_magasin.focus_set()
        liste_objet_magasin.bind('<Key>', clavier_listes_magasin)
    if liste_mana_magasin.winfo_ismapped() == 1:
        frame_texte_magasin.grid_forget()
        liste_mana_magasin.grid_forget()
        liste_mana_magasin.unbind('<Key>')
        liste_objet_magasin.grid()
        liste_objet_magasin.select_set(0)
        frame_texte_magasin.grid()
        liste_objet_magasin.focus_set()
        liste_objet_magasin.bind('<Key>', clavier_listes_magasin)


def bouton_magasin_soins():
    if liste_objet_magasin.winfo_ismapped() == 1:
        liste_objet_magasin.grid_forget()
        frame_texte_magasin.grid_forget()
        liste_objet_magasin.unbind('<Key>')
        liste_soins_magasin.grid()
        liste_soins_magasin.select_set(0)
        frame_texte_magasin.grid()
        liste_soins_magasin.focus_set()
        liste_soins_magasin.bind('<Key>', clavier_listes_magasin)
    if liste_mana_magasin.winfo_ismapped() == 1:
        liste_mana_magasin.grid_forget()
        frame_texte_magasin.grid_forget()
        liste_mana_magasin.unbind('<Key>')
        liste_soins_magasin.grid()
        liste_soins_magasin.select_set(0)
        frame_texte_magasin.grid()
        liste_soins_magasin.focus_set()
        liste_soins_magasin.bind('<Key>', clavier_listes_magasin)


def bouton_magasin_mana():
    if liste_soins_magasin.winfo_ismapped() == 1:
        liste_soins_magasin.grid_forget()
        frame_texte_magasin.grid_forget()
        liste_soins_magasin.unbind('<Key>')
        liste_mana_magasin.grid()
        liste_mana_magasin.select_set(0)
        frame_texte_magasin.grid()
        liste_mana_magasin.focus_set()
        liste_mana_magasin.bind('<Key>', clavier_listes_magasin)
    if liste_objet_magasin.winfo_ismapped() == 1:
        liste_objet_magasin.grid_forget()
        frame_texte_magasin.grid_forget()
        liste_objet_magasin.unbind('<Key>')
        liste_mana_magasin.grid()
        liste_mana_magasin.select_set(0)
        frame_texte_magasin.grid()
        liste_mana_magasin.focus_set()
        liste_mana_magasin.bind('<Key>', clavier_listes_magasin)


def vente_magasin_fenetre():
    if frame_menu_liste_carte.winfo_ismapped() == 0:
        magasin_menu.place_forget()
        frame_menu_combat.pack_forget()
        canva_combat.pack_forget()
        magasin_menu.unbind('<Key>')
        affiche_canvas_carte().pack_forget()
        label_narration_carte.pack_forget()
        label_narration_carte.pack()
        frame_menu_carte_bouton.pack()
        frame_menu_liste_carte.pack()
        frame_texte_money_vendre.pack()
        frame_menu_back_carte.pack()
        liste_menu_mana_carte.pack_forget()
        liste_menu_utilitaires_carte.pack_forget()
        liste_menu_objetrares_carte.pack_forget()
        liste_menu_soins_carte.pack()
        liste_menu_soins_carte.focus_set()
        liste_menu_soins_carte.select_set(0)
        liste_menu_soins_carte.activate(0)
        vartextupdate_carte('Quel objet voulez-vous vendre ?')
        liste_menu_soins_carte.bind('<Key>', clavier_vente_carte)
    else:
        liste_menu_soins_carte.unbind('<Key>')
        liste_menu_mana_carte.unbind('<Key>')
        liste_menu_objetrares_carte.unbind('<Key>')
        liste_menu_utilitaires_carte.unbind('<Key>')
        liste_menu_objetrares_carte.pack_forget()
        liste_menu_utilitaires_carte.pack_forget()
        liste_menu_mana_carte.pack_forget()
        liste_menu_soins_carte.pack_forget()
        frame_menu_liste_carte.pack_forget()
        frame_texte_money_vendre.pack_forget()
        frame_menu_back_carte.pack_forget()
        label_narration_carte.pack_forget()
        frame_menu_carte_bouton.pack_forget()
        label_narration_carte.pack()
        affiche_canvas_carte().pack()
        magasin_menu.place(relx=0.5, rely=0.45, anchor=CENTER)
        magasin_menu.bind('<Key>', curseur_magasin)
        magasin_menu.focus_set()


def clavier_vente_carte(event):
    touche = event.keysym
    if touche == 'Right' and fenetre.focus_get() == liste_menu_soins_carte:
        keyboard_bis_vente(liste_menu_soins_carte, liste_menu_mana_carte)
    elif touche == 'Right' and fenetre.focus_get() == liste_menu_mana_carte:
        keyboard_bis_vente(liste_menu_mana_carte, liste_menu_utilitaires_carte)
    elif touche == 'Right' and fenetre.focus_get() == liste_menu_utilitaires_carte:
        keyboard_bis_vente(liste_menu_utilitaires_carte, liste_menu_objetrares_carte)
    elif touche == 'Left' and fenetre.focus_get() == liste_menu_objetrares_carte:
        keyboard_bis_vente(liste_menu_objetrares_carte, liste_menu_utilitaires_carte)
    elif touche == 'Left' and fenetre.focus_get() == liste_menu_utilitaires_carte:
        keyboard_bis_vente(liste_menu_utilitaires_carte, liste_menu_mana_carte)
    elif touche == 'Left' and fenetre.focus_get() == liste_menu_mana_carte:
        keyboard_bis_vente(liste_menu_mana_carte, liste_menu_soins_carte)
    elif touche == 'z':
        vente_magasin_fenetre()
    elif touche == 'a':
        if liste_menu_soins_carte.winfo_ismapped() == 1:
            vente_soin_objet()
        elif liste_menu_mana_carte.winfo_ismapped() == 1:
            vente_mana_objet()
        elif liste_menu_utilitaires_carte.winfo_ismapped() == 1:
            vente_utilitaire_objet()
        else:
            vartextupdate_carte('Impossible de vendre des objets rares ...')


def keyboard_bis_vente(fonction1, fonction2):
    fonction1.unbind('<Key>')
    fonction1.pack_forget()
    fonction2.pack()
    fonction2.focus_set()
    fonction2.selection_clear(0, 'end')
    fonction2.activate(0)
    fonction2.select_set(0)
    fonction2.bind('<Key>', clavier_vente_carte)


def vente_soin_objet():
    nombre = liste_menu_soins_carte.curselection()[0]
    item = liste_menu_soins_carte.get(nombre)
    mot = item_finding(item)
    for i in range(len(liste_soins_objets)):
        if liste_soins_objets[i].nom == mot:
            liste_soins_objets[i].quantite -= 1
            for j in range(len(sac_liste[0])):
                if mot == sac_liste[0][j][0]:
                    sac_liste[0][j][1] -= 1
            liste_annexe = []
            for k in range(len(sac_liste[0])):
                if sac_liste[0][k][1] != 0:
                    liste_annexe.append(sac_liste[0][k])
            sac_liste[0] = liste_annexe
            liste_menu_soins_carte.delete(nombre)
            liste_soins_combat.delete(nombre)
            Perso1.argent += liste_soins_objets[i].prix
            if liste_soins_objets[i].quantite > 0:
                liste_menu_soins_carte.insert(nombre, str(liste_soins_objets[i].nom) + '    x ' + str(
                    liste_soins_objets[i].quantite))
                liste_soins_combat.insert(nombre, str(liste_soins_objets[i].nom) + '    x ' + str(
                    liste_soins_objets[i].quantite))
                liste_menu_soins_carte.select_set(nombre)
                liste_menu_soins_carte.activate(nombre)
            dev_update()
            vartextupdate_carte("Vous avez gagné " + str(liste_soins_objets[i].prix) + ' PO !')
            dev_update()


def vente_mana_objet():
    nombre = liste_menu_mana_carte.curselection()[0]
    item = liste_menu_mana_carte.get(liste_menu_mana_carte.curselection()[0])
    mot = item_finding(item)
    for i in range(len(liste_mana_objet)):
        if liste_mana_objet[i].nom == mot:
            liste_mana_objet[i].quantite -= 1
            for j in range(len(sac_liste[1])):
                if mot == sac_liste[1][j][0]:
                    sac_liste[1][j][1] -= 1
            liste_annexe = []
            for k in range(len(sac_liste[1])):
                if sac_liste[1][k][1] != 0:
                    liste_annexe.append(sac_liste[1][k])
            sac_liste[1] = liste_annexe
            liste_menu_mana_carte.delete(nombre)
            liste_mana_combat.delete(nombre)
            Perso1.argent += liste_mana_objet[i].prix
            if liste_mana_objet[i].quantite > 0:
                liste_menu_mana_carte.insert(nombre, str(liste_mana_objet[i].nom) + '    x ' + str(
                    liste_mana_objet[i].quantite))
                liste_mana_combat.insert(nombre,
                                         str(liste_mana_objet[i].nom) + '    x ' + str(liste_mana_objet[i].quantite))
                liste_menu_mana_carte.select_set(nombre)
                liste_menu_mana_carte.activate(nombre)
            dev_update()
            vartextupdate_carte("Vous avez gagné " + str(liste_mana_objet[i].prix) + ' Po !')
            dev_update()


def vente_utilitaire_objet():
    nombre = liste_menu_utilitaires_carte.curselection()[0]
    item = liste_menu_utilitaires_carte.get(nombre)
    mot = item_finding(item)
    for i in range(len(liste_utilitaire_objet)):
        if liste_utilitaire_objet[i].nom == mot:
            liste_utilitaire_objet[i].quantite -= 1
            for j in range(len(sac_liste[2])):
                if mot == sac_liste[2][j][0]:
                    sac_liste[2][j][1] -= 1
            liste_annexe = []
            for k in range(len(sac_liste[2])):
                if sac_liste[2][k][1] != 0:
                    liste_annexe.append(sac_liste[2][k])
                sac_liste[2] = liste_annexe
                liste_menu_utilitaires_carte.delete(nombre)
                Perso1.argent += liste_utilitaire_objet[i].prix
                if liste_utilitaire_objet[i].quantite > 0:
                    liste_menu_utilitaires_carte.insert(nombre, str(liste_utilitaire_objet[i].nom) + '    x ' + str(
                        liste_utilitaire_objet[i].quantite))
                    liste_menu_utilitaires_carte.select_set(nombre)
                    liste_menu_utilitaires_carte.activate(nombre)
                dev_update()
                vartextupdate_carte("Vous avez gagné " + str(liste_utilitaire_objet[i].prix) + ' Po !')
                dev_update()


# Fonctions du menu


def menu_fonction():
    menu.place(relx=0.5, rely=0.45, anchor=CENTER)
    affiche_canvas_carte().tk.call('raise', menu)
    affiche_canvas_carte().unbind('<KeyPress>')
    affiche_canvas_carte().unbind('<KeyRelease>')
    menu.focus_set()
    menu.bind('<Key>', curseur_menu)


def curseur_menu(event):
    touche = event.keysym
    if touche == 'Down':
        if menu.coords(bouton_choix_menu) == [8, 8, 347, 102]:
            menu.coords(bouton_choix_menu, 8, 101, 347, 194)
        elif menu.coords(bouton_choix_menu) == [8, 101, 347, 194]:
            menu.coords(bouton_choix_menu, 8, 192, 347, 287)
        elif menu.coords(bouton_choix_menu) == [8, 192, 347, 287]:
            menu.coords(bouton_choix_menu, 8, 8, 347, 102)
    if touche == 'Up':
        if menu.coords(bouton_choix_menu) == [8, 192, 347, 287]:
            menu.coords(bouton_choix_menu, 8, 101, 347, 194)
        elif menu.coords(bouton_choix_menu) == [8, 101, 347, 194]:
            menu.coords(bouton_choix_menu, 8, 8, 347, 102)
        elif menu.coords(bouton_choix_menu) == [8, 8, 347, 102]:
            menu.coords(bouton_choix_menu, 8, 192, 347, 287)
    if touche == 'z':
        menu.coords(bouton_choix_menu, 8, 8, 347, 102)
        menu.unbind('<Key>')
        menu.place_forget()
        affiche_canvas_carte().focus_set()
        affiche_canvas_carte().bind('<KeyPress>', clavierbis)
        affiche_canvas_carte().bind('<KeyRelease>', clavierbis)
        changement_route()
    if touche == 'a' and menu.coords(bouton_choix_menu) == [8, 8, 347, 102]:
        menu_sac()
    if touche == 'a' and menu.coords(bouton_choix_menu) == [8, 192, 347, 287]:
        sauvegarde_menu()
    if touche == 'a' and menu.coords(bouton_choix_menu) == [8, 101, 347, 194]:
        menu_equipement()


def menu_sac():
    menu.unbind('<Key>')
    menu.place_forget()
    label_narration_carte.pack_forget()
    affiche_canvas_carte().pack_forget()
    canva_combat.pack_forget()
    frame_menu_combat.pack_forget()
    frame_menu_carte_bouton.pack()
    frame_menu_liste_carte.pack()
    frame_menu_liste_carte.focus_set()
    liste_menu_utilitaires_carte.pack_forget()
    liste_menu_mana_carte.pack_forget()
    liste_menu_objetrares_carte.pack_forget()
    liste_menu_soins_carte.pack()
    label_narration_carte.pack()
    frame_menu_back_carte.pack()
    keyboard_player(liste_menu_soins_carte)
    vartextupdate_carte('Quel objet voulez-vous utiliser ?')


def menu_sac_clavier(event):
    touche = event.keysym
    if touche == "Right" and liste_menu_soins_carte.winfo_ismapped() == 1:
        liste_menu_soins_carte.pack_forget()
        liste_menu_mana_carte.pack()
    if touche == "Right" and liste_menu_mana_carte.winfo_ismapped() == 1:
        liste_menu_mana_carte.pack_forget()
        liste_menu_utilitaires_carte.pack()
    if touche == "Right" and liste_menu_utilitaires_carte.winfo_ismapped() == 1:
        liste_menu_utilitaires_carte.pack_forget()
        liste_menu_objetrares_carte.pack()
    if touche == "Left" and liste_menu_mana_carte.winfo_ismapped() == 1:
        liste_menu_mana_carte.pack_forget()
        liste_menu_soins_carte.pack()
    if touche == "Left" and liste_menu_utilitaires_carte.winfo_ismapped() == 1:
        liste_menu_utilitaires_carte.pack_forget()
        liste_menu_mana_carte.pack()
    if touche == "Left" and liste_menu_objetrares_carte.winfo_ismapped() == 1:
        liste_menu_objetrares_carte.pack_forget()
        liste_menu_utilitaires_carte.pack()
    if touche == "z":
        back_menu_carte()
    if touche == "Down" or touche == "Up":
        if liste_menu_soins_carte.winfo_ismapped() == 1:
            keyboard_player(liste_menu_soins_carte)
        if liste_menu_mana_carte.winfo_ismapped() == 1:
            keyboard_player(liste_menu_mana_carte)
        if liste_menu_utilitaires_carte.winfo_ismapped() == 1:
            keyboard_player(liste_menu_utilitaires_carte)
        if liste_menu_objetrares_carte.winfo_ismapped() == 1:
            keyboard_player(liste_menu_objetrares_carte)


def menu_to_soins():
    liste_menu_mana_carte.pack_forget()
    liste_menu_objetrares_carte.pack_forget()
    liste_menu_utilitaires_carte.pack_forget()
    liste_menu_soins_carte.pack()


def menu_to_mana():
    liste_menu_soins_carte.pack_forget()
    liste_menu_objetrares_carte.pack_forget()
    liste_menu_utilitaires_carte.pack_forget()
    liste_menu_mana_carte.pack()


def keyboard_player(fonction):
    liste_menu_soins_carte.unbind('<Key>')
    liste_menu_utilitaires_carte.unbind('<Key>')
    liste_menu_mana_carte.unbind('<Key>')
    liste_menu_objetrares_carte.unbind('<Key>')
    fonction.focus_set()
    fonction.selection_clear(0, 'end')
    fonction.select_set(0)
    fonction.activate(0)
    fonction.bind('<Key>', fonction_keyboard_player)


def fonction_keyboard_player(event):
    touche = event.keysym
    if touche == "Right":
        if liste_menu_soins_carte.winfo_ismapped() == 1:
            liste_menu_soins_carte.pack_forget()
            liste_menu_mana_carte.pack()
            keyboard_player(liste_menu_mana_carte)
        if liste_menu_mana_carte.winfo_ismapped() == 1:
            liste_menu_mana_carte.pack_forget()
            liste_menu_utilitaires_carte.pack()
            keyboard_player(liste_menu_utilitaires_carte)
        if liste_menu_utilitaires_carte.winfo_ismapped() == 1:
            liste_menu_utilitaires_carte.pack_forget()
            liste_menu_objetrares_carte.pack()
            keyboard_player(liste_menu_objetrares_carte)
    if touche == 'Left':
        if liste_menu_objetrares_carte.winfo_ismapped() == 1:
            liste_menu_objetrares_carte.pack_forget()
            liste_menu_utilitaires_carte.pack()
            keyboard_player(liste_menu_utilitaires_carte)
        if liste_menu_utilitaires_carte.winfo_ismapped() == 1:
            liste_menu_utilitaires_carte.pack_forget()
            liste_menu_mana_carte.pack()
            keyboard_player(liste_menu_mana_carte)
        if liste_menu_mana_carte.winfo_ismapped() == 1:
            liste_menu_mana_carte.pack_forget()
            liste_menu_soins_carte.pack()
            keyboard_player(liste_menu_soins_carte)
    if touche == 'z':
        back_menu_carte()
    elif touche == 'a':
        if liste_menu_soins_carte.winfo_ismapped() == 1:
            liste_menu_soins_carte.unbind('<Key>')
            soins_sac_objet()
            time.sleep(0.1)
            liste_menu_soins_carte.bind('<Key>', fonction_keyboard_player)
        if liste_menu_mana_carte.winfo_ismapped() == 1:
            liste_menu_mana_carte.unbind('<Key>')
            mana_sac_objet()
            time.sleep(0.1)
            liste_menu_mana_carte.bind('<Key>', fonction_keyboard_player)
        if liste_menu_utilitaires_carte.winfo_ismapped() == 1:
            utilitaire_sac_objet()
            time.sleep(0.1)
            liste_menu_utilitaires_carte.bind('<Key>', fonction_keyboard_player)
        if liste_menu_objetrares_carte.winfo_ismapped() == 1:
            if liste_menu_objetrares_carte.curselection() != ():
                selection_index = liste_menu_objetrares_carte.curselection()[0]
                item_name = liste_menu_objetrares_carte.get(selection_index)
                
                if item_name == "Carte":
                    affiche_carte_item()
                else:
                    vartextupdate_carte("Cet objet ne peut pas être utilisé.")



def utilitaire_sac_objet():
    if liste_menu_utilitaires_carte.curselection() != ():
        nombre = liste_menu_utilitaires_carte.curselection()[0]
        item = liste_menu_utilitaires_carte.get(nombre)
        mot = item_finding(item)
        for i in range(len(liste_utilitaire_objet)):
            if liste_utilitaire_objet[i].nom == mot:
                liste_utilitaire_objet[i].quantite -= 1
                for j in range(len(sac_liste[2])):
                    if mot == sac_liste[2][j][0]:
                        sac_liste[2][j][1] -= 1
                liste_annexe = []
                for k in range(len(sac_liste[2])):
                    if sac_liste[2][k][1] != 0:
                        liste_annexe.append(sac_liste[2][k])
                    sac_liste[2] = liste_annexe
                    liste_menu_utilitaires_carte.delete(nombre)
                    if liste_utilitaire_objet[i].quantite > 0:
                        liste_menu_utilitaires_carte.insert(nombre, str(liste_utilitaire_objet[i].nom) + '    x ' + str(liste_utilitaire_objet[i].quantite))
                        liste_menu_utilitaires_carte.select_set(nombre)
                        liste_menu_utilitaires_carte.activate(nombre)
                    effet_objet_utilitaire(liste_utilitaire_objet[i])
                    dev_update()


def soins_sac_objet():
    if liste_menu_soins_carte.curselection() != ():
        nombre = liste_menu_soins_carte.curselection()[0]
        item = liste_menu_soins_carte.get(nombre)
        mot = item_finding(item)
        for i in range(len(liste_soins_objets)):
            if liste_soins_objets[i].nom == mot:
                liste_soins_objets[i].quantite -= 1
                for j in range(len(sac_liste[0])):
                    if mot == sac_liste[0][j][0]:
                        sac_liste[0][j][1] -= 1
                liste_annexe = []
                for k in range(len(sac_liste[0])):
                    if sac_liste[0][k][1] != 0:
                        liste_annexe.append(sac_liste[0][k])
                sac_liste[0] = liste_annexe
                liste_menu_soins_carte.delete(nombre)
                liste_soins_combat.delete(nombre)
                Perso1.soin_objet(liste_soins_objets[i])
                if liste_soins_objets[i].quantite > 0:
                    liste_menu_soins_carte.insert(nombre, str(liste_soins_objets[i].nom) + '    x ' + str(liste_soins_objets[i].quantite))
                    liste_soins_combat.insert(nombre, str(liste_soins_objets[i].nom) + '    x ' + str(liste_soins_objets[i].quantite))
                    liste_menu_soins_carte.select_set(nombre)
                    liste_menu_soins_carte.activate(nombre)
                vartextupdate_carte("Vous avez regagné " + str(liste_soins_objets[i].soin) + ' PV.')
                dev_update()


def effet_objet_utilitaire(objet):
    effet = objet.effet
    if effet[0] == "Repousse":
        global repousse_var
        repousse_var = (1, effet[1])
        vartextupdate_carte("Vous avez utilisé l'objet " + str(objet.nom))


def mana_sac_objet():
    if liste_menu_mana_carte.curselection() != ():
        nombre = liste_menu_mana_carte.curselection()[0]
        item = liste_menu_mana_carte.get(liste_menu_mana_carte.curselection()[0])
        mot = item_finding(item)
        for i in range(len(liste_mana_objet)):
            if liste_mana_objet[i].nom == mot:
                liste_mana_objet[i].quantite -= 1
                for j in range(len(sac_liste[1])):
                    if mot == sac_liste[1][j][0]:
                        sac_liste[1][j][1] -= 1
                liste_annexe = []
                for k in range(len(sac_liste[1])):
                    if sac_liste[1][k][1] != 0:
                        liste_annexe.append(sac_liste[1][k])
                sac_liste[1] = liste_annexe
                liste_menu_mana_carte.delete(nombre)
                liste_mana_combat.delete(nombre)
                Perso1.mana_objet(liste_mana_objet[i])
                if liste_mana_objet[i].quantite > 0:
                    liste_menu_mana_carte.insert(nombre, str(liste_mana_objet[i].nom) + '    x ' + str(liste_mana_objet[i].quantite))
                    liste_mana_combat.insert(nombre, str(liste_mana_objet[i].nom) + '    x ' + str(liste_mana_objet[i].quantite))
                    liste_menu_mana_carte.select_set(nombre)
                    liste_menu_mana_carte.activate(nombre)
                vartextupdate_carte("Vous avez regagné " + str(liste_mana_objet[i].mana) + ' PM.')
                dev_update()


def item_finding(item):
    mot = ''
    for i in range(len(item)):
        if item[i] != ' ':
            mot += item[i]
        if item[i] == ' ':
            if item[i+1] == ' ':
                return mot
            else:
                mot += item[i]


def affiche_carte_item():
    """Affiche une fenêtre avec l'image de la carte du monde."""
    # On cache les widgets du menu du sac
    frame_menu_carte_bouton.pack_forget()
    frame_menu_liste_carte.pack_forget()
    frame_menu_back_carte.pack_forget()
    label_narration_carte.pack_forget()

    # Création d'une nouvelle fenêtre pour la carte
    top_carte = Toplevel(fenetre)
    top_carte.title("Carte du monde")
    top_carte.geometry("800x650")
    top_carte.resizable(False, False)

    # Chargement et affichage de l'image
    try:
        img_carte = PhotoImage(file='carte_du_monde.png')
        label_carte = Label(top_carte, image=img_carte)
        label_carte.image = img_carte  # Garder une référence
        label_carte.pack()
    except Exception as e:
        # Au cas où l'image ne se charge pas
        label_erreur = Label(top_carte, text=f"Erreur: Impossible de charger 'carte_du_monde.png'\n{e}", font=('Calibri', 15))
        label_erreur.pack(pady=50)

    vartextupdate_carte("Appuyez sur 'z' pour fermer la carte.")
    label_narration_carte.pack() # On ré-affiche la narration

    def fermer_carte(event=None):
        if event.keysym == 'z':
            top_carte.destroy()
            # On ré-affiche le menu du sac
            menu_sac()

    top_carte.bind('<KeyPress>', fermer_carte)
    top_carte.focus_set()


def menu_to_utilitaires():
    liste_menu_mana_carte.pack_forget()
    liste_menu_objetrares_carte.pack_forget()
    liste_menu_soins_carte.pack_forget()
    liste_menu_utilitaires_carte.pack()


def menu_to_objetsrares():
    liste_menu_mana_carte.pack_forget()
    liste_menu_soins_carte.pack_forget()
    liste_menu_utilitaires_carte.pack_forget()
    liste_menu_objetrares_carte.pack()


def back_menu_carte():
    frame_menu_liste_carte.pack_forget()
    frame_menu_carte_bouton.pack_forget()
    label_narration_carte.pack_forget()
    frame_menu_back_carte.pack_forget()
    liste_menu_soins_carte.unbind('<Key>')
    liste_menu_mana_carte.unbind('<Key>')
    liste_menu_utilitaires_carte.unbind('<Key>')
    liste_menu_objetrares_carte.unbind('<Key>')
    label_narration_carte.pack()
    vartextupdate_carte('')
    affiche_canvas_carte().pack()
    menu.place(relx=0.5, rely=0.45, anchor=CENTER)
    menu.focus_set()
    menu.bind('<Key>', curseur_menu)


def sauvegarde_menu():
    enregistrement_sac()
    bis_enregistrement_equipement()
    enregistrement_perso()
    vartextupdate_carte("Le jeu a été sauvegardé !")


def menu_equipement():
    menu.unbind('<Key>')
    menu.place_forget()
    label_narration_carte.pack_forget()
    affiche_canvas_carte().pack_forget()
    canva_combat.pack_forget()
    frame_menu_combat.pack_forget()
    frame_menu_equipement_carte.place(x=190, y=50)
    label_narration_carte.place(x=240, y=490)
    frame_menu_changer_equipement.focus_set()
    bouton_menu_casque_carte.config(bg='dark grey')
    frame_menu_changer_equipement.bind('<Key>', menu_equipement_clavier)
    vartextupdate_carte('Quel équipement voulez-vous changer ?')


def menu_equipement_clavier(event):
    touche = event.keysym
    if touche == 'z' and bouton_menu_botte_carte.winfo_ismapped() == 1:
        frame_menu_changer_equipement.unbind('<Key>')
        bouton_menu_botte_carte.config(bg='lightgrey')
        bouton_menu_armure_carte.config(bg='light grey')
        bouton_equipement_back_to_menu_carte.config(bg='light grey')
        bouton_menu_arme_carte.config(bg='light grey')
        label_narration_carte.place_forget()
        frame_menu_equipement_carte.place_forget()
        label_narration_carte.pack()
        affiche_canvas_carte().pack()
        menu.place(relx=0.5, rely=0.45, anchor=CENTER)
        menu.bind('<Key>', curseur_menu)
        menu.focus_set()
        changement_route()
    if touche == 'Right' and bouton_menu_casque_carte.cget('background') == 'light grey' and bouton_menu_armure_carte.cget('background') == 'light grey' and bouton_menu_botte_carte.cget('background') == 'light grey' and bouton_menu_arme_carte.cget('background') == 'light grey':
        bouton_menu_casque_carte.config(bg='dark grey')
    elif touche == 'Down' and bouton_menu_casque_carte.cget('background') == 'dark grey':
        bouton_menu_casque_carte.config(bg='light grey')
        bouton_menu_armure_carte.config(bg='dark grey')
    elif touche == 'Down' and bouton_menu_armure_carte.cget('background') == 'dark grey':
        bouton_menu_armure_carte.config(bg='light grey')
        bouton_menu_botte_carte.config(bg='dark grey')
    elif touche == 'Down' and bouton_menu_botte_carte.cget('background') == 'dark grey':
        bouton_menu_botte_carte.config(bg='light grey')
        bouton_menu_arme_carte.config(bg='dark grey')
    elif touche == 'Down' and bouton_menu_arme_carte.cget('background') == 'dark grey':
        bouton_menu_arme_carte.config(bg='light grey')
        bouton_equipement_back_to_menu_carte.config(bg='dark grey')
    elif touche == 'Up' and bouton_menu_arme_carte.cget('background') == 'dark grey':
        bouton_menu_arme_carte.config(bg='light grey')
        bouton_menu_botte_carte.config(bg='dark grey')
    elif touche == 'Up' and bouton_menu_botte_carte.cget('background') == 'dark grey':
        bouton_menu_botte_carte.config(bg='light grey')
        bouton_menu_armure_carte.config(bg='dark grey')
    elif touche == 'Up' and bouton_menu_armure_carte.cget('background') == 'dark grey':
        bouton_menu_armure_carte.config(bg='light grey')
        bouton_menu_casque_carte.config(bg='dark grey')
    elif touche == 'Up' and bouton_equipement_back_to_menu_carte.cget('background') == 'dark grey':
        bouton_equipement_back_to_menu_carte.config(bg='light grey')
        bouton_menu_arme_carte.config(bg='dark grey')
    if touche == 'a' and bouton_menu_casque_carte.cget('background') == 'dark grey':
        menu_equipement_to_casques()
    elif touche == 'a' and bouton_menu_armure_carte.cget('background') == 'dark grey':
        menu_equipement_to_armures()
    elif touche == 'a' and bouton_menu_botte_carte.cget('background') == 'dark grey':
        menu_equipement_to_bottes()
    elif touche == 'a' and bouton_equipement_back_to_menu_carte.cget('background') == 'dark grey':
        bouton_equipement_back_to_menu_carte.config(bg='light grey')
        menu_back_to_equipement()
    elif touche == 'a' and bouton_menu_arme_carte.cget('background') == 'dark grey':
        menu_equipement_to_armes()


def menu_equipement_to_casques():
    bouton_menu_casque_carte.grid_forget()
    bouton_menu_armure_carte.grid_forget()
    bouton_menu_arme_carte.grid_forget()
    bouton_menu_botte_carte.grid_forget()
    bouton_equipement_back_to_menu_carte.grid_forget()
    liste_menu_casque.grid()
    bouton_choix_back_to_equipement_carte.grid()
    liste_menu_casque.bind('<Key>', clavier_equipement_casque)
    liste_menu_casque.focus_set()
    liste_menu_casque.selection_clear(0, 'end')
    liste_menu_casque.select_set(0)
    liste_menu_casque.activate(0)
    vartextupdate_carte('Quel casque souhaitez-vous équiper ?')


def menu_equipement_to_armures():
    bouton_menu_casque_carte.grid_forget()
    bouton_menu_armure_carte.grid_forget()
    bouton_menu_arme_carte.grid_forget()
    bouton_menu_botte_carte.grid_forget()
    bouton_equipement_back_to_menu_carte.grid_forget()
    liste_menu_armure.grid()
    bouton_choix_back_to_equipement_carte.grid()
    liste_menu_armure.bind('<Key>', clavier_equipement_armure)
    liste_menu_armure.focus_set()
    liste_menu_armure.selection_clear(0, 'end')
    liste_menu_armure.select_set(0)
    liste_menu_armure.activate(0)
    vartextupdate_carte('Quelle armure souhaitez-vous équiper ?')


def menu_equipement_to_bottes():
    bouton_menu_casque_carte.grid_forget()
    bouton_menu_armure_carte.grid_forget()
    bouton_menu_arme_carte.grid_forget()
    bouton_menu_botte_carte.grid_forget()
    bouton_equipement_back_to_menu_carte.grid_forget()
    liste_menu_botte.grid()
    bouton_choix_back_to_equipement_carte.grid()
    liste_menu_botte.bind('<Key>', clavier_equipement_botte)
    liste_menu_botte.focus_set()
    liste_menu_botte.selection_clear(0, 'end')
    liste_menu_botte.select_set(0)
    liste_menu_botte.activate(0)
    vartextupdate_carte('Quelles jambières souhaitez-vous équiper ?')


def menu_equipement_to_armes():
    bouton_menu_casque_carte.grid_forget()
    bouton_menu_armure_carte.grid_forget()
    bouton_menu_arme_carte.grid_forget()
    bouton_menu_botte_carte.grid_forget()
    bouton_equipement_back_to_menu_carte.grid_forget()
    bouton_menu_arme_phys.grid(row=0, column=0, pady=15)
    bouton_menu_arme_mag.grid(row=1, column=0, pady=15)
    bouton_menu_batons_mag.grid(row=2, column=0, pady=15)
    bouton_menu_arme_to_equipement.grid(row=3, column=0, pady=15)
    frame_menu_changer_equipement.focus_set()
    frame_menu_changer_equipement.bind('<Key>', menu_equipement_clavier_arme)
    bouton_menu_arme_phys.config(bg='dark grey')


def menu_arme_to_equipement():
    frame_menu_changer_equipement.bind('<Key>', menu_equipement_clavier)
    bouton_menu_arme_to_equipement.config(bg='light grey')
    bouton_menu_arme_to_equipement.grid_forget()
    bouton_menu_arme_phys.grid_forget()
    bouton_menu_batons_mag.grid_forget()
    bouton_menu_arme_mag.grid_forget()
    bouton_menu_casque_carte.grid(row=0, column=0, pady=15)
    bouton_menu_armure_carte.grid(row=1, column=0, pady=15)
    bouton_menu_botte_carte.grid(row=2, column=0, pady=15)
    bouton_menu_arme_carte.grid(row=3, column=0, pady=15)
    bouton_equipement_back_to_menu_carte.grid(row=4, column=0, pady=15)
    vartextupdate_carte('Quel équipement souhaitez-vous échanger ?')


def menu_equipement_clavier_arme(event):
    touche = event.keysym
    if touche == 'z' and bouton_menu_arme_phys.winfo_ismapped() == 1:
        frame_menu_changer_equipement.unbind('<Key>')
        frame_menu_changer_equipement.bind('<Key>', menu_equipement_clavier)
        frame_menu_changer_equipement.focus_set()
        bouton_menu_arme_mag.config(bg='light grey')
        bouton_menu_batons_mag.config(bg='light grey')
        bouton_menu_arme_to_equipement.config(bg='light grey')
        bouton_menu_arme_phys.grid_forget()
        bouton_menu_arme_mag.grid_forget()
        bouton_menu_batons_mag.grid_forget()
        bouton_menu_arme_to_equipement.grid_forget()
        bouton_menu_casque_carte.grid(row=0, column=0, pady=15)
        bouton_menu_armure_carte.grid(row=1, column=0, pady=15)
        bouton_menu_botte_carte.grid(row=2, column=0, pady=15)
        bouton_menu_arme_carte.grid(row=3, column=0, pady=15)
        bouton_equipement_back_to_menu_carte.grid(row=4, column=0, pady=15)
        vartextupdate_carte('Quel équipement voulez-vous changer ?')
    elif touche == 'Down' and bouton_menu_arme_phys.cget('background') == 'dark grey':
        bouton_menu_arme_phys.config(bg='light grey')
        bouton_menu_arme_mag.config(bg='dark grey')
    elif touche == 'Down' and bouton_menu_arme_mag.cget('background') == 'dark grey':
        bouton_menu_arme_mag.config(bg='light grey')
        bouton_menu_batons_mag.config(bg='dark grey')
    elif touche == 'Down' and bouton_menu_batons_mag.cget('background') == 'dark grey':
        bouton_menu_arme_to_equipement.config(bg='dark grey')
        bouton_menu_batons_mag.config(bg='light grey')
    elif touche == 'Up' and bouton_menu_arme_to_equipement.cget('background') == 'dark grey':
        bouton_menu_arme_to_equipement.config(bg='light grey')
        bouton_menu_batons_mag.config(bg='dark grey')
    elif touche == 'Up' and bouton_menu_batons_mag.cget('background') == 'dark grey':
        bouton_menu_arme_mag.config(bg='dark grey')
        bouton_menu_batons_mag.config(bg='light grey')
    elif touche == 'Up' and bouton_menu_arme_mag.cget('background') == 'dark grey':
        bouton_menu_arme_mag.config(bg='light grey')
        bouton_menu_arme_phys.config(bg='dark grey')
    elif touche == 'a' and bouton_menu_arme_to_equipement.cget('background') == 'dark grey':
        menu_arme_to_equipement()
    elif touche == 'a' and bouton_menu_arme_phys.cget('background') == 'dark grey':
        menu_arme_to_arme_phys()
    elif touche == 'a' and bouton_menu_arme_mag.cget('background') == 'dark grey':
        menu_arme_to_arme_mag()
    elif touche == 'a' and bouton_menu_batons_mag.cget('background') == 'dark grey':
        menu_arme_to_baton_mag()


def menu_arme_to_baton_mag():
    bouton_menu_arme_phys.grid_forget()
    bouton_menu_arme_mag.grid_forget()
    bouton_menu_batons_mag.grid_forget()
    bouton_menu_arme_to_equipement.grid_forget()
    liste_menu_bat_mag.grid(row=0, column=0)
    bouton_menu_arme_to_choix_arme.grid(row=1, column=0)
    liste_menu_bat_mag.focus_set()
    liste_menu_bat_mag.selection_clear(0, 'end')
    liste_menu_bat_mag.select_set(0)
    liste_menu_bat_mag.activate(0)
    frame_menu_changer_equipement.unbind('<Key>')
    liste_menu_bat_mag.bind('<Key>', clavier_bat_mag)
    vartextupdate_carte('Quelle baton magique souhaitez-vous équiper ?')


def menu_arme_to_arme_mag():
    bouton_menu_arme_phys.grid_forget()
    bouton_menu_arme_mag.grid_forget()
    bouton_menu_batons_mag.grid_forget()
    bouton_menu_arme_to_equipement.grid_forget()
    liste_menu_arme_mag.grid(row=0, column=0)
    bouton_menu_arme_to_choix_arme.grid(row=1, column=0)
    liste_menu_arme_mag.focus_set()
    liste_menu_arme_mag.selection_clear(0, 'end')
    liste_menu_arme_mag.select_set(0)
    liste_menu_arme_mag.activate(0)
    frame_menu_changer_equipement.unbind('<Key>')
    liste_menu_arme_mag.bind('<Key>', clavier_arme_mag)
    vartextupdate_carte('Quelle arme magique souhaitez-vous équiper ?')


def menu_arme_to_arme_phys():
    bouton_menu_arme_phys.grid_forget()
    bouton_menu_arme_mag.grid_forget()
    bouton_menu_batons_mag.grid_forget()
    bouton_menu_arme_to_equipement.grid_forget()
    liste_menu_arme_phys.grid(row=0, column=0)
    bouton_menu_arme_to_choix_arme.grid(row=1, column=0)
    liste_menu_arme_phys.focus_set()
    liste_menu_arme_phys.selection_clear(0, 'end')
    liste_menu_arme_phys.select_set(0)
    liste_menu_arme_phys.activate(0)
    frame_menu_changer_equipement.unbind('<Key>')
    liste_menu_arme_phys.bind('<Key>', clavier_arme_phys)
    vartextupdate_carte('Quelle arme physique souhaitez-vous équiper ?')


def clavier_bat_mag(event):
    touche = event.keysym
    if touche == 'z':
        frame_menu_changer_equipement.focus_set()
        liste_menu_bat_mag.unbind('<Key>')
        frame_menu_changer_equipement.bind('<Key>', menu_equipement_clavier_arme)
        liste_menu_bat_mag.grid_forget()
        bouton_menu_arme_to_choix_arme.grid_forget()
        bouton_menu_arme_phys.grid(row=0, column=0, pady=15)
        bouton_menu_arme_mag.grid(row=1, column=0, pady=15)
        bouton_menu_batons_mag.grid(row=2, column=0, pady=15)
        bouton_menu_arme_to_equipement.grid(row=3, column=0, pady=15)
    elif touche == 'a' and liste_menu_bat_mag.curselection() != ():
        nombre = liste_menu_bat_mag.curselection()[0]
        change_arme(choix_arme_menu())
        liste_menu_bat_mag.activate(nombre)
        liste_menu_bat_mag.select_set(nombre)


def clavier_arme_mag(event):
    touche = event.keysym
    if touche == 'z':
        frame_menu_changer_equipement.focus_set()
        liste_menu_arme_mag.unbind('<Key>')
        frame_menu_changer_equipement.bind('<Key>', menu_equipement_clavier_arme)
        liste_menu_arme_mag.grid_forget()
        bouton_menu_arme_to_choix_arme.grid_forget()
        bouton_menu_arme_phys.grid(row=0, column=0, pady=15)
        bouton_menu_arme_mag.grid(row=1, column=0, pady=15)
        bouton_menu_batons_mag.grid(row=2, column=0, pady=15)
        bouton_menu_arme_to_equipement.grid(row=3, column=0, pady=15)
    elif touche == 'a' and liste_menu_arme_mag.curselection() != ():
        nombre = liste_menu_arme_mag.curselection()[0]
        change_arme(choix_arme_menu())
        liste_menu_arme_mag.activate(nombre)
        liste_menu_arme_mag.select_set(nombre)


def clavier_arme_phys(event):
    touche = event.keysym
    if touche == 'z':
        frame_menu_changer_equipement.focus_set()
        liste_menu_arme_phys.unbind('<Key>')
        frame_menu_changer_equipement.bind('<Key>', menu_equipement_clavier_arme)
        liste_menu_arme_phys.grid_forget()
        bouton_menu_arme_to_choix_arme.grid_forget()
        bouton_menu_arme_phys.grid(row=0, column=0, pady=15)
        bouton_menu_arme_mag.grid(row=1, column=0, pady=15)
        bouton_menu_batons_mag.grid(row=2, column=0, pady=15)
        bouton_menu_arme_to_equipement.grid(row=3, column=0, pady=15)
    elif touche == 'a' and liste_menu_arme_phys.curselection() != ():
        nombre = liste_menu_arme_phys.curselection()[0]
        change_arme(choix_arme_menu())
        liste_menu_arme_phys.activate(nombre)
        liste_menu_arme_phys.select_set(nombre)


def bouton_menu_choix_to_arme():
    frame_menu_changer_equipement.focus_set()
    liste_menu_arme_mag.unbind('<Key>')
    liste_menu_bat_mag.unbind('<Key>')
    liste_menu_arme_phys.unbind('<Key>')
    frame_menu_changer_equipement.bind('<Key>', menu_equipement_clavier_arme)
    liste_menu_arme_mag.grid_forget()
    liste_menu_arme_phys.grid_forget()
    liste_menu_bat_mag.grid_forget()
    bouton_menu_arme_to_choix_arme.grid_forget()
    bouton_menu_arme_phys.grid(row=0, column=0, pady=15)
    bouton_menu_arme_mag.grid(row=1, column=0, pady=15)
    bouton_menu_batons_mag.grid(row=2, column=0, pady=15)
    bouton_menu_arme_to_equipement.grid(row=3, column=0, pady=15)


def clavier_equipement_armure(event):
    touche = event.keysym
    if touche == 'z':
        liste_menu_armure.grid_forget()
        bouton_choix_back_to_equipement_carte.grid_forget()
        bouton_menu_casque_carte.grid(row=0, column=0, pady=15)
        bouton_menu_armure_carte.grid(row=1, column=0, pady=15)
        bouton_menu_botte_carte.grid(row=2, column=0, pady=15)
        bouton_menu_arme_carte.grid(row=3, column=0, pady=15)
        bouton_equipement_back_to_menu_carte.grid(row=4, column=0, pady=15)
        liste_menu_armure.unbind('<Key>')
        frame_menu_changer_equipement.bind('<Key>', menu_equipement_clavier)
        frame_menu_changer_equipement.focus_set()
        vartextupdate_carte('Quel équipement voulez-vous changer ?')
    elif touche == 'a' and liste_menu_armure.curselection() != ():
        nombre = liste_menu_armure.curselection()[0]
        change_armure(choix_armure_menu())
        liste_menu_armure.activate(nombre)
        liste_menu_armure.select_set(nombre)


def clavier_equipement_botte(event):
    touche = event.keysym
    if touche == 'z':
        liste_menu_botte.grid_forget()
        bouton_choix_back_to_equipement_carte.grid_forget()
        bouton_menu_casque_carte.grid(row=0, column=0, pady=15)
        bouton_menu_armure_carte.grid(row=1, column=0, pady=15)
        bouton_menu_botte_carte.grid(row=2, column=0, pady=15)
        bouton_menu_arme_carte.grid(row=3, column=0, pady=15)
        bouton_equipement_back_to_menu_carte.grid(row=4, column=0, pady=15)
        liste_menu_botte.unbind('<Key>')
        frame_menu_changer_equipement.bind('<Key>', menu_equipement_clavier)
        frame_menu_changer_equipement.focus_set()
        vartextupdate_carte('Quel équipement voulez-vous changer ?')
    elif touche == 'a' and liste_menu_botte.curselection() != ():
        nombre = liste_menu_botte.curselection()[0]
        change_botte(choix_botte_menu())
        liste_menu_botte.activate(nombre)
        liste_menu_botte.select_set(nombre)


def clavier_equipement_casque(event):
    touche = event.keysym
    if touche == 'z':
        liste_menu_casque.grid_forget()
        bouton_choix_back_to_equipement_carte.grid_forget()
        bouton_menu_casque_carte.grid(row=0, column=0, pady=15)
        bouton_menu_armure_carte.grid(row=1, column=0, pady=15)
        bouton_menu_botte_carte.grid(row=2, column=0, pady=15)
        bouton_menu_arme_carte.grid(row=3, column=0, pady=15)
        bouton_equipement_back_to_menu_carte.grid(row=4, column=0, pady=15)
        liste_menu_casque.unbind('<Key>')
        frame_menu_changer_equipement.bind('<Key>', menu_equipement_clavier)
        frame_menu_changer_equipement.focus_set()
        vartextupdate_carte('Quel équipement voulez-vous changer ?')
    elif touche == 'a' and liste_menu_casque.curselection() != ():
        nombre = liste_menu_casque.curselection()[0]
        change_casque(choix_casque_menu())
        liste_menu_casque.activate(nombre)
        liste_menu_casque.select_set(nombre)


def menu_back_to_equipement():
    frame_menu_changer_equipement.unbind('<Key>')
    label_narration_carte.place_forget()
    frame_menu_equipement_carte.place_forget()
    label_narration_carte.pack()
    affiche_canvas_carte().pack()
    menu.place(relx=0.5, rely=0.45, anchor=CENTER)
    menu.bind('<Key>', curseur_menu)
    menu.focus_set()


def choix_to_equipement():
    liste_menu_casque.grid_forget()
    liste_menu_casque.unbind('<Key>')
    liste_menu_armure.grid_forget()
    liste_menu_armure.unbind('<Key>')
    liste_menu_botte.grid_forget()
    liste_menu_botte.unbind('<Key>')
    frame_menu_changer_equipement.focus_set()
    frame_menu_changer_equipement.bind('<Key>', menu_equipement_clavier)
    bouton_choix_back_to_equipement_carte.grid_forget()
    bouton_menu_casque_carte.grid(row=0, column=0, pady=15)
    bouton_menu_armure_carte.grid(row=1, column=0, pady=15)
    bouton_menu_botte_carte.grid(row=2, column=0, pady=15)
    bouton_menu_arme_carte.grid(row=3, column=0, pady=15)
    bouton_equipement_back_to_menu_carte.grid(row=4, column=0, pady=15)


def choix_casque_menu():
    if liste_menu_casque.winfo_ismapped():
        nombre = liste_menu_casque.curselection()[0]
        item = liste_menu_casque.get(nombre)
        while item[0] != ')':
            item = item[1:]
        item = item[2:]
        for i in range(len(liste_casque_bis)):
            if liste_casque_bis[i].nom == item:
                return liste_casque_bis[i]
    elif liste_casque_combat.winfo_ismapped() == 1:
        nombre = liste_casque_combat.curselection()[0]
        item = liste_casque_combat.get(nombre)
        while item[0] != ')':
            item = item[1:]
        item = item[2:]
        for i in range(len(liste_casque_bis)):
            if liste_casque_bis[i].nom == item:
                return liste_casque_bis[i]


def choix_armure_menu():
    if liste_menu_armure.winfo_ismapped() == 1:
        nombre = liste_menu_armure.curselection()[0]
        item = liste_menu_armure.get(nombre)
        while item[0] != ')':
            item = item[1:]
        item = item[2:]
        for i in range(len(liste_armures_bis)):
            if liste_armures_bis[i].nom == item:
                return liste_armures_bis[i]
    elif liste_armure_combat.winfo_ismapped() == 1:
        nombre = liste_armure_combat.curselection()[0]
        item = liste_armure_combat.get(nombre)
        while item[0] != ')':
            item = item[1:]
        item = item[2:]
        for i in range(len(liste_armures_bis)):
            if liste_armures_bis[i].nom == item:
                return liste_armures_bis[i]


def choix_botte_menu():
    if liste_menu_botte.winfo_ismapped() == 1:
        nombre = liste_menu_botte.curselection()[0]
        item = liste_menu_botte.get(nombre)
        while item[0] != ')':
            item = item[1:]
        item = item[2:]
        for i in range(len(liste_bottes_bis)):
            if liste_bottes_bis[i].nom == item:
                return liste_bottes_bis[i]
    elif liste_botte_combat.winfo_ismapped() == 1:
        nombre = liste_botte_combat.curselection()[0]
        item = liste_botte_combat.get(nombre)
        while item[0] != ')':
            item = item[1:]
        item = item[2:]
        for i in range(len(liste_bottes_bis)):
            if liste_bottes_bis[i].nom == item:
                return liste_bottes_bis[i]


def choix_arme_menu():
    if liste_menu_arme_phys.winfo_ismapped() == 1:
        nombre = liste_menu_arme_phys.curselection()[0]
        item = liste_menu_arme_phys.get(nombre)
        while item[0] != ')':
            item = item[1:]
        item = item[2:]
        for i in range(len(liste_arme_phys_bis)):
            if liste_arme_phys_bis[i].nom == item:
                return liste_arme_phys_bis[i]
    elif liste_menu_arme_mag.winfo_ismapped() == 1:
        nombre = liste_menu_arme_mag.curselection()[0]
        item = liste_menu_arme_mag.get(nombre)
        while item[0] != ')':
            item = item[1:]
        item = item[2:]
        for i in range(len(liste_arme_mag_bis)):
            if liste_arme_mag_bis[i].nom == item:
                return liste_arme_mag_bis[i]
    elif liste_menu_bat_mag.winfo_ismapped() == 1:
        nombre = liste_menu_bat_mag.curselection()[0]
        item = liste_menu_bat_mag.get(nombre)
        while item[0] != ')':
            item = item[1:]
        item = item[2:]
        for i in range(len(liste_bat_mag_bis)):
            if liste_bat_mag_bis[i].nom == item:
                return liste_bat_mag_bis[i]
    elif fenetre.focus_get() == liste_arme_physique_combat:
        nombre = liste_arme_physique_combat.curselection()[0]
        item = liste_arme_physique_combat.get(nombre)
        while item[0] != ')':
            item = item[1:]
        item = item[2:]
        for i in range(len(liste_arme_phys_bis)):
            if liste_arme_phys_bis[i].nom == item:
                return liste_arme_phys_bis[i]
    elif fenetre.focus_get() == liste_arme_magique_combat:
        nombre = liste_arme_magique_combat.curselection()[0]
        item = liste_arme_magique_combat.get(nombre)
        while item[0] != ')':
            item = item[1:]
        item = item[2:]
        for i in range(len(liste_arme_mag_bis)):
            if liste_arme_mag_bis[i].nom == item:
                return liste_arme_mag_bis[i]
    elif fenetre.focus_get() == liste_baton_magique_combat:
        nombre = liste_baton_magique_combat.curselection()[0]
        item = liste_baton_magique_combat.get(nombre)
        while item[0] != ')':
            item = item[1:]
        item = item[2:]
        for i in range(len(liste_bat_mag_bis)):
            if liste_bat_mag_bis[i].nom == item:
                return liste_bat_mag_bis[i]


# Fonctions combat


def sac_combat():
    if bouton_sac_soins.winfo_ismapped() == 0:
        frame_menu_combat.pack_forget()
        frame_menu_combat.unbind('<Key>')
        frame_sac.pack(side=TOP)
        frame_sac.focus_set()
        frame_sac.bind('<Key>', clavier_sac_combat)
        bouton_sac_soins.config(bg='green')
        bouton_sac_mana.config(bg='light blue')
        bouton_back_sac.config(bg='light grey')
        vartextupdate_combat('Que voulez-vous faire ?')
    elif bouton_sac_soins.winfo_ismapped() == 1:
        frame_sac.pack_forget()
        frame_sac.unbind('<Key>')
        frame_menu_combat.pack()
        frame_menu_combat.focus_set()
        frame_menu_combat.bind('<Key>', clavier_frame_combat)


def clavier_sac_combat(event):
    touche = event.keysym
    if touche == 'Left' and bouton_sac_mana.cget('background') == 'blue':
        bouton_sac_mana.config(bg='light blue')
        bouton_sac_soins.config(bg='green')
    elif touche == 'Right' and bouton_sac_soins.cget('background') == 'green':
        bouton_sac_mana.config(bg='blue')
        bouton_sac_soins.config(bg='light green')
    elif touche == 'Down' and bouton_sac_soins.cget('background') == 'green':
        bouton_back_sac.config(bg='dark grey')
        bouton_sac_soins.config(bg='light green')
    elif touche == 'Down' and bouton_sac_mana.cget('background') == 'blue':
        bouton_sac_mana.config(bg='light blue')
        bouton_back_sac.config(bg='dark grey')
    elif touche == 'Up' and bouton_back_sac.cget('background') == 'dark grey':
        bouton_back_sac.config(bg='light grey')
        bouton_sac_soins.config(bg='green')
    elif touche == 'Right' and bouton_back_sac.cget('background') == 'dark grey':
        bouton_sac_mana.config(bg='blue')
        bouton_back_sac.config(bg='light grey')
    elif touche == 'Left' and bouton_back_sac.cget('background') == 'dark grey':
        bouton_sac_soins.config(bg='green')
        bouton_back_sac.config(bg='light grey')
    elif touche == 'a' and bouton_back_sac.cget('background') == 'dark grey':
        sac_combat()
    elif touche == 'a' and bouton_sac_soins.cget('background') == 'green':
        sac_soin_combat()
    elif touche == 'a' and bouton_sac_mana.cget('background') == 'blue':
        sac_mana_combat()
    elif touche == 'z':
        sac_combat()


def sac_soin_combat():
    if frame_sac_soin.winfo_ismapped() == 0:
        frame_sac.unbind('<Key>')
        frame_sac.pack_forget()
        frame_sac_soin.pack()
        liste_soins_combat.focus_set()
        liste_soins_combat.selection_clear(0, 'end')
        liste_soins_combat.select_set(0)
        liste_soins_combat.activate(0)
        liste_soins_combat.bind('<Key>', clavier_sac_soins_combat)
    if frame_sac_soin.winfo_ismapped() == 1:
        liste_soins_combat.unbind('<Key>')
        frame_sac_soin.pack_forget()
        frame_sac.pack()
        frame_sac.focus_set()
        frame_sac.bind('<Key>', clavier_sac_combat)


def sac_mana_combat():
    if frame_sac_mana.winfo_ismapped() == 0:
        frame_sac.unbind('<Key>')
        frame_sac.pack_forget()
        frame_sac_mana.pack()
        liste_mana_combat.focus_set()
        liste_mana_combat.selection_clear(0, 'end')
        liste_mana_combat.select_set(0)
        liste_mana_combat.activate(0)
        liste_mana_combat.bind('<Key>', clavier_sac_mana_combat)
    if frame_sac_mana.winfo_ismapped() == 1:
        liste_mana_combat.unbind('<Key>')
        frame_sac_mana.pack_forget()
        frame_sac.pack()
        frame_sac.focus_set()
        frame_sac.bind('<Key>', clavier_sac_combat)


def clavier_sac_soins_combat(event):
    touche = event.keysym
    if touche == 'z':
        sac_soin_combat()
    if touche == 'a' and liste_soins_combat.curselection() != ():
        soins_combat()
        combat_test(2, Mechant_humain)


def clavier_sac_mana_combat(event):
    touche = event.keysym
    if touche == 'z':
        sac_mana_combat()
    if touche == 'a' and liste_mana_combat.curselection() != ():
        mana_combat()
        combat_test(3, Mechant_humain)


def fuite_combat():
    canva_combat.pack_forget()
    frame_menu_combat.pack_forget()
    label_narration_carte.pack()
    affiche_canvas_carte().pack()
    frame_menu_combat.unbind('<Key>')
    affiche_canvas_carte().focus_set()
    affiche_canvas_carte().bind('<KeyPress>', clavierbis)
    affiche_canvas_carte().bind('<KeyRelease>', clavierbis)
    changement_route()
    vartext_combat.set('Que voulez-vous faire ?')
    texte_frame_menu_combat.update()
    dev_update()


def soins_combat():
    nombre = liste_soins_combat.curselection()[0]
    item = liste_soins_combat.get(nombre)
    mot = item_finding(item)
    for i in range(len(liste_soins_objets)):
        if liste_soins_objets[i].nom == mot:
            liste_soins_objets[i].quantite -= 1
            for j in range(len(sac_liste[0])):
                if mot == sac_liste[0][j][0]:
                    sac_liste[0][j][1] -= 1
            liste_annexe = []
            for k in range(len(sac_liste[0])):
                if sac_liste[0][k][1] != 0:
                    liste_annexe.append(sac_liste[0][k])
            sac_liste[0] = liste_annexe
            liste_menu_soins_carte.delete(nombre)
            liste_soins_combat.delete(nombre)
            Perso1.soin_objet(liste_soins_objets[i])
            if liste_soins_objets[i].quantite > 0:
                liste_menu_soins_carte.insert(nombre, str(liste_soins_objets[i].nom) + '    x ' + str(
                    liste_soins_objets[i].quantite))
                liste_soins_combat.insert(nombre, str(liste_soins_objets[i].nom) + '    x ' + str(
                    liste_soins_objets[i].quantite))
                liste_soins_combat.select_set(nombre)
                liste_soins_combat.activate(nombre)
            dev_update()


def mana_combat():
    nombre = liste_mana_combat.curselection()[0]
    item = liste_mana_combat.get(nombre)
    mot = item_finding(item)
    for i in range(len(liste_mana_objet)):
        if liste_mana_objet[i].nom == mot:
            liste_mana_objet[i].quantite -= 1
            for j in range(len(sac_liste[1])):
                if mot == sac_liste[1][j][0]:
                    sac_liste[1][j][1] -= 1
            liste_annexe = []
            for k in range(len(sac_liste[1])):
                if sac_liste[1][k][1] != 0:
                    liste_annexe.append(sac_liste[1][k])
            sac_liste[1] = liste_annexe
            liste_menu_mana_carte.delete(nombre)
            liste_mana_combat.delete(nombre)
            Perso1.mana_objet(liste_mana_objet[i])
            if liste_mana_objet[i].quantite > 0:
                liste_menu_mana_carte.insert(nombre, str(liste_mana_objet[i].nom) + '    x ' + str(
                    liste_mana_objet[i].quantite))
                liste_mana_combat.insert(nombre, str(liste_mana_objet[i].nom) + '    x ' + str(
                    liste_mana_objet[i].quantite))
                liste_mana_combat.select_set(nombre)
                liste_mana_combat.activate(nombre)
            dev_update()


def equipement_combat():
    if frame_equipement_combat.winfo_ismapped() == 0:
        frame_menu_combat.pack_forget()
        frame_menu_combat.unbind('<Key>')
        frame_equipement_combat.pack()
        frame_equipement_combat.focus_set()
        bouton_equipement_arme_combat.config(bg='dark grey')
        bouton_back_equipement_to_menu.config(bg='light grey')
        bouton_equipement_armure_combat.config(bg='light grey')
        bouton_equipement_botte_combat.config(bg='light grey')
        bouton_equipement_casque_combat.config(bg='light grey')
        frame_equipement_combat.bind('<Key>', clavier_equipement_combat)
    else:
        frame_equipement_combat.pack_forget()
        frame_equipement_combat.unbind('<Key>')
        frame_menu_combat.pack()
        frame_menu_combat.focus_set()
        frame_menu_combat.bind('<Key>', clavier_frame_combat)


def clavier_equipement_combat(event):
    touche = event.keysym
    if touche == 'Down' and bouton_equipement_arme_combat.cget('background') == 'dark grey':
        bouton_equipement_arme_combat.config(bg='light grey')
        bouton_equipement_armure_combat.config(bg='dark grey')
    elif touche == 'Down' and bouton_equipement_armure_combat.cget('background') == 'dark grey':
        bouton_equipement_armure_combat.config(bg='light grey')
        bouton_back_equipement_to_menu.config(bg='dark grey')
    elif touche == 'Down' and bouton_equipement_casque_combat.cget('background') == 'dark grey':
        bouton_equipement_casque_combat.config(bg='light grey')
        bouton_back_equipement_to_menu.config(bg='dark grey')
    elif touche == 'Down' and bouton_equipement_botte_combat.cget('background') == 'dark grey':
        bouton_equipement_botte_combat.config(bg='light grey')
        bouton_back_equipement_to_menu.config(bg='dark grey')
    elif touche == 'Left' and bouton_back_equipement_to_menu.cget('background') == 'dark grey':
        bouton_back_equipement_to_menu.config(bg='light grey')
        bouton_equipement_casque_combat.config(bg='dark grey')
    elif touche == 'Left' and bouton_equipement_armure_combat.cget('background') == 'dark grey':
        bouton_equipement_armure_combat.config(bg='light grey')
        bouton_equipement_casque_combat.config(bg='dark grey')
    elif touche == 'Left' and bouton_equipement_botte_combat.cget('background') == 'dark grey':
        bouton_equipement_botte_combat.config(bg='light grey')
        bouton_equipement_armure_combat.config(bg='dark grey')
    elif touche == 'Left' and bouton_equipement_arme_combat.cget('background') == 'dark grey':
        bouton_equipement_casque_combat.config(bg='dark grey')
        bouton_equipement_arme_combat.config(bg='light grey')
    elif touche == 'Up' and bouton_equipement_armure_combat.cget('background') == 'dark grey':
        bouton_equipement_arme_combat.config(bg='dark grey')
        bouton_equipement_armure_combat.config(bg='light grey')
    elif touche == 'Up' and bouton_equipement_botte_combat.cget('background') == 'dark grey':
        bouton_equipement_botte_combat.config(bg='light grey')
        bouton_equipement_arme_combat.config(bg='dark grey')
    elif touche == 'Up' and bouton_back_equipement_to_menu.cget('background') == 'dark grey':
        bouton_back_equipement_to_menu.config(bg='light grey')
        bouton_equipement_armure_combat.config(bg='dark grey')
    elif touche == 'Up' and bouton_equipement_casque_combat.cget('background') == 'dark grey':
        bouton_equipement_casque_combat.config(bg='light grey')
        bouton_equipement_arme_combat.config(bg='dark grey')
    elif touche == 'Right' and bouton_equipement_armure_combat.cget('background') == 'dark grey':
        bouton_equipement_botte_combat.config(bg='dark grey')
        bouton_equipement_armure_combat.config(bg='light grey')
    elif touche == 'Right' and bouton_equipement_casque_combat.cget('background') == 'dark grey':
        bouton_equipement_armure_combat.config(bg='dark grey')
        bouton_equipement_casque_combat.config(bg='light grey')
    elif touche == 'Right' and bouton_equipement_arme_combat.cget('background') == 'dark grey':
        bouton_equipement_botte_combat.config(bg='dark grey')
        bouton_equipement_arme_combat.config(bg='light grey')
    elif touche == 'Right' and bouton_back_equipement_to_menu.cget('background') == 'dark grey':
        bouton_equipement_botte_combat.config(bg='dark grey')
        bouton_back_equipement_to_menu.config(bg='light grey')
    elif touche == 'z':
        equipement_combat()
    elif touche == 'a' and bouton_back_equipement_to_menu.cget('background') == 'dark grey':
        equipement_combat()
    elif touche == 'a' and bouton_equipement_arme_combat.cget('background') == 'dark grey':
        equipement_arme_combat()
    elif touche == 'a' and bouton_equipement_casque_combat.cget('background') == 'dark grey':
        equipement_casque_combat()
    elif touche == 'a' and bouton_equipement_armure_combat.cget('background') == 'dark grey':
        equipement_armure_combat()
    elif touche == 'a' and bouton_equipement_botte_combat.cget('background') == 'dark grey':
        equipement_botte_combat()


def equipement_casque_combat():
    bouton_equipement_casque_combat.grid_forget()
    bouton_equipement_armure_combat.grid_forget()
    bouton_equipement_botte_combat.grid_forget()
    bouton_back_equipement_to_menu.grid_forget()
    frame_equipement_arme_combat.grid_forget()
    frame_equipement_combat_personnage.grid_forget()
    liste_casque_combat.grid(row=1, column=1)
    liste_casque_combat.focus_set()
    liste_casque_combat.select_set(0)
    liste_casque_combat.activate(0)
    liste_casque_combat.bind('<Key>', clavier_retour_choix_equipement_combat)
    frame_equipement_combat.unbind('<Key>')
    bouton_back_equipement.grid(row=2, column=1)


def clavier_retour_choix_equipement_combat(event):
    touche = event.keysym
    if touche == 'z':
        retour_equipement_choix_bouton_combat()
    if touche == 'a' and liste_casque_combat.winfo_ismapped() == 1 and liste_casque_combat.curselection() != ():
        combat_test(5, Mechant_humain)
    elif touche == 'a' and liste_armure_combat.winfo_ismapped() == 1 and liste_armure_combat.curselection() != ():
        combat_test(6, Mechant_humain)
    elif touche == 'a' and liste_botte_combat.winfo_ismapped() == 1 and liste_botte_combat.curselection() != ():
        combat_test(7, Mechant_humain)


def equipement_armure_combat():
    bouton_equipement_casque_combat.grid_forget()
    bouton_equipement_armure_combat.grid_forget()
    bouton_equipement_botte_combat.grid_forget()
    bouton_back_equipement_to_menu.grid_forget()
    frame_equipement_arme_combat.grid_forget()
    frame_equipement_combat_personnage.grid_forget()
    liste_armure_combat.grid()
    liste_armure_combat.focus_set()
    liste_armure_combat.select_set(0)
    liste_armure_combat.activate(0)
    liste_armure_combat.bind('<Key>', clavier_retour_choix_equipement_combat)
    frame_equipement_combat.unbind('<Key>')
    bouton_back_equipement.grid(row=2, column=1)


def equipement_botte_combat():
    bouton_equipement_casque_combat.grid_forget()
    bouton_equipement_armure_combat.grid_forget()
    bouton_equipement_botte_combat.grid_forget()
    bouton_back_equipement_to_menu.grid_forget()
    frame_equipement_arme_combat.grid_forget()
    frame_equipement_combat_personnage.grid_forget()
    liste_botte_combat.grid()
    liste_botte_combat.focus_set()
    liste_botte_combat.select_set(0)
    liste_botte_combat.activate(0)
    liste_botte_combat.bind('<Key>', clavier_retour_choix_equipement_combat)
    frame_equipement_combat.unbind('<Key>')
    bouton_back_equipement.grid(row=2, column=1)


def equipement_arme_combat():
    if liste_arme_physique_combat.winfo_ismapped() == 0:
        frame_equipement_combat_bouton.grid_forget()
        frame_equipement_combat_personnage.grid_forget()
        bouton_equipement_arme_combat.grid_forget()
        frame_equipement_combat.unbind('<Key>')
        liste_arme_physique_combat.grid(row=0, column=0)
        liste_arme_magique_combat.grid(row=0, column=1)
        liste_baton_magique_combat.grid(row=0, column=2)
        bouton_back_arme_to_equipement.grid(row=1, column=1)
        liste_arme_physique_combat.focus_set()
        liste_arme_physique_combat.select_set(0)
        liste_arme_physique_combat.activate(0)
        liste_arme_physique_combat.bind('<Key>', clavier_arme_phys_combat)
    else:
        bouton_back_arme_to_equipement.grid_forget()
        liste_arme_physique_combat.grid_forget()
        liste_baton_magique_combat.grid_forget()
        liste_arme_magique_combat.grid_forget()
        bouton_equipement_arme_combat.grid(row=0, column=1)
        frame_equipement_combat.focus_set()
        frame_equipement_combat.bind('<Key>', clavier_equipement_combat)
        frame_equipement_combat_bouton.grid(row=1, column=1, pady=20)
        frame_equipement_combat_personnage.grid(row=2, column=1)


def clavier_arme_phys_combat(event):
    touche = event.keysym
    if touche == 'Right' and fenetre.focus_get() == liste_arme_physique_combat:
        liste_arme_magique_combat.focus_set()
        liste_arme_magique_combat.select_set(0)
        liste_arme_magique_combat.activate(0)
        liste_arme_physique_combat.unbind('<Key>')
        liste_arme_magique_combat.bind('<Key>', clavier_arme_phys_combat)
    elif touche == 'Right' and fenetre.focus_get() == liste_arme_magique_combat:
        liste_baton_magique_combat.focus_set()
        liste_baton_magique_combat.select_set(0)
        liste_baton_magique_combat.activate(0)
        liste_arme_magique_combat.unbind('<Key>')
        liste_baton_magique_combat.bind('<Key>', clavier_arme_phys_combat)
    elif touche == 'Left' and fenetre.focus_get() == liste_baton_magique_combat:
        liste_arme_magique_combat.focus_set()
        liste_arme_magique_combat.select_set(0)
        liste_arme_magique_combat.activate(0)
        liste_baton_magique_combat.unbind('<Key>')
        liste_arme_magique_combat.bind('<Key>', clavier_arme_phys_combat)
    elif touche == 'Left' and fenetre.focus_get() == liste_arme_magique_combat:
        liste_arme_physique_combat.focus_set()
        liste_arme_physique_combat.select_set(0)
        liste_arme_physique_combat.activate(0)
        liste_arme_magique_combat.unbind('<Key>')
        liste_arme_physique_combat.bind('<Key>', clavier_arme_phys_combat)
    elif touche == 'z':
        equipement_arme_combat()
    elif touche =='a' and fenetre.focus_get().curselection() != ():
        combat_test(4, Mechant_humain)


def retour_equipement_choix_bouton_combat():
    liste_botte_combat.grid_forget()
    liste_armure_combat.grid_forget()
    liste_casque_combat.grid_forget()
    bouton_back_equipement.grid_forget()
    frame_equipement_arme_combat.grid(row=0, column=1)
    bouton_equipement_casque_combat.grid(column=0, row=1)
    bouton_equipement_armure_combat.grid(column=1, row=1, padx=20)
    bouton_equipement_botte_combat.grid(column=2, row=1)
    frame_equipement_combat.focus_set()
    frame_equipement_combat.bind('<Key>', clavier_equipement_combat)
    bouton_equipement_casque_combat.config(bg='light grey')
    bouton_equipement_botte_combat.config(bg='light grey')
    bouton_equipement_armure_combat.config(bg='light grey')
    bouton_back_equipement_to_menu.config(bg='light grey')
    bouton_equipement_arme_combat.config(bg='dark grey')
    frame_equipement_combat_personnage.grid(row=2, column=1)
    bouton_back_equipement_to_menu.grid()


def init_combat():
    frame_menu_combat.focus_set()
    bouton_attaque.config(bg='dark grey')
    bouton_fuite.config(bg='light grey')
    bouton_sac.config(bg='light grey')
    bouton_equipement.config(bg='light grey')
    affiche_canvas_carte().unbind('<KeyPress>')
    affiche_canvas_carte().unbind('<KeyRelease>')
    frame_menu_combat.bind('<Key>', clavier_frame_combat)


def clavier_frame_combat(event):
    touche = event.keysym
    if touche == 'Left' and bouton_attaque.cget('background') == 'dark grey':
        bouton_attaque.config(bg='light grey')
        bouton_sac.config(bg='dark grey')
    elif touche == 'Left' and bouton_equipement.cget('background') == 'dark grey':
        bouton_attaque.config(bg='dark grey')
        bouton_equipement.config(bg='light grey')
    elif touche == 'Right' and bouton_sac.cget('background') == 'dark grey':
        bouton_sac.config(bg='light grey')
        bouton_attaque.config(bg='dark grey')
    elif touche == 'Right' and bouton_attaque.cget('background') == 'dark grey':
        bouton_attaque.config(bg='light grey')
        bouton_equipement.config(bg='dark grey')
    elif touche == 'Down' and bouton_attaque.cget('background') == 'dark grey':
        bouton_attaque.config(bg='light grey')
        bouton_fuite.config(bg='dark grey')
    elif touche == 'Down' and bouton_sac.cget('background') == 'dark grey':
        bouton_sac.config(bg='light grey')
        bouton_fuite.config(bg='dark grey')
    elif touche == 'Down' and bouton_equipement.cget('background') == 'dark grey':
        bouton_equipement.config(bg='light grey')
        bouton_fuite.config(bg='dark grey')
    elif touche == 'Up' and bouton_fuite.cget('background') == 'dark grey':
        bouton_attaque.config(bg='dark grey')
        bouton_fuite.config(bg='light grey')
    elif touche == 'Left' and bouton_fuite.cget('background') == 'dark grey':
        bouton_sac.config(bg='dark grey')
        bouton_fuite.config(bg='light grey')
    elif touche == 'Right' and bouton_fuite.cget('background') == 'dark grey':
        bouton_equipement.config(bg='dark grey')
        bouton_fuite.config(bg='light grey')
    elif touche == 'a' and bouton_fuite.cget('background') == 'dark grey':
        fuite_combat()
    elif touche == 'a' and bouton_sac.cget('background') == 'dark grey':
        sac_combat()
    elif touche == 'a' and bouton_equipement.cget('background') == 'dark grey':
        equipement_combat()
    elif touche == 'a' and bouton_attaque.cget('background') == 'dark grey':
        attaque_combat()


def attaque_combat():
    if frame_menu_combat.winfo_ismapped() == 1:
        frame_menu_combat.unbind('<Key>')
        frame_menu_combat.pack_forget()
        frame_attaque_combat.pack()
        frame_attaque_combat.focus_set()
        bouton_attaque_basique.config(bg='dark grey')
        bouton_attaque_spe_1.config(bg='light grey')
        bouton_attaque_spe_2.config(bg='light grey')
        bouton_attaque_spe_3.config(bg='light grey')
        bouton_back_attaque_to_menu.config(bg='light grey')
        frame_attaque_combat.bind('<Key>', clavier_attaque_combat)
    else:
        frame_attaque_combat.unbind('<Key>')
        frame_attaque_combat.pack_forget()
        frame_menu_combat.pack()
        frame_menu_combat.focus_set()
        frame_menu_combat.bind('<Key>', clavier_frame_combat)


def clavier_attaque_combat(event):
    touche = event.keysym
    if touche == "Down" and bouton_attaque_basique.cget('background') == 'dark grey':
        bouton_attaque_basique.config(bg='light grey')
        bouton_attaque_spe_2.config(bg='dark grey')
    elif touche == "Down" and bouton_attaque_basique.cget('background') == 'light grey':
        bouton_attaque_spe_1.config(bg='light grey')
        bouton_attaque_spe_2.config(bg='light grey')
        bouton_attaque_spe_3.config(bg='light grey')
        bouton_back_attaque_to_menu.config(bg='dark grey')
    elif touche == "Left" and bouton_attaque_basique.cget('background') == 'dark grey':
        bouton_attaque_basique.config(bg='light grey')
        bouton_attaque_spe_1.config(bg='dark grey')
    elif touche == "Right" and bouton_attaque_basique.cget('background') == 'dark grey':
        bouton_attaque_basique.config(bg='light grey')
        bouton_attaque_spe_3.config(bg='dark grey')
    elif touche == "Left" and bouton_attaque_spe_2.cget('background') == 'dark grey':
        bouton_attaque_spe_1.config(bg='dark grey')
        bouton_attaque_spe_2.config(bg='light grey')
    elif touche == "Left" and bouton_attaque_spe_3.cget('background') == 'dark grey':
        bouton_attaque_spe_3.config(bg='light grey')
        bouton_attaque_spe_2.config(bg='dark grey')
    elif touche == "Left" and bouton_back_attaque_to_menu.cget('background') == 'dark grey':
        bouton_attaque_spe_1.config(bg='dark grey')
        bouton_back_attaque_to_menu.config(bg='light grey')
    elif touche == "Right" and bouton_attaque_spe_2.cget('background') == 'dark grey':
        bouton_attaque_spe_3.config(bg='dark grey')
        bouton_attaque_spe_2.config(bg='light grey')
    elif touche == "Right" and bouton_attaque_spe_1.cget('background') == 'dark grey':
        bouton_attaque_spe_1.config(bg='light grey')
        bouton_attaque_spe_2.config(bg='dark grey')
    elif touche == "Right" and bouton_back_attaque_to_menu.cget('background') == 'dark grey':
        bouton_back_attaque_to_menu.config(bg='light grey')
        bouton_attaque_spe_3.config(bg='dark grey')
    elif touche == "Up" and bouton_back_attaque_to_menu.cget('background') == 'dark grey':
        bouton_back_attaque_to_menu.config(bg='light grey')
        bouton_attaque_spe_2.config(bg='dark grey')
    elif touche == "Up" and bouton_back_attaque_to_menu.cget('background') == 'light grey':
        bouton_attaque_spe_1.config(bg='light grey')
        bouton_attaque_spe_2.config(bg='light grey')
        bouton_attaque_spe_3.config(bg='light grey')
        bouton_attaque_basique.config(bg='dark grey')
    elif touche == 'z':
        attaque_combat()
    elif touche =='a' and bouton_back_attaque_to_menu.cget('background') == 'dark grey':
        attaque_combat()
    elif touche == 'a' and bouton_attaque_basique.cget('background') == 'dark grey':
        attaque_test(Mechant_humain)


def detourement_images(liste):
    Liste = []
    for i in range(len(liste)):
        array = np.array(liste[i])
        mask = np.all(array == [255, 255, 255, 255], axis=-1)
        array[mask] = [255, 255, 255, 0]
        Liste.append(Image.fromarray(array))
    return Liste


def barre_de_vie_main_perso():
    vie = Perso1.vie
    rapport = vie/Perso1.viemax
    coo = (81, 121, 200, 130)
    coobis = (21, 91, 230, 100)
    coord = coo[0] + int(rapport*(coo[2] - coo[0]))
    coordbis = coobis[0] + int((coobis[2] - coobis[0]) * rapport)
    if Perso1.vie <= 0:
        Perso1.vie = 0
        canva_combat.itemconfig(barre_de_vie, fill='')
        Canva_perso.itemconfig(barre_menu_mana, fill='')
    else:
        canva_combat.itemconfig(barre_de_vie, fill='red')
        Canva_perso.itemconfig(barre_menu_vie, fill='red')
    canva_combat.coords(barre_de_vie, coo[0], coo[1], coord, coo[3])
    Canva_perso.coords(barre_menu_vie, coobis[0], coobis[1], coordbis, coobis[3])
    canva_combat.itemconfig(dev_nombre_de_pts_de_vie_main_perso, text='PV : ' + str(Perso1.vie) + '/' + str(Perso1.viemax))


def barre_de_mana_main_perso():
    mana = Perso1.mana
    rapport = mana/Perso1.manamax
    coo = (81, 151, 180, 155)
    coobis = (21, 111, 230, 120)
    coord = coo[0] + int(rapport*(coo[2] - coo[0]))
    coordbis = coobis[0] + int((coobis[2] - coobis[0]) * rapport)
    if Perso1.mana <= 0:
        Perso1.mana = 0
        canva_combat.itemconfig(barre_de_mana, fill='')
        Canva_perso.itemconfig(barre_menu_mana, fill='')
    else:
        canva_combat.itemconfig(barre_de_mana, fill='blue')
        Canva_perso.itemconfig(barre_menu_mana, fill='blue')
    canva_combat.coords(barre_de_mana, coo[0], coo[1], coord, coo[3])
    Canva_perso.coords(barre_menu_mana, coobis[0], coobis[1], coordbis, coobis[3])
    canva_combat.itemconfig(dev_nombre_de_pts_de_mana_main_perso, text='PM : ' + str(Perso1.mana) + '/' + str(Perso1.manamax))


def barre_dexp_main_perso():
    exp = Perso1.exp
    rapport = exp/Perso1.exprestante
    coo = (81, 151, 180, 155)
    coobis = (21, 131, 190, 135)
    coord = coo[0] + int((coo[2]-coo[0])*rapport)
    coordbis = coobis[0] + int((coobis[2] - coobis[0])*rapport)
    if Perso1.exp == 0:
        canva_combat.itemconfig(barre_dexp, fill='')
        Canva_perso.itemconfig(barre_menu_exp, fill='')
    else:
        canva_combat.itemconfig(barre_dexp, fill='blue')
        Canva_perso.itemconfig(barre_menu_exp, fill='blue')
    canva_combat.coords(barre_dexp, coo[0], coo[1], coord, coo[3])
    Canva_perso.coords(barre_menu_exp, coobis[0], coobis[1], coordbis, coobis[3])


def barre_de_vie_mechants(bonhomme):
    vie = bonhomme.vie
    rapport = vie/bonhomme.viemax
    coo = (401, 181, 520, 190)
    coord = coo[0] + int(rapport*(coo[2]-coo[0]))
    if bonhomme.vie <= 0:
        bonhomme.vie = 0
        canva_combat.itemconfig(barre_de_vie_mechant, fill='')
    else:
        canva_combat.itemconfig(barre_de_vie_mechant, fill='red')
    canva_combat.coords(barre_de_vie_mechant, coo[0], coo[1], coord, coo[3])


def attaque_test(bonhomme):
    frame_attaque_combat.pack_forget()
    frame_menu_combat.pack()
    frame_attaque_combat.unbind('<Key>')
    frame_menu_combat.focus_set()
    bouton_sac.grid_forget()
    bouton_attaque.grid_forget()
    bouton_equipement.grid_forget()
    bouton_fuite.grid_forget()
    vartextupdate_combat('Vous attaquez le méchant !')
    if Perso1.arme is not None and type(Perso1.arme) == type(epee):
        Perso1.attaque_physique_cible(bonhomme)
    elif Perso1.arme is not None and type(Perso1.arme) == type(epeebis):
        if Perso1.arme.attaque_physique >= Perso1.arme.attaque_magique:
            Perso1.attaque_physique_cible(bonhomme)
        else:
            Perso1.attaque_magique_cible(bonhomme)
    else:
        Perso1.attaque_magique_cible(bonhomme)
    barre_de_vie_mechants(bonhomme)
    time.sleep(0.5)
    if bonhomme.vie <= 0:
        vartextupdate_combat('Le méchant est KO !')
        time.sleep(0.7)
        win_exp(bonhomme.exp)
        Perso1.get_argent(bonhomme.argent)
        vartextupdate_combat('Vous avez gagné ' + str(bonhomme.exp) + " pts d'exp !")
        time.sleep(1.5)
        bouton_attaque.grid(row=1, column=1)
        bouton_sac.grid(row=2, column=0)
        bouton_equipement.grid(row=2, column=2)
        bouton_fuite.grid(row=3, column=1)
        bonhomme.vie = bonhomme.viemax
        barre_de_vie_mechants(bonhomme)
        dev_update()
        global current_key
        current_key = None
        fuite_combat()
        move_rectangle()
    else:
        attaque_mechant(bonhomme)


def attaque_mechant(bonhomme):
    vartextupdate_combat('Le méchant vous attaque !')
    time.sleep(0.5)
    bonhomme.attaque_physique_cible(Perso1)
    barre_de_vie_main_perso()
    bouton_attaque.grid(row=1, column=1)
    bouton_sac.grid(row=2, column=0)
    bouton_equipement.grid(row=2, column=2)
    bouton_fuite.grid(row=3, column=1)
    frame_menu_combat.focus_set()
    frame_menu_combat.bind('<Key>', clavier_frame_combat)
    vartextupdate_combat('Que voulez-vous faire ?')


def win_exp(exp):
    Perso1.exp += exp
    barre_dexp_main_perso()
    time.sleep(0.5)
    if Perso1.exp >= Perso1.exprestante:
        while Perso1.exp >= Perso1.exprestante:
            difference = Perso1.exp - Perso1.exprestante
            Perso1.niveau += 1
            Perso1.exp = difference
            Perso1.exprestante = int(0.919 + 2.4 * Perso1.niveau + 2.4 * (Perso1.niveau ** 2))
            barre_dexp_main_perso()
            canva_combat.itemconfig(dev_niveau_perso_combat, text=str(Perso1.nom) + '  niv: ' + str(Perso1.niveau))


def dev_update():
    canva_combat.itemconfig(dev_niveau_perso_combat, text=str(Perso1.nom) + '  niv: ' + str(Perso1.niveau))
    canva_combat.itemconfig(dev_nombre_de_pts_de_vie_main_perso, text='PV : ' + str(Perso1.vie) + '/' + str(Perso1.viemax))
    canva_combat.itemconfig(dev_nombre_de_pts_de_mana_main_perso, text='PM : ' + str(Perso1.mana) + '/' + str(Perso1.manamax))
    Canva_perso.itemconfig(dev_def_perso, text='Def : ' + str(Perso1.defense_physique))
    Canva_perso.itemconfig(dev_defmag_perso, text='Def mag : ' + str(Perso1.defense_magique))
    Canva_perso.itemconfig(dev_atk_perso, text='Atk : ' + str(Perso1.attaque_physique))
    Canva_perso.itemconfig(dev_atkmag_perso, text='Atk mag : ' + str(Perso1.attaque_magique))
    Canva_perso.itemconfig(dev_vie_perso, text='PV : ' + str(Perso1.vie) + '/' + str(Perso1.viemax))
    Canva_perso.itemconfig(dev_mana_perso, text='PM : ' + str(Perso1.mana) + '/' + str(Perso1.manamax))
    Canva_perso.itemconfig(dev_exp_perso, text=str(Perso1.exp) + '/' + str(Perso1.exprestante))
    texte_magasin_money.config(text='Vous avez ' + str(Perso1.argent) + ' Po')
    texte_money_vendre.config(text='Vous avez ' + str(Perso1.argent) + ' Po')
    barre_dexp_main_perso()
    barre_de_vie_main_perso()
    Canva_perso.itemconfig(dev_money_perso, text='Argent: ' + str(Perso1.argent) + ' Po')


def combat_test(choix, bonhomme):
    if choix == 1: #attaque basique
        frame_attaque_combat.pack_forget()
        frame_menu_combat.pack()
        frame_attaque_combat.unbind('<Key>')
        frame_menu_combat.focus_set()
        bouton_sac.grid_forget()
        bouton_attaque.grid_forget()
        bouton_equipement.grid_forget()
        bouton_fuite.grid_forget()
        vartextupdate_combat('Vous attaquez le méchant !')
        if Perso1.arme is not None and type(Perso1.arme) == type(epee):
            Perso1.attaque_physique_cible(bonhomme)
        elif Perso1.arme is not None and type(Perso1.arme) == type(epeebis):
            if Perso1.arme.attaque_physique >= Perso1.arme.attaque_magique:
                Perso1.attaque_physique_cible(bonhomme)
            else:
                Perso1.attaque_magique_cible(bonhomme)
        else:
            Perso1.attaque_magique_cible(bonhomme)
        barre_de_vie_mechants(bonhomme)

    elif choix == 2: #soins
        frame_sac_soin.unbind('<Key>')
        frame_sac.unbind('<Key>')
        frame_sac_soin.pack_forget()
        frame_sac.pack_forget()
        frame_menu_combat.pack()
        frame_menu_combat.focus_set()
        frame_menu_combat.unbind('<Key>')
        frame_menu_combat.focus_set()
        bouton_sac.grid_forget()
        bouton_attaque.grid_forget()
        bouton_equipement.grid_forget()
        bouton_fuite.grid_forget()
        vartextupdate_combat('Vous avez regagné des PV !')
        time.sleep(0.5)

    elif choix == 3: # mana
        frame_sac_mana.unbind('<Key>')
        frame_sac.unbind('<Key>')
        frame_sac_mana.pack_forget()
        frame_menu_combat.focus_set()
        frame_sac.pack_forget()
        frame_menu_combat.pack()
        frame_menu_combat.focus_set()
        frame_menu_combat.unbind('<Key>')
        frame_menu_combat.focus_set()
        bouton_sac.grid_forget()
        bouton_attaque.grid_forget()
        bouton_equipement.grid_forget()
        bouton_fuite.grid_forget()
        vartextupdate_combat('Vous avez regagné des PM !')
        time.sleep(0.5)

    elif choix == 4: #equipement arme
        change_arme(choix_arme_menu())
        frame_menu_combat.unbind('<Key>')
        liste_arme_physique_combat.unbind('<Key>')
        liste_arme_magique_combat.unbind('<Key>')
        liste_baton_magique_combat.unbind('<Key>')
        vartextupdate_combat("Vous avez changé d'arme !")
        time.sleep(0.5)
        equipement_arme_combat()
        equipement_combat()
        frame_menu_combat.focus_set()
        bouton_sac.grid_forget()
        bouton_attaque.grid_forget()
        bouton_equipement.grid_forget()
        bouton_fuite.grid_forget()

    elif choix == 5: #equipement casques
        change_casque(choix_casque_menu())
        frame_menu_combat.unbind('<Key>')
        liste_casque_combat.unbind('<Key>')
        vartextupdate_combat("Vous avez changé de casque !")
        time.sleep(0.5)
        retour_equipement_choix_bouton_combat()
        equipement_combat()
        frame_menu_combat.focus_set()
        bouton_sac.grid_forget()
        bouton_attaque.grid_forget()
        bouton_equipement.grid_forget()
        bouton_fuite.grid_forget()

    elif choix == 6: # equipement armure
        change_armure(choix_armure_menu())
        frame_menu_combat.unbind('<Key>')
        liste_armure_combat.unbind('<Key>')
        vartextupdate_combat("Vous avez changé d'armure !")
        time.sleep(0.5)
        retour_equipement_choix_bouton_combat()
        equipement_combat()
        frame_menu_combat.focus_set()
        bouton_sac.grid_forget()
        bouton_attaque.grid_forget()
        bouton_equipement.grid_forget()
        bouton_fuite.grid_forget()

    elif choix == 7: # equipement bottes
        change_botte(choix_botte_menu())
        frame_menu_combat.unbind('<Key>')
        liste_botte_combat.unbind('<Key>')
        vartextupdate_combat("Vous avez changé de bottes !")
        time.sleep(0.5)
        retour_equipement_choix_bouton_combat()
        equipement_combat()
        frame_menu_combat.focus_set()
        bouton_sac.grid_forget()
        bouton_attaque.grid_forget()
        bouton_equipement.grid_forget()
        bouton_fuite.grid_forget()
    if bonhomme.vie <= 0:
        vartextupdate_combat('Le méchant est KO !')
        time.sleep(0.7)
        win_exp(bonhomme.exp)
        Perso1.get_argent(bonhomme.argent)
        vartextupdate_combat('Vous avez gagné ' + str(bonhomme.exp) + " pts d'exp !")
        time.sleep(1.5)
        bouton_attaque.grid(row=1, column=1)
        bouton_sac.grid(row=2, column=0)
        bouton_equipement.grid(row=2, column=2)
        bouton_fuite.grid(row=3, column=1)
        bonhomme.vie = bonhomme.viemax
        barre_de_vie_mechants(bonhomme)
        dev_update()
        global current_key
        current_key = None
        fuite_combat()
        move_rectangle()
    else:
        attaque_mechant(bonhomme)


# Fonctions enregistrement


def enregistrement_perso():
    Perso1.coord = (int(affiche_canvas_carte().coords(liste_canvas_obstacles_herbes_capteurs[affiche_reste_carte()][4])[0]), int(affiche_canvas_carte().coords(liste_canvas_obstacles_herbes_capteurs[affiche_reste_carte()][4])[1]))
    fichier = open('New_Game_Main_Character.txt', 'w')
    fichier.write(str(Perso1.nom)+'\n')
    fichier.write(str(Perso1.argent) + '\n')
    fichier.write(str(Perso1.vie) + '\n')
    fichier.write(str(Perso1.exp) + '\n')
    fichier.write(str(Perso1.niveau) + '\n')
    fichier.write(str(Perso1.exprestante) + '\n')
    fichier.write(str(Perso1.viemax) + '\n')
    fichier.write(str(Perso1.attaque_physique) + '\n')
    fichier.write(str(Perso1.defense_physique) + '\n')
    fichier.write(str(Perso1.mana) + '\n')
    fichier.write(str(Perso1.manamax) + '\n')
    fichier.write(str(Perso1.regeneration_mana) + '\n')
    fichier.write(str(Perso1.critique) + '\n')
    fichier.write(str(Perso1.defense_magique) + '\n')
    fichier.write(str(Perso1.attaque_magique) + '\n')
    fichier.write(str(Perso1.type) + '\n')
    fichier.write(str(Perso1.etat) + '\n')
    fichier.write(str(Perso1.capacite1) + '\n')
    fichier.write(str(Perso1.capacite2) + '\n')
    fichier.write(str(Perso1.capacite3) + '\n')
    fichier.write(str(Perso1.capacite4) + '\n')
    fichier.write(str(Perso1.capacite5) + '\n')
    fichier.write(str(Perso1.capacite6) + '\n')
    fichier.write(str(Perso1.position) + '\n')
    b = '('
    premier = Perso1.coord[0]
    if len(str(premier)) == 1:
        b += "00" + str(premier)
    elif len(str(premier)) == 2:
        b += "0" + str(premier)
    else:
        b += str(premier)
    b += ", "
    deuxieme = Perso1.coord[1]
    if len(str(deuxieme)) == 1:
        b += "00" + str(deuxieme)
    elif len(str(deuxieme)) == 2:
        b += "0" + str(deuxieme)
    else:
        b += str(deuxieme)
    b += ')'
    fichier.write(b + '\n')
    fichier.write('\n')
    fichier.close()


def bis_enregistrement_equipement():
    fichier = open('New_Game_Equipement.txt', 'w')
    for i in range(len(equipement_liste)):
        for j in range(len(equipement_liste[i])):
            fichier.write(equipement_liste[i][j][0] + '\t' + str(equipement_liste[i][j][1]) + '\t' + str(equipement_liste[i][j][2]) + '\n')
        fichier.write('\n')
    fichier.close()


def recherche_equipement_bis():
    fichier = open('New_Game_Equipement.txt', 'r')
    L_equip = []
    L_tempo = []
    for ligne in fichier:
        if ligne != '\n':
            a = ligne.strip()
            a = a.split('\t')
            L_tempo.append([a[0], int(a[1]), int(a[2])])
        else:
            L_equip.append(L_tempo)
            L_tempo = []
    return L_equip


def init_bis_equip():
    liste_arme_phys = equipement_liste[0]
    for i in range(len(liste_arme_phys)):
        objet = '(' + str(liste_arme_phys[i][1]) + ') ' + liste_arme_phys[i][0]
        if liste_arme_phys[i][2] == 1:
            for j in range(len(liste_arme_phys_bis)):
                if liste_arme_phys_bis[j].nom == liste_arme_phys[i][0]:
                    Perso1.get_arme(liste_arme_phys_bis[j])
                    liste_arme_physique_combat.insert(i + 1, '* ' + objet)
                    liste_menu_arme_phys.insert(i + 1, '* ' + objet)
        else:
            liste_arme_physique_combat.insert(i + 1, objet)
            liste_menu_arme_phys.insert(i + 1, objet)
    liste_arme_mag = equipement_liste[1]
    for i in range(len(liste_arme_mag)):
        objet = '(' + str(liste_arme_mag[i][1]) + ') ' + liste_arme_mag[i][0]
        if liste_arme_mag[i][2] == 1:
            for j in range(len(liste_arme_mag_bis)):
                if liste_arme_mag_bis[j].nom == liste_arme_mag[i][0]:
                    Perso1.get_arme(liste_arme_mag_bis[j])
                    liste_arme_magique_combat.insert(i + 1, '* ' + objet)
                    liste_menu_arme_mag.insert(i + 1, '* ' + objet)
        else:
            liste_arme_magique_combat.insert(i + 1, objet)
            liste_menu_arme_mag.insert(i + 1, objet)
    liste_bat_mag = equipement_liste[2]
    for i in range(len(liste_bat_mag)):
        objet = '(' + str(liste_bat_mag[i][1]) + ') ' + liste_bat_mag[i][0]
        if liste_bat_mag[i][2] == 1:
            for j in range(len(liste_bat_mag_bis)):
                if liste_bat_mag_bis[j].nom == liste_bat_mag[i][0]:
                    Perso1.get_arme(liste_bat_mag_bis[j])
                    liste_baton_magique_combat.insert(i + 1, '* ' + objet)
                    liste_menu_bat_mag.insert(i + 1, '* ' + objet)
        else:
            liste_baton_magique_combat.insert(i + 1, objet)
            liste_menu_bat_mag.insert(i + 1, objet)
    liste_casque = equipement_liste[3]
    for i in range(len(liste_casque)):
        objet = '(' + str(liste_casque[i][1]) + ') ' + liste_casque[i][0]
        if liste_casque[i][2] == 1:
            for j in range(len(liste_casque_bis)):
                if liste_casque_bis[j].nom == liste_casque[i][0]:
                    Perso1.get_casque(liste_casque_bis[j])
                    liste_casque_combat.insert(i + 1, '* ' + objet)
                    liste_menu_casque.insert(i + 1, '* ' + objet)
        else:
            liste_casque_combat.insert(i + 1, objet)
            liste_menu_casque.insert(i + 1, objet)
    liste_armure = equipement_liste[4]
    for i in range(len(liste_armure)):
        objet = '(' + str(liste_armure[i][1]) + ') ' + liste_armure[i][0]
        if liste_armure[i][2] == 1:
            for j in range(len(liste_armures_bis)):
                if liste_armures_bis[j].nom == liste_armure[i][0]:
                    Perso1.get_armure(liste_armures_bis[j])
                    liste_armure_combat.insert(i + 1, '* ' + objet)
                    liste_menu_armure.insert(i + 1, '* ' + objet)
        else:
            liste_armure_combat.insert(i + 1, objet)
            liste_menu_armure.insert(i + 1, objet)
    liste_bottes = equipement_liste[5]
    for i in range(len(liste_bottes)):
        objet = '(' + str(liste_bottes[i][1]) + ') ' + liste_bottes[i][0]
        if liste_bottes[i][2] == 1:
            for j in range(len(liste_bottes_bis)):
                if liste_bottes_bis[j].nom == liste_bottes[i][0]:
                    Perso1.get_botte(liste_bottes_bis[j])
                    liste_botte_combat.insert(i + 1, '* ' + objet)
                    liste_menu_botte.insert(i + 1, '* ' + objet)
        else:
            liste_botte_combat.insert(i + 1, objet)
            liste_menu_botte.insert(i + 1, objet)


def change_casque(objet):
    Perso1.get_casque(objet)
    liste = equipement_liste[3]
    for i in range(len(liste)):
        if liste[i][0] == objet.nom:
            liste[i][2] = 1
        else:
            liste[i][2] = 0
    liste_casque_combat.delete(0, 'end')
    liste_menu_casque.delete(0, 'end')
    for i in range(len(liste)):
        if liste[i][2] == 1:
            liste_casque_combat.insert(liste_casque_combat.size() + 1, '* (' + str(objet.niveau) + ') ' + str(objet.nom))
            liste_menu_casque.insert(liste_menu_casque.size() +1, '* (' + str(objet.niveau) + ') ' + str(objet.nom))
            liste_casque_combat.select_set(liste_casque_combat.size())
            liste_casque_combat.activate(liste_casque_combat.size())
        else:
            liste_casque_combat.insert(liste_casque_combat.size() + 1, '(' + str(liste[i][1]) + ') ' + str(liste[i][0]))
            liste_menu_casque.insert(liste_menu_casque.size() + 1, '(' + str(liste[i][1]) + ') ' + str(liste[i][0]))


def change_armure(objet):
    Perso1.get_armure(objet)
    liste = equipement_liste[4]
    for i in range(len(liste)):
        if liste[i][0] == objet.nom:
            liste[i][2] = 1
        else:
            liste[i][2] = 0
    liste_armure_combat.delete(0, 'end')
    liste_menu_armure.delete(0, 'end')
    for i in range(len(liste)):
        if liste[i][2] == 1:
            liste_armure_combat.insert(liste_armure_combat.size() + 1, '* (' + str(objet.niveau) + ') ' + str(objet.nom))
            liste_menu_armure.insert(liste_menu_armure.size() + 1, '* (' + str(objet.niveau) + ') ' + str(objet.nom))
            liste_armure_combat.select_set(liste_armure_combat.size() + 1)
            liste_armure_combat.activate(liste_armure_combat.size() + 1)
        else:
            liste_armure_combat.insert(liste_armure_combat.size() + 1, '(' + str(liste[i][1]) + ') ' + str(liste[i][0]))
            liste_menu_armure.insert(liste_menu_armure.size() + 1, '(' + str(liste[i][1]) + ') ' + str(liste[i][0]))


def change_botte(objet):
    Perso1.get_botte(objet)
    liste = equipement_liste[5]
    for i in range(len(liste)):
        if liste[i][0] == objet.nom:
            liste[i][2] = 1
        else:
            liste[i][2] = 0
    liste_botte_combat.delete(0, 'end')
    liste_menu_botte.delete(0, 'end')
    for i in range(len(liste)):
        if liste[i][2] == 1:
            liste_botte_combat.insert(liste_botte_combat.size() + 1, '* (' + str(objet.niveau) + ') ' + str(objet.nom))
            liste_menu_botte.insert(liste_menu_botte.size() + 1, '* (' + str(objet.niveau) + ') ' + str(objet.nom))
            liste_botte_combat.select_set(liste_botte_combat.size() + 1)
            liste_botte_combat.activate(liste_botte_combat.size() + 1)
        else:
            liste_botte_combat.insert(liste_botte_combat.size() + 1, '(' + str(liste[i][1]) + ') ' + str(liste[i][0]))
            liste_menu_botte.insert(liste_menu_botte.size() + 1, '(' + str(liste[i][1]) + ') ' + str(liste[i][0]))


def change_arme(objet):
    Perso1.get_arme(objet)
    for i in range(3):
        liste = equipement_liste[i]
        for j in range(len(liste)):
            if liste[j][0] == objet.nom:
                liste[j][2] = 1
            else:
                liste[j][2] = 0
        if i == 0:
            liste_arme_physique_combat.delete(0, 'end')
            liste_menu_arme_phys.delete(0, 'end')
            for j in range(len(liste)):
                if liste[j][2] == 1:
                    liste_arme_physique_combat.insert(liste_arme_physique_combat.size() + 1, '* (' + str(objet.niveau) + ') ' + str(objet.nom))
                    liste_menu_arme_phys.insert(liste_menu_arme_phys.size() + 1, '* (' + str(objet.niveau) + ') ' + str(objet.nom))
                    liste_arme_physique_combat.select_set(liste_arme_physique_combat.size() + 1)
                    liste_arme_physique_combat.activate(liste_arme_physique_combat.size() + 1)
                else:
                    liste_arme_physique_combat.insert(liste_arme_physique_combat.size() + 1, '(' + str(liste[j][1]) + ') ' + str(liste[i][0]))
                    liste_menu_arme_phys.insert(liste_menu_arme_phys.size() + 1, '(' + str(liste[j][1]) + ') ' + str(liste[i][0]))
        if i == 1:
            liste_arme_magique_combat.delete(0, 'end')
            liste_menu_arme_mag.delete(0, 'end')
            for j in range(len(liste)):
                if liste[j][2] == 1:
                    liste_arme_magique_combat.insert(liste_arme_magique_combat.size() + 1,
                                                      '* (' + str(objet.niveau) + ') ' + str(objet.nom))
                    liste_menu_arme_mag.insert(liste_menu_arme_mag.size() + 1,
                                                '* (' + str(objet.niveau) + ') ' + str(objet.nom))
                    liste_arme_magique_combat.select_set(liste_arme_magique_combat.size() + 1)
                    liste_arme_magique_combat.activate(liste_arme_magique_combat.size() + 1)
                else:
                    liste_arme_magique_combat.insert(liste_arme_magique_combat.size() + 1,
                                                      '(' + str(liste[j][1]) + ') ' + str(liste[j][0]))
                    liste_menu_arme_mag.insert(liste_menu_arme_mag.size() + 1,
                                                '(' + str(liste[j][1]) + ') ' + str(liste[j][0]))
        if i == 2:
            liste_baton_magique_combat.delete(0, 'end')
            liste_menu_bat_mag.delete(0, 'end')
            for j in range(len(liste)):
                if liste[j][2] == 1:
                    liste_baton_magique_combat.insert(liste_baton_magique_combat.size() + 1,
                                                      '* (' + str(objet.niveau) + ') ' + str(objet.nom))
                    liste_menu_bat_mag.insert(liste_menu_bat_mag.size() + 1,
                                                '* (' + str(objet.niveau) + ') ' + str(objet.nom))
                    liste_baton_magique_combat.select_set(liste_baton_magique_combat.size() + 1)
                    liste_baton_magique_combat.activate(liste_baton_magique_combat.size() + 1)
                else:
                    liste_baton_magique_combat.insert(liste_baton_magique_combat.size() + 1,
                                                      '(' + str(liste[j][1]) + ') ' + str(liste[j][0]))
                    liste_menu_bat_mag.insert(liste_menu_bat_mag.size() + 1,
                                                '(' + str(liste[j][1]) + ') ' + str(liste[j][0]))


def enregistrement_sac():
    fichier = open('New_Game_Sac.txt', 'w')
    for i in range(len(sac_liste)):
        for j in range(len(sac_liste[i])):
            fichier.write(sac_liste[i][j][0] + '\t' + str(sac_liste[i][j][1]) + '\n')
        fichier.write('\n')
    fichier.close()


def recherche_perso():
    fichier = open('New_Game_Main_Character.txt', 'r')
    L = []
    for ligne in fichier:
        if ligne == "\n":
            break
        a = ligne.strip()
        L.append(a)
    L[24] = (int(L[24][1:4]), int(L[24][6:9]))
    for i in range(len(L)):
        if L[i] == "None":
            L[i] = None
    Perso_return = Class_jeu_1.Main_perso(L[0], int(L[1]), int(L[2]), int(L[3]), int(L[4]), int(L[5]), int(L[6]),
                                          int(L[7]), int(L[8]), int(L[9]), int(L[10]), int(L[11]), float(L[12]),
                                          int(L[13]), int(L[14]), L[15], L[16], L[17], L[18], L[19], L[20], L[21],
                                          L[22], int(L[23]), L[24])
    return Perso_return


def recherche_sac():
    fichier = open('New_Game_Sac.txt', 'r')
    L_sac = []
    L_tempo = []
    for ligne in fichier:
        if ligne != '\n':
            a = ligne.strip()
            a = a.split('\t')
            L_tempo.append([a[0], int(a[1])])
        else:
            L_sac.append(L_tempo)
            L_tempo = []
    return L_sac


def changer_texte_combat(texte):
    vartext_combat.set(texte)
    texte_frame_menu_combat.update()


def init_sac_soins():
    liste_soins = sac_liste[0]
    for i in range(len(liste_soins)):
        objet = liste_soins[i][0] + '    x ' + str(liste_soins[i][1])
        liste_soins_combat.insert(i+1, objet)
        liste_menu_soins_carte.insert(i+1, objet)
        for j in range(len(liste_soins_objets)):
            if liste_soins[i][0] == liste_soins_objets[j].nom:
                liste_soins_objets[j].quantite = liste_soins[i][1]
    liste_compare = []
    for k in range(len(liste_soins)):
        liste_compare.append(liste_soins[k][0])
    for l in range(len(liste_soins_objets)):
        if liste_soins_objets[l].nom not in liste_compare:
            liste_soins_objets[l].quantite = 0


def init_sac_mana():
    liste_manas = sac_liste[1]
    for i in range(len(liste_manas)):
        objet = liste_manas[i][0] + '    x ' + str(liste_manas[i][1])
        liste_mana_combat.insert(i+1, objet)
        liste_menu_mana_carte.insert(i+1, objet)
        for j in range(len(liste_mana_objet)):
            if liste_manas[i][0] == liste_mana_objet[j].nom:
                liste_mana_objet[j].quantite = liste_manas[i][1]
    liste_compare = []
    for k in range(len(liste_manas)):
        liste_compare.append(liste_manas[k][0])
    for l in range(len(liste_mana_objet)):
        if liste_mana_objet[l].nom not in liste_compare:
            liste_mana_objet[l].quantite = 0


def init_magasin():
    for j in range(len(liste_magasin[0])):
        liste_soins_magasin.insert(j+1, str(liste_magasin[0][j].nom) + '     ' + str(liste_magasin[0][j].prix) + ' Po')
    for j in range(len(liste_magasin[1])):
        liste_mana_magasin.insert(j+1, str(liste_magasin[1][j].nom) + '     ' + str(liste_magasin[1][j].prix) + ' Po')
    for j in range(len(liste_magasin[2])):
        liste_objet_magasin.insert(j+1, str(liste_magasin[2][j].nom) + '     ' + str(liste_magasin[2][j].prix) + ' Po')


def init_sac_utilitaires():
    liste_util = sac_liste[2]
    for i in range(len(liste_util)):
        objet = liste_util[i][0] + '    x ' + str(liste_util[i][1])
        liste_menu_utilitaires_carte.insert(i+1, objet)
        for j in range(len(liste_utilitaire_objet)):
            if liste_util[i][0] == liste_utilitaire_objet[j].nom:
                liste_utilitaire_objet[j].quantite = liste_util[i][1]
    liste_compare = []
    for k in range(len(liste_util)):
        liste_compare.append(liste_util[k][0])
    for l in range(len(liste_utilitaire_objet)):
        if liste_utilitaire_objet[l].nom not in liste_compare:
            liste_utilitaire_objet[l].quantite = 0


def init_sac_objetrares():
    liste_obj = sac_liste[3]
    for i in range(len(liste_obj)):
        objet = liste_obj[i][0]
        liste_menu_objetrares_carte.insert(i+1, objet)


def affiche_canvas_carte():
    numero = Perso1.position
    return liste_canvas_obstacles_herbes_capteurs[numero-1][0]


def affiche_reste_carte():
    return Perso1.position - 1


def liste_capteurss():
    liste = []
    for i in range(len(liste_canvas_obstacles_herbes_capteurs[affiche_reste_carte()][3])):
        liste.append(liste_canvas_obstacles_herbes_capteurs[affiche_reste_carte()][3][i])
    liste_capt = []
    for i in liste:
        liste_capt.append(i[0])
    return liste_capt


def changement_carte():
    liste_valeur = liste_canvas_obstacles_herbes_capteurs[affiche_reste_carte()][3]
    for i in range(len(liste_valeur)):
        if verif_collision_carte(liste_canvas_obstacles_herbes_capteurs[affiche_reste_carte()][4], [liste_valeur[i][0]], affiche_canvas_carte())[0][0]:
            affiche_canvas_carte().itemconfigure(liste_canvas_obstacles_herbes_capteurs[affiche_reste_carte()][4],
                                                 state='hidden')
            canva_combat.pack_forget()
            frame_menu_combat.pack_forget()
            a = affiche_canvas_carte().coords(liste_canvas_obstacles_herbes_capteurs[affiche_reste_carte()][4])[0]
            b = affiche_canvas_carte().coords(liste_canvas_obstacles_herbes_capteurs[affiche_reste_carte()][4])[1]
            a = changement_coordonnees(a, b)[0]
            b = changement_coordonnees(a, b)[1]
            affiche_canvas_carte().pack_forget()
            Perso1.position = liste_canvas_obstacles_herbes_capteurs[affiche_reste_carte()][3][i][1]
            affiche_canvas_carte().pack()
            affiche_canvas_carte().itemconfigure(liste_canvas_obstacles_herbes_capteurs[affiche_reste_carte()][4],
                                                 state='normal')
            affiche_canvas_carte().coords(liste_canvas_obstacles_herbes_capteurs[affiche_reste_carte()][4], a, b, a + 50, b + 50)
            affiche_canvas_carte().tag_raise(liste_canvas_obstacles_herbes_capteurs[affiche_reste_carte()][4])
            affiche_canvas_carte().focus_set()
            changement_route()
            return 1
    return 0


def changement_coordonnees(a, b):
    if a == 700:
        a -= 690
    if a == 0:
        a += 690
    if b == 550:
        b -= 540
    if b == 0:
        b += 540
    return [a, b]


def changement_route():
    numero_tableau = affiche_reste_carte() + 1
    for i in range(len(liste_route)):
        for j in liste_route[i][1:]:
            if numero_tableau == j:
                vartextupdate_carte(liste_route[i][0])
                break


def mechant_bonhomme():
    numero = Perso1.position
    a = ''
    for i in range(len(liste_route)):
        for elem in liste_route[i]:
            if numero == elem:
                a = liste_route[i][0]
    if a == 'Route 1':
        niveau_mechant = [2, 3, 4]
        nom_mechant = []
        argent_mechant = 12*niveau_mechant

        #nom, argent, vie, exp, niveau, viemax, attaque_physique, defense_physique, mana, manamax,
                 #regeneration_mana, critique, defense_magique, attaque_magique, type, statut, etat


def shop():
    affiche_canvas_carte().unbind('<KeyPress>')
    affiche_canvas_carte().unbind('<KeyRelease>')


fenetre = Tk()
fenetre.minsize(1080, 720)
fenetre.geometry('1080x720')


# Creation personnages tests


Perso1 = recherche_perso()
Mechant_monstre = Class_jeu_1.Mechant("Monstre", 1000, 20, 10, 0, 20, 2, 2, 0, 0, 0, 1.5, 2, 2, ("neutre", "neutre"), "monstre", "normal")
Mechant_humain = Class_jeu_1.Mechant("Stan", 200, 20, 10, 0, 20, 8, 2, 0, 0, 0, 1.5, 2, 2, ("neutre", "neutre"), "humain", "normal")
Potion = Class_jeu_1.Objet_soin("Potion", 20, "aha", 10, 1, 6)
Super_potion = Class_jeu_1.Objet_soin("Super potion", 100, 'oho', 100, 5, 2)
Petite_fiole = Class_jeu_1.Objet_mana("Petite fiole", 20, "aha", 5, 1, 3)
Fiole = Class_jeu_1.Objet_mana("Fiole", 100, 'oho', 20, 2, 2)
image_perso1 = PhotoImage(file='défense.png')
image_mechant_humain = PhotoImage(file='défense.png')
epee = Class_jeu_1.Arme_physique("Epee", 1000, "wesh salut", 0, 2, "feu", 1, None, None, None)
epeebis = Class_jeu_1.Arme_magique("epeee", 2, 'a', 0, 2, 2, 'plante', 2, None, None, None)
arme_mag = Class_jeu_1.Arme_magique("arme mag", 50, 'aha', 0, 2, 2, "neutre", 1, None, None, None)
baton_mag = Class_jeu_1.Baton_magique('baton_mag', 50, 'oho', 0, 2, "neutre", 1, None, None,None)
casque = Class_jeu_1.Casque("casque", 20, 'aha', 0, 2, 2, 2, 2, 1)
casque2 = Class_jeu_1.Casque('casque2', 20, 'aha', 0, 2, 2, 2, 2, 1)
armure = Class_jeu_1.Armure('armure', 20, 'aah', 0, 2, 2, 2, 2, 1)
botte = Class_jeu_1.Botte('bottes', 20, 'oho', 0, 2, 2, 2, 2, 1, 3)
Repousse = Class_jeu_1.Utilitaire("Repousse", 50, 'aha', 2, 4, ('Repousse', 100))
liste_monstre = ['M1', 'M2', 'M3', 'M4']
liste_arme_phys_bis = [epee]
liste_arme_mag_bis = [epeebis, arme_mag]
liste_bat_mag_bis = [baton_mag]
liste_casque_bis = [casque, casque2]
liste_armures_bis = [armure]
liste_bottes_bis = [botte]
liste_soins_objets = [Potion, Super_potion]
liste_mana_objet = [Petite_fiole, Fiole]
liste_utilitaire_objet = [Repousse]
liste_magasin = [[Potion, Super_potion], [Petite_fiole, Fiole], [Repousse]]
Perso1.get_arme(epee)
Perso1.get_casque(casque)
Mechant_humain.get_arme(epeebis)
repousse_var = (0, 0)


# Création carte du jeu


canvas_carte1 = Canvas(fenetre, width=750, height=600, bg='ivory')
coords = (int(Perso1.coord[0]), int(Perso1.coord[1]))
obstacle = canvas_carte1.create_rectangle(300, 0, 750, 200, fill='red', width=0)
obstacle12 = canvas_carte1.create_rectangle(0, 370, 300, 600, fill='red', width=0)
obstacle13 = canvas_carte1.create_rectangle(300, 550, 750, 600, fill='red', width=0)
obstacle14 = canvas_carte1.create_rectangle(0, 0, 300, 50, fill='red', width=0)
obstacle15 = canvas_carte1.create_rectangle(0, 50, 50, 370, fill='red', width=0)
hautes_herbes1 = canvas_carte1.create_rectangle(300, 370, 600, 550, fill='green', width=0)
rectangle1 = canvas_carte1.create_rectangle(10, 10, 60, 60, fill='pink')
capteur_de_position_12 = canvas_carte1.create_rectangle(700, 200, 750, 550, fill='light blue', width=0)
compteur_htes_herbes = 0
canvas_carte2 = Canvas(fenetre, width=750, height=600, bg='ivory')
rectangle2 = canvas_carte2.create_rectangle(0, 0, 50, 50, fill='pink')
pnj2 = canvas_carte2.create_rectangle(290, 460, 340, 510, fill='brown')
hautes_herbes2 = canvas_carte2.create_rectangle(450, 150, 670, 550, fill='green', width=0)
obstacle2 = canvas_carte2.create_rectangle(0, 0, 100, 200, fill='red', width=0)
obstacle21 = canvas_carte2.create_rectangle(670, 150, 750, 550, fill='red', width=0)
obstacle22 = canvas_carte2.create_rectangle(450, 550, 750, 600, fill='red', width=0)
obstacle23 = canvas_carte2.create_rectangle(0, 0, 300, 150, fill='red', width=0)
obstacle24 = canvas_carte2.create_rectangle(450, 0, 750, 150, fill='red', width=0)
obstacle25 = canvas_carte2.create_rectangle(0, 550, 450, 600, fill='red', width=0)
capteur_de_position_21 = canvas_carte2.create_rectangle(0, 200, 50, 550, fill='light blue', width=0)
capteur_de_position_23 = canvas_carte2.create_rectangle(300, 0, 450, 50, fill='light blue', width=0)
canvas_carte2.tag_raise(hautes_herbes2)
canvas_carte3 = Canvas(fenetre, width=750, height=600, bg='ivory')
obstacle3 = canvas_carte3.create_rectangle(0, 550, 300, 600, fill='red', width=0)
obstacle31 = canvas_carte3.create_rectangle(0, 0, 50, 600, fill='red', width=0)
obstacle32 = canvas_carte3.create_rectangle(0, 0, 750, 50, fill='red', width=0)
obstacle33 = canvas_carte3.create_rectangle(700, 0, 750, 600, fill='red', width=0)
obstacle34 = canvas_carte3.create_rectangle(450, 550, 750, 600, fill='red', width=0)
capteur_de_position_32 = canvas_carte3.create_rectangle(300, 550, 450, 600, fill='light blue', width=0)
magasin3 = canvas_carte3.create_rectangle(120, 120, 300, 240, fill='blue', width=0)
campement3 = canvas_carte3.create_rectangle(500, 200, 650, 350, fill='light green', width=0)
rectangle3 = canvas_carte3.create_rectangle(0, 0, 50, 50, fill='pink')
liste_canvas_obstacles_herbes_capteurs = [[canvas_carte1, [obstacle, obstacle12, obstacle13, obstacle14, obstacle15], [hautes_herbes1], [(capteur_de_position_12, 2)], rectangle1, [], [], []],
                                          [canvas_carte2, [obstacle2, obstacle21, obstacle22, obstacle23, obstacle24, obstacle25, pnj2], [hautes_herbes2], [(capteur_de_position_21, 1), (capteur_de_position_23, 3)], rectangle2, [], [(pnj2, 1)],[]],
                                          [canvas_carte3, [obstacle3, obstacle31, obstacle32, obstacle33, obstacle34, magasin3, campement3], [], [(capteur_de_position_32, 2)], rectangle3, [magasin3], [], [campement3]]
                                          ]
liste_route = [['Route 1', 1, 2], ['Route 2', 3]]
vartext = StringVar()
liste_capteurs = liste_capteurss()
label_narration_carte = Label(fenetre, textvar=vartext, anchor=CENTER, bg='white', height=2, bd=2, relief=GROOVE, width=60, font=('Calibri', 15))
label_narration_carte.pack()
affiche_canvas_carte().tag_raise(liste_canvas_obstacles_herbes_capteurs[affiche_reste_carte()][4])
affiche_canvas_carte().focus_set()
affiche_canvas_carte().bind('<KeyPress>', clavierbis)
affiche_canvas_carte().bind('<KeyPress>', key_pressed)

affiche_canvas_carte().bind('<KeyRelease>', clavierbis)
affiche_canvas_carte().pack()
affiche_canvas_carte().coords(liste_canvas_obstacles_herbes_capteurs[affiche_reste_carte()][4], coords[0], coords[1], coords[0] + 50, coords[1] + 50)
changement_route()


# Création du menu


menu = Canvas(fenetre, width=350, height=320, bg='white', bd=1, relief=GROOVE)
bouton_sac_carte = menu.create_rectangle(10, 10, 346, 101, fill='red')
menu.create_text(177, 50, text='Sac', font=('Calibri', 20))
bouton_choix_menu = menu.create_rectangle(8, 8, 347, 102, fill='', outline='blue', width=3)
bouton_resume = menu.create_rectangle(10, 103, 346, 192, fill='red')
menu.create_text(177, 143, text='Personnage', font=('Calibri', 20))
bouton_save = menu.create_rectangle(10, 194, 346, 285, fill='red')
menu.create_text(177, 234, text='Sauvegarder', font=('Calibri', 20))
frame_menu_carte_bouton = Frame(fenetre, bg='ivory', bd=1, relief=FLAT)
frame_menu_liste_carte = Frame(fenetre, bg='ivory', bd=1, relief=FLAT)
frame_menu_back_carte = Frame(fenetre, bg='ivory', bd=1, relief=FLAT)
bouton_menu_soins_carte = Button(frame_menu_carte_bouton, bg='light grey', bd=1, fg='green', font=('Calibri', 20), width=10, text='Soins', command=lambda: menu_to_soins())
bouton_menu_manas_carte = Button(frame_menu_carte_bouton, bg='light grey', bd=1, fg='blue', font=('Calibri', 20), width=10, text='Mana', command=lambda: menu_to_mana())
bouton_menu_utilitaires_carte = Button(frame_menu_carte_bouton, bg='light grey', bd=1, font=('Calibri', 20), width=10, text='Objets', command=lambda: menu_to_utilitaires())
bouton_menu_objetrares_carte = Button(frame_menu_carte_bouton, bg='light grey', bd=1, font=('Calibri', 20), width=10, text='Objets rares', command=lambda: menu_to_objetsrares())
bouton_retour_menu_carte = Button(frame_menu_back_carte, bg='light grey', bd=1, font=('Calibri', 20), width=10, text='Back', command=lambda: back_menu_carte())
bouton_menu_soins_carte.grid(row=0, column=0, padx=5)
bouton_menu_manas_carte.grid(row=0, column=1, padx=5)
bouton_menu_utilitaires_carte.grid(row=0, column=2, padx=5)
bouton_menu_objetrares_carte.grid(row=0, column=3, padx=5)
bouton_retour_menu_carte.grid()
liste_menu_soins_carte = Listbox(frame_menu_liste_carte, bg='ivory', bd=2, relief=SUNKEN, selectmode=BROWSE, height=7, font=('Calibri', 25), fg='green', activestyle='dotbox', selectforeground='black', highlightcolor='light grey', selectbackground='light pink', width=31)
liste_menu_mana_carte = Listbox(frame_menu_liste_carte, bg='ivory', bd=2, relief=SUNKEN, selectmode=BROWSE, height=7, font=('Calibri', 25), fg='blue', activestyle='dotbox', selectforeground='black', highlightcolor='light grey', selectbackground='light pink', width=31)
liste_menu_utilitaires_carte = Listbox(frame_menu_liste_carte, bg='ivory', bd=2, relief=SUNKEN, selectmode=BROWSE, height=7, font=('Calibri', 25), fg='black', activestyle='dotbox', selectforeground='black', highlightcolor='light grey', selectbackground='light pink', width=31)
liste_menu_objetrares_carte = Listbox(frame_menu_liste_carte, bg='ivory', bd=2, relief=SUNKEN, selectmode=BROWSE, height=7, font=('Calibri', 25), fg='black', activestyle='dotbox', selectforeground='black', highlightcolor='light grey', selectbackground='light pink', width=31)
liste_menu_soins_carte.pack()
frame_menu_equipement_carte = Frame(fenetre, bd=1, bg='ivory', relief=FLAT)
frame_menu_stats_carte_equipement = Frame(frame_menu_equipement_carte, bd=1, bg='ivory', relief=FLAT)
frame_menu_changer_equipement = Frame(frame_menu_equipement_carte, bd=1, bg='ivory', relief=FLAT)
frame_menu_stats_carte_equipement.grid(row=0, column=0)
frame_menu_changer_equipement.grid(row=0, column=1)
Canva_perso = Canvas(frame_menu_stats_carte_equipement, bg='light grey', bd=1, relief=SUNKEN, width=500, height=400)
Canva_perso.create_rectangle(0, 0, 510, 70, fill='light blue', width=0)
dev_nom_perso = Canva_perso.create_text(20, 35, text=str(Perso1.nom), font=('Calibri', 20), anchor='w')
Canva_perso.create_rectangle(330, 70, 510, 410, fill='light green', width=0)
dev_atk_perso = Canva_perso.create_text(350, 105, text='Atk : 10', font=('Calibri', 15), anchor='w')
dev_atkmag_perso = Canva_perso.create_text(350, 140, text='Atk mag : 7', font=('Calibri', 15), anchor='w')
dev_def_perso = Canva_perso.create_text(350, 175, text='Def : 7', font=('Calibri', 15), anchor='w')
dev_defmag_perso = Canva_perso.create_text(350, 210, text='Def mag : 9', font=('Calibri', 15), anchor='w')
dev_money_perso = Canva_perso.create_text(490, 35, text=str(Perso1.argent) + ' Po', font=('Calibri', 20), anchor='e')
dev_vie_perso = Canva_perso.create_text(240, 95, text='PV : ' + str(Perso1.vie) + '/' + str(Perso1.viemax), font=('Calibri', 13), anchor='w')
dev_mana_perso = Canva_perso.create_text(240, 115, text='PM : ' + str(Perso1.mana) + '/' + str(Perso1.manamax), font=('Calibri', 13), anchor='w')
dev_exp_perso = Canva_perso.create_text(200, 132, text=str(Perso1.exp) + '/' + str(Perso1.exprestante), font=('Calibri', 13), anchor='w')
barre_menu_vie_max = Canva_perso.create_rectangle(20, 90, 230, 100, fill='white')
barre_menu_vie = Canva_perso.create_rectangle(21, 91, 230, 100, fill='red', width=0)
barre_menu_mana_max = Canva_perso.create_rectangle(20, 110, 230, 120, fill='white')
barre_menu_mana = Canva_perso.create_rectangle(21, 111, 230, 120, fill='blue', width=0)
barre_menu_exp_max = Canva_perso.create_rectangle(20, 130, 190, 135, fill='white')
barre_menu_exp = Canva_perso.create_rectangle(21, 131, 190, 135, fill='blue', width=0)
Canva_perso.pack()
bouton_menu_casque_carte = Button(frame_menu_changer_equipement, text='Casques', bd=1, relief=GROOVE, bg='light grey', font=('Calibri', 20), width=13, command=lambda: menu_equipement_to_casques())
bouton_menu_armure_carte = Button(frame_menu_changer_equipement, text='Armures', bd=1, relief=GROOVE, bg='light grey', font=('Calibri', 20), width=13, command=lambda: menu_equipement_to_armures())
bouton_menu_botte_carte = Button(frame_menu_changer_equipement, text='Bottes', bd=1, relief=GROOVE, bg='light grey', font=('Calibri', 20), width=13, command=lambda: menu_equipement_to_bottes())
bouton_menu_arme_carte = Button(frame_menu_changer_equipement, text='Armes', bd=1, relief=GROOVE, bg='light grey', font=('Calibri', 20), width=13, command=lambda: bouton_menu_choix_to_arme())
bouton_equipement_back_to_menu_carte = Button(frame_menu_changer_equipement, text='Back', bd=1, relief=GROOVE, bg='light grey', font=('Calibri', 20), width=13, command=lambda: menu_back_to_equipement())
bouton_choix_back_to_equipement_carte = Button(frame_menu_changer_equipement, text='Back', bd=1, relief=GROOVE, bg='light grey', font=('Calibri', 20), width=13, command=lambda: choix_to_equipement())
bouton_menu_casque_carte.grid(row=0, column=0, pady=15)
bouton_menu_armure_carte.grid(row=1, column=0, pady=15)
bouton_menu_botte_carte.grid(row=2, column=0, pady=15)
bouton_menu_arme_carte.grid(row=3, column=0, pady=15)
bouton_equipement_back_to_menu_carte.grid(row=4, column=0, pady=15)
bouton_menu_arme_phys = Button(frame_menu_changer_equipement, text='Armes physiques', bd=1, relief=GROOVE, bg='light grey', font=('Calibri', 20), width=15, command=lambda: menu_arme_to_arme_phys())
bouton_menu_arme_mag = Button(frame_menu_changer_equipement, text='Armes magiques', bd=1, relief=GROOVE, bg='light grey', font=('Calibri', 20), width=15, command=lambda: menu_arme_to_arme_mag())
bouton_menu_batons_mag = Button(frame_menu_changer_equipement, text='Batons magiques', bd=1, relief=GROOVE, bg='light grey', font=('Calibri', 20), width=15, command=lambda: menu_arme_to_baton_mag())
bouton_menu_arme_to_equipement = Button(frame_menu_changer_equipement, text='Back', bd=1, relief=GROOVE, bg='light grey', font=('Calibri', 20), width=13, command=lambda: menu_arme_to_equipement())
bouton_menu_arme_to_choix_arme = Button(frame_menu_changer_equipement, text='Back', bd=1, relief=GROOVE, bg='light grey', font=('Calibri', 20), width=13)
liste_menu_arme_phys = Listbox(frame_menu_changer_equipement, bg='ivory', bd=1, relief=SUNKEN, selectmode=BROWSE, height=7, font=('Calibri', 25), fg='black', activestyle='dotbox', selectforeground='black', highlightcolor='light grey', selectbackground='light pink', width=20)
liste_menu_arme_mag = Listbox(frame_menu_changer_equipement, bg='ivory', bd=1, relief=SUNKEN, selectmode=BROWSE, height=7, font=('Calibri', 25), fg='black', activestyle='dotbox', selectforeground='black', highlightcolor='light grey', selectbackground='light pink', width=20)
liste_menu_bat_mag = Listbox(frame_menu_changer_equipement, bg='ivory', bd=1, relief=SUNKEN, selectmode=BROWSE, height=7, font=('Calibri', 25), fg='black', activestyle='dotbox', selectforeground='black', highlightcolor='light grey', selectbackground='light pink', width=20)
liste_menu_casque = Listbox(frame_menu_changer_equipement, bg='ivory', bd=1, relief=SUNKEN, selectmode=BROWSE, height=7, font=('Calibri', 25), fg='black', activestyle='dotbox', selectforeground='black', highlightcolor='light grey', selectbackground='light pink', width=20)
liste_menu_armure = Listbox(frame_menu_changer_equipement, bg='ivory', bd=1, relief=SUNKEN, selectmode=BROWSE, height=7, font=('Calibri', 25), fg='black', activestyle='dotbox', selectforeground='black', highlightcolor='light grey', selectbackground='light pink', width=20)
liste_menu_botte = Listbox(frame_menu_changer_equipement, bg='ivory', bd=1, relief=SUNKEN, selectmode=BROWSE, height=7, font=('Calibri', 25), fg='black', activestyle='dotbox', selectforeground='black', highlightcolor='light grey', selectbackground='light pink', width=20)


# Création du magasin


magasin_menu = Canvas(fenetre, width=350, height=320, bg='ivory', bd=1, relief=GROOVE)
magasin_menu.create_rectangle(10, 10, 346, 101, fill='red')
magasin_menu.create_text(177, 50, text='Magasin', font=('Calibri', 20))
bouton_choix_magasin = magasin_menu.create_rectangle(8, 8, 347, 102, fill='', outline='blue', width=3)
bouton_vendre = magasin_menu.create_rectangle(10, 103, 346, 192, fill='red')
magasin_menu.create_text(177, 143, text='Vendre', font=('Calibri', 20))
bouton_back_magasin = magasin_menu.create_rectangle(10, 194, 346, 285, fill='red')
magasin_menu.create_text(177, 234, text='Quitter', font=('Calibri', 20))
frame_magasin = Frame(fenetre, bd=1, relief=SUNKEN, bg='ivory')
liste_soins_magasin = Listbox(frame_magasin, relief=SUNKEN, bd=1, bg='ivory', width=60, font=('Calibri', 20), height=7, activestyle='dotbox', selectforeground='black', highlightcolor='light grey', selectbackground='light pink', fg='green')
liste_mana_magasin = Listbox(frame_magasin, relief=SUNKEN, bd=1, bg='ivory', width=60, font=('Calibri', 20), height=7, activestyle='dotbox', selectforeground='black', highlightcolor='light grey', selectbackground='light pink', fg='blue')
liste_objet_magasin = Listbox(frame_magasin, relief=SUNKEN, bd=1, bg='ivory', width=60, font=('Calibri', 20), height=7, activestyle='dotbox', selectforeground='black', highlightcolor='light grey', selectbackground='light pink')
frame_bouton_magasin = Frame(frame_magasin, bg='ivory', bd=1, relief=SUNKEN)
bouton_magasin_soin = Button(frame_bouton_magasin, relief=GROOVE, bd=1, bg='light grey', font=('Calibri', 25), text='Soins', width=15, fg='green', command=lambda: bouton_magasin_soins())
bouton_magasin_manas = Button(frame_bouton_magasin, relief=GROOVE, bd=1, bg='light grey', font=('Calibri', 25), text='Mana', width=15, fg='blue', command=lambda: bouton_magasin_mana())
bouton_magasin_objets = Button(frame_bouton_magasin, relief=GROOVE, bd=1, bg='light grey', font=('Calibri', 25), text='Objets', width=15, fg='black', command=lambda: bouton_magasin_objet())
bouton_magasin_soin.grid(row=0, column=0, padx=5)
bouton_magasin_manas.grid(row=0, column=1, padx=5)
bouton_magasin_objets.grid(row=0, column=2, padx=5)
frame_bouton_magasin.grid(row=0, column=0)
liste_soins_magasin.grid(row=1, column=0)
frame_texte_magasin = Frame(frame_magasin, bg='ivory', bd=1, relief=SUNKEN)
texte_magasin_money = Label(frame_texte_magasin, text= 'Vous avez ' + str(Perso1.argent) + ' Po', anchor=CENTER, bg='white', height=2, bd=2, relief=GROOVE, width=60, font=('Calibri', 15))
texte_magasin_money.grid(row=2, column=0)
frame_texte_magasin.grid(row=2, column=0)
frame_texte_money_vendre = Frame(fenetre, bg='ivory', bd=1, relief=SUNKEN)
texte_money_vendre = Label(frame_texte_money_vendre, text='Vous avez ' + str(Perso1.argent) + ' Po', anchor=CENTER, bg='white', height=2, bd=2, relief=GROOVE, width=53, font=('Calibri', 15))
texte_money_vendre.pack()


### Système de combat


canva_combat = Canvas(fenetre, bg='light grey')
canva_combat.pack(anchor=CENTER)
canva_combat.config(height=340, width=600)
frame_menu_combat = Frame(fenetre, bd=1, relief=FLAT)
frame_menu_combat.pack()
frame_menu_combat.config(height=320)
bouton_sac = Button(frame_menu_combat, text='Sac', relief=RIDGE, bd=1, bg='light grey', font=('Calibri', 18), width=13, height=2, command=lambda: sac_combat())
bouton_equipement = Button(frame_menu_combat, text='Equipement', relief=RIDGE, bd=1, bg='light grey', font=('Calibri', 18), width=13, height=2, command=lambda: equipement_combat())
bouton_attaque = Button(frame_menu_combat, text='Attaquer', relief=RIDGE, bd=1, bg='light grey', font=('Calibri', 18), width=13, height=2, command=lambda: attaque_combat())
bouton_fuite = Button(frame_menu_combat, text='Fuite', relief=RIDGE, bd=1, bg='light grey', font=('Calibri', 18), width=13, height=2, command=lambda: fuite_combat())
vartext_combat = StringVar()
vartext_combat.set('')
texte_frame_menu_combat = Label(frame_menu_combat, textvar=vartext_combat, anchor=CENTER, bg='white', height=2, bd=2, relief=GROOVE, width=60, font=('Calibri', 15))
texte_frame_menu_combat.grid(row=0, column=1)
bouton_attaque.grid(row=1, column=1)
bouton_sac.grid(row=2, column=0)
bouton_equipement.grid(row=2, column=2)
bouton_fuite.grid(row=3, column=1)
frame_sac = Frame(fenetre, relief=FLAT, bd=1)
frame_sac.config(height=200, width=500)
bouton_sac_soins = Button(frame_sac, text="Soins", bd=1, relief=GROOVE, bg='light green', font=('Calibri', 20), width=11, height=2, command=lambda: sac_soin_combat())
bouton_sac_mana = Button(frame_sac, text="Mana", bd=1, relief=GROOVE, bg="light blue", font=('Calibri', 20), width=11, height=2, command=lambda: sac_mana_combat())
bouton_back_sac = Button(frame_sac, text='Back', bd=1, relief=GROOVE, bg='light grey', font=('Calibri', 20), width=11, height=2,  command=lambda: sac_combat())
vartext_combat_sac = StringVar()
texte_frame_menu_sac_combat = Label(frame_sac, textvar=vartext_combat_sac, anchor=CENTER, bg='white', height=2, bd=2, relief=GROOVE, width=50, font=('Calibri', 15))
texte_frame_menu_sac_combat.grid(row=0, column=1)
bouton_sac_soins.grid(row=1, column=0)
bouton_sac_mana.grid(row=1, column=2)
bouton_back_sac.grid(row=3, column=1)
frame_sac_soin = Frame(fenetre, bd=1, bg='light green', relief=FLAT)
frame_sac_soin.config(height=350, width=500)
bouton_back_sac_soin = Button(frame_sac_soin, bd=1, text='Back', relief=SUNKEN, bg='light grey', font=('Calibri', 15), width=10, height=2, command=lambda: sac_soin_combat())
bouton_back_sac_soin.pack(side=BOTTOM)
frame_sac_mana = Button(fenetre, relief=FLAT, bg='light blue', bd=1)
frame_sac_mana.config(height=350, width=500)
bouton_back_sac_mana = Button(frame_sac_mana, bd=1, text='Back', relief=SUNKEN, bg='light grey', font=('Calibri', 15), width=10, height=2, command=lambda: sac_mana_combat())
bouton_back_sac_mana.pack(side=BOTTOM)
frame_equipement_combat = Frame(fenetre, bg='ivory', bd=1, relief=FLAT, height=120)
frame_texte_equipement_combat = Frame(frame_equipement_combat, bg='ivory', bd=1, relief=FLAT)
frame_reste_equipement_combat = Frame(frame_equipement_combat, bg='ivory', bd=1, relief=FLAT)
texte_frame_menu_equipement_combat = Label(frame_texte_equipement_combat, textvar=vartext_combat_sac, anchor=CENTER, bg='white', height=2, bd=2, relief=GROOVE, width=50, font=('Calibri', 15))
texte_frame_menu_equipement_combat.grid()
frame_equipement_combat_bouton = Frame(frame_reste_equipement_combat, bd=2, relief=FLAT, height=120)
bouton_equipement_casque_combat = Button(frame_equipement_combat_bouton, relief=GROOVE, bd=1, bg='light grey', text='Casques', font=('Calibri', 20), width=10, command=lambda: equipement_casque_combat())
bouton_equipement_armure_combat = Button(frame_equipement_combat_bouton, relief=GROOVE, bd=1, bg='light grey', text='Armures', font=('Calibri', 20), width=10, command=lambda: equipement_armure_combat())
bouton_equipement_botte_combat = Button(frame_equipement_combat_bouton, relief=GROOVE, bd=1, bg='light grey', text='Bottes', font=('Calibri', 20), width=10, command=lambda: equipement_botte_combat())
frame_equipement_combat_personnage = Frame(frame_reste_equipement_combat, bg='', bd=2, relief=FLAT, height=120)
frame_equipement_arme_combat = Frame(frame_reste_equipement_combat, bd=2, relief=FLAT, height=120)
bouton_equipement_arme_combat = Button(frame_equipement_arme_combat, relief=GROOVE, bg='light grey', text='Arme', font=('Calibri', 20), width=10, command=lambda: equipement_arme_combat())
bouton_back_arme_to_equipement = Button(frame_equipement_arme_combat, relief=GROOVE, bg='light grey', text='Back', font=('Calibri', 20), width=10, command=lambda: equipement_arme_combat())
frame_texte_equipement_combat.grid()
frame_reste_equipement_combat.grid()
bouton_equipement_arme_combat.grid(column=0)
frame_equipement_arme_combat.grid(row=0, column=1)
frame_equipement_combat_bouton.grid(row=1, column=1, pady=20)
frame_equipement_combat_personnage.grid(row=2, column=1)
bouton_equipement_casque_combat.grid(row=0, column=0)
bouton_equipement_armure_combat.grid(row=0, column=1, padx=20)
bouton_equipement_botte_combat.grid(row=0, column=2)
liste_arme_physique_combat = Listbox(frame_equipement_arme_combat, relief=FLAT, bd=1, activestyle='dotbox', selectforeground='black', bg='ivory', selectmode=BROWSE, height=5, font=('Calibri', 20), fg='blue', highlightcolor='light grey', selectbackground='light pink')
liste_arme_magique_combat = Listbox(frame_equipement_arme_combat, relief=FLAT, bd=1, activestyle='dotbox', selectforeground='black', bg='ivory', selectmode=BROWSE, height=5, font=('Calibri', 20), fg='blue', highlightcolor='light grey', selectbackground='light pink')
liste_baton_magique_combat = Listbox(frame_equipement_arme_combat, relief=FLAT, bd=1, activestyle='dotbox', selectforeground='black', bg='ivory', selectmode=BROWSE, height=5, font=('Calibri', 20), fg='blue', highlightcolor='light grey', selectbackground='light pink')
liste_casque_combat = Listbox(frame_equipement_combat_bouton, relief=FLAT, bd=1, activestyle='dotbox', selectforeground='black', bg='ivory', selectmode=BROWSE, height=5, font=('Calibri', 20), fg='blue', highlightcolor='light grey', selectbackground='light pink')
liste_armure_combat = Listbox(frame_equipement_combat_bouton, relief=FLAT, bd=1, activestyle='dotbox', selectforeground='black', bg='ivory', selectmode=BROWSE, height=5, font=('Calibri', 20), fg='blue', highlightcolor='light grey', selectbackground='light pink')
liste_botte_combat = Listbox(frame_equipement_combat_bouton, relief=FLAT, bd=1, activestyle='dotbox', selectforeground='black', bg='ivory', selectmode=BROWSE, height=5, font=('Calibri', 20), fg='blue', highlightcolor='light grey', selectbackground='light pink')
liste_soins_combat = Listbox(frame_sac_soin, relief=FLAT, bd=1, activestyle='dotbox', selectforeground='black', bg='ivory', selectmode=BROWSE, height=4, font=('Calibri', 25), fg='blue', highlightcolor='light grey', selectbackground='light pink', width=25)
vartexte_soin_combat = StringVar()
vartexte_soin_combat.set('Quel objet voulez-vous utiliser ?')
label_texte_soin_combat = Label(frame_sac_soin, bd=1, relief=GROOVE, font=('Calibri', 15), height=2, width=42, bg='white', anchor=CENTER, textvar=vartexte_soin_combat)
label_texte_soin_combat.pack(side=TOP)
liste_soins_combat.pack()
vartexte_mana_combat = StringVar()
vartexte_mana_combat.set('Quel mana voulez-vous utiliser ?')
label_texte_mana_combat = Label(frame_sac_mana, bd=1, relief=GROOVE, font=('Calibri', 15), height=2, width=42, bg='white', anchor=CENTER, textvar=vartexte_mana_combat)
label_texte_mana_combat.pack(side=TOP)
liste_mana_combat = Listbox(frame_sac_mana, relief=FLAT, bd=1, activestyle='dotbox', selectforeground='black', bg='ivory', selectmode=BROWSE, height=4, font=('Calibri', 25), fg='blue', highlightcolor='light grey', selectbackground='light pink', width=25)
liste_mana_combat.pack()
bouton_back_equipement = Button(frame_reste_equipement_combat, text='Back', font=('Calibri', 20), bd=1, relief=SUNKEN, width=10, command=lambda:retour_equipement_choix_bouton_combat())
bouton_back_equipement_to_menu = Button(frame_equipement_combat_personnage, relief=SUNKEN, bd=1, bg='light grey', font=('Calibri', 20), width=8, text='Back', command=lambda: equipement_combat())
bouton_back_equipement_to_menu.pack(side=BOTTOM)
frame_attaque_combat = Frame(fenetre, relief=FLAT, bd=1, bg='ivory')
bouton_attaque_basique = Button(frame_attaque_combat, text='Attaque', font=('Calibri', 25), bd=1, relief=GROOVE, bg='light grey', height=2, width=16, command=lambda : combat_test(1, Mechant_humain))
bouton_attaque_spe_1 = Button(frame_attaque_combat, text='Atk spé 1', font=('Calibri', 18), bd=1, relief=GROOVE, bg='light grey', width=10, height=2)
bouton_attaque_spe_2 = Button(frame_attaque_combat, text='Atk spé 2', font=('Calibri', 18), bd=1, relief=GROOVE, bg='light grey', width=10, height=2)
bouton_attaque_spe_3 = Button(frame_attaque_combat, text='Atk spé 3', font=('Calibri', 18), bd=1, relief=GROOVE, bg='light grey', width=10, height=2)
bouton_back_attaque_to_menu = Button(frame_attaque_combat, text=' Back ', bd=1, relief=GROOVE, bg='light grey', font=('Calibri', 18), width=10, command=lambda: attaque_combat())
bouton_attaque_basique.grid(row=1, column=1, pady=9)
bouton_attaque_spe_1.grid(row=2, column=0, padx=10, pady=9)
bouton_attaque_spe_2.grid(row=2, column=1, padx=10, pady=9)
bouton_attaque_spe_3.grid(row=2, column=2, padx=10, pady=9)
bouton_back_attaque_to_menu.grid(row=4, column=1, pady=9)
canva_combat.create_image(90, 180, anchor='nw', image=image_perso1)
canva_combat.create_image(410, 20, anchor='nw', image=image_mechant_humain)
canva_combat.create_rectangle(50, 90, 300, 165, fill='dark grey', width=0)
barre_de_vie_max = canva_combat.create_rectangle(80, 120, 200, 130, fill='white')
barre_de_vie = canva_combat.create_rectangle(81, 121, 200, 130, fill='red', width=0)
barre_de_mana_max = canva_combat.create_rectangle(80, 135, 200, 145, fill='white')
barre_de_mana = canva_combat.create_rectangle(81, 136, 200, 145, fill='blue', width=0)
barre_dexp_max = canva_combat.create_rectangle(80, 150, 180, 155, fill='white')
barre_dexp = canva_combat.create_rectangle(81, 151, 180, 155, fill='blue', width=0)
canva_combat.create_rectangle(390, 165, 550, 205, fill='dark grey', width=0)
barre_de_vie_mechant_max = canva_combat.create_rectangle(400, 180, 520, 190, fill='white')
barre_de_vie_mechant = canva_combat.create_rectangle(401, 181, 520, 190, fill='red', width=0)
niveau_mechant_combat = canva_combat.create_text(530, 185, text=str(Mechant_humain.niveau), font=('Calibri', 13), anchor='w')
dev_niveau_perso_combat = canva_combat.create_text(85, 105, text=str(Perso1.nom) + '  niv: ' + str(Perso1.niveau), anchor='w', font=('Calibri', 13))
dev_nombre_de_pts_de_vie_main_perso = canva_combat.create_text(205, 124, text=str(Perso1.vie) + '/' + str(Perso1.viemax), font=('Calibri', 12), anchor='w')
dev_nombre_de_pts_de_mana_main_perso = canva_combat.create_text(205, 139, text='PM : ' + str(Perso1.mana) + '/' + str(Perso1.manamax), font=('Calibri', 12), anchor='w')
barre_dexp_main_perso()


# initialisation combat


sac_liste = recherche_sac()
equipement_liste = recherche_equipement_bis()
init_sac_soins()
init_sac_mana()
init_bis_equip()
init_sac_utilitaires()
init_sac_objetrares()
init_magasin()
dev_update()
change_casque(casque)
change_arme(baton_mag)
liste_menu_objetrares_carte.insert(4, "Petite clef")
# liste_menu_objetrares_carte.insert(5, "Carte")


fenetre.mainloop()
