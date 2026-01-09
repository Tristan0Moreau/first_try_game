import random


class Objet_soin:
    def __init__(self, nom, prix, description, soin, rarete, quantite):
        self.nom = nom
        self.prix = prix
        self.description = description
        self.soin = soin
        self.rarete = rarete
        self.quantite = quantite


class Main_perso:
    def __init__(self, nom, argent, vie, exp, niveau, exprestante, viemax, attaque_physique, defense_physique, mana,
                 manamax, regeneration_mana, critique, defense_magique, attaque_magique, type, etat, capacite1,
                 capacite2, capacite3, capacite4, capacite5, capacite6, position, coord):
        self.nom = nom
        self.argent = argent
        self.vie = vie
        self.exp = exp
        self.niveau = niveau
        self.exprestante = exprestante
        self.viemax = viemax
        self.attaque_physique = attaque_physique
        self.defense_physique = defense_physique
        self.mana = mana
        self.manamax = manamax
        self.regeneration_mana = regeneration_mana
        self.critique = critique
        self.defense_magique = defense_magique
        self.attaque_magique = attaque_magique
        self.armure = None
        self.botte = None
        self.casque = None
        self.arme = None
        self.baton_magie = None
        self.type = type
        self.etat = etat
        self.capacite1 = capacite1
        self.capacite2 = capacite2
        self.capacite3 = capacite3
        self.capacite4 = capacite4
        self.capacite5 = capacite5
        self.capacite6 = capacite6
        self.position = position
        self.coord = coord

    def attaque_magique_cible(self, cible):
        degats = self.attaque_magique
        if self.arme is not None:
            degats *= self.arme.attaque_magique
        if self.casque is not None:
            degats *= self.casque.attaque_magique
        if self.armure is not None:
            degats *= self.armure.attaque_magique
        if self.botte is not None:
            degats *= self.botte.attaque_magique
        degats *= type_calculeur(self.type, cible.type)
        degats = int(degats)
        degats /= cible.defense_magique
        if cible.armure is not None:
            degats /= cible.armure.defense_magique
        if cible.casque is not None:
            degats /= cible.casque.defense_magique
        if cible.botte is not None:
            degats /= cible.botte.defense_magique
        if degats <= 0:
            degats += 1 - degats
        chance = random.randint(0, 16)
        if chance == 5 and self.critique > 1:
            degats *= self.critique
        degats = int(degats)
        cible.take_damage(degats)

    def attaque_physique_cible(self, cible):
        degats = self.attaque_physique
        if self.arme is not None:
            degats *= self.arme.attaque_physique
        if self.casque is not None:
            degats *= self.casque.attaque_physique
        if self.armure is not None:
            degats *= self.armure.attaque_physique
        if self.botte is not None:
            degats *= self.botte.attaque_physique
        degats *= type_calculeur(self.type, cible.type)
        degats = int(degats)
        degats /= cible.defense_physique
        if cible.armure is not None:
            degats /= cible.armure.defense_physique
        if cible.casque is not None:
            degats /= cible.casque.defense_physique
        if cible.botte is not None:
            degats /= cible.botte.defense_physique
        if degats <= 0:
            degats += 1 - degats
        chance = random.randint(0, 16)
        if chance == 5 and self.critique > 1:
            degats *= self.critique
        degats = int(degats)
        cible.take_damage(degats)

    def take_damage(self, damages):
        self.vie -= damages

    def win_exp(self, exp):
        self.exp += exp
        if self.exp >= self.exprestante:
            self.niveau += 1
            self.exp = 0
            self.exprestante = int(0.919 + 2.4*self.niveau + 2.4 * (self.niveau**2))

    def soin_objet(self, objet):
        self.vie += objet.soin
        if self.vie > self.viemax:
            self.vie = self.viemax

    def mana_objet(self, objet):
        self.mana += objet.mana
        if self.mana > self.manamax:
            self.mana = self.manamax

    def get_casque(self, casque):
        self.casque = casque

    def get_armure(self, armure):
        self.armure = armure

    def get_botte(self, botte):
        self.botte = botte

    def change_type(self):
        self.type = (self.type[0], self.arme.type)

    def get_argent(self, argent):
        self.argent += argent

    def get_arme(self, arme):
        self.arme = arme
        self.change_type()

class Capacite:
    def __init__(self, nom, description, type, effet, prix_mana, prix, degats_physique, degats_magique):
        self.nom = nom
        self.description = description
        self.type = type
        self.effet = effet
        self.prix_mana = prix_mana
        self.prix = prix
        self.degats_physique = degats_physique
        self.degats_magique = degats_magique


class Objet_mana:
    def __init__(self, nom, prix, description, mana, rarete, quantite):
        self.nom = nom
        self.prix = prix
        self.description = description
        self.mana = mana
        self.rarete = rarete
        self.quantite = quantite


class Arme_physique:
    def __init__(self, nom, prix, description, niveau, attaque_physique, type, rarete, capacite1, capacite2, capacite3):
        self.nom = nom
        self.prix = prix
        self.description = description
        self.niveau = niveau
        self.rarete = rarete
        self.attaque_physique = attaque_physique
        self.type = type
        self.attaque_magique = 0
        self.capacite1 = capacite1
        self.capacite2 = capacite2
        self.capacite3 = capacite3


class Arme_magique:
    def __init__(self, nom, prix, description, niveau, attaque_physique, attaque_magique, type, rarete, capacite1, capacite2, capacite3):
        self.nom = nom
        self.prix = prix
        self.description = description
        self.niveau = niveau
        self.rarete = rarete
        self.attaque_physique = attaque_physique
        self.type = type
        self.attaque_magique = attaque_magique
        self.capacite1 = capacite1
        self.capacite2 = capacite2
        self.capacite3 = capacite3


class Baton_magique:
    def __init__(self, nom, prix, description, niveau, attaque_magique, type, rarete, capacite1, capacite2, capacite3):
        self.nom = nom
        self.prix = prix
        self.description = description
        self.niveau = niveau
        self.rarete = rarete
        self.attaque_magique = attaque_magique
        self.type = type
        self.attaque_physique = 0
        self.capacite1 = capacite1
        self.capacite2 = capacite2
        self.capacite3 = capacite3


class Casque:
    def __init__(self, nom, prix, description, niveau, defense_physique, defense_magique, attaque_magique, attaque_physique, rarete):
        self.nom = nom
        self.prix = prix
        self.description = description
        self.niveau = niveau
        self.defense_physique = defense_physique
        self.defense_magique = defense_magique
        self.attaque_magique = attaque_magique
        self.attaque_physique = attaque_physique
        self.rarete = rarete


class Armure:
    def __init__(self, nom, prix, description, niveau, defense_physique, defense_magique, attaque_magique, attaque_physique, rarete):
        self.nom = nom
        self.prix = prix
        self.description = description
        self.niveau = niveau
        self.defense_physique = defense_physique
        self.defense_magique = defense_magique
        self.attaque_magique = attaque_magique
        self.attaque_physique = attaque_physique
        self.rarete = rarete


class Botte:
    def __init__(self, nom, prix, description, niveau, defense_physique, defense_magique, attaque_magique, attaque_physique, rarete, vitesse_marche):
        self.nom = nom
        self.prix = prix
        self.description = description
        self.niveau = niveau
        self.defense_physique = defense_physique
        self.defense_magique = defense_magique
        self.attaque_magique = attaque_magique
        self.attaque_physique = attaque_physique
        self.rarete = rarete
        self.vitesse_marche = vitesse_marche


class Utilitaire:
    def __init__(self, nom, prix, description, rarete, quantite, effet):
        self.nom = nom
        self.prix = prix
        self.description = description
        self.rarete = rarete
        self.quantite = quantite
        self.effet = effet


class Mechant:
    def __init__(self, nom, argent, vie, exp, niveau, viemax, attaque_physique, defense_physique, mana, manamax,
                 regeneration_mana, critique, defense_magique, attaque_magique, type, statut, etat):
        self.nom = nom
        self.argent = argent
        self.vie = vie
        self.exp = exp
        self.niveau = niveau
        self.viemax = viemax
        self.attaque_physique = attaque_physique
        self.defense_physique = defense_physique
        self.mana = mana
        self.manamax = manamax
        self.regeneration_mana = regeneration_mana
        self.critique = critique
        self.defense_magique = defense_magique
        self.attaque_magique = attaque_magique
        self.armure = None
        self.botte = None
        self.casque = None
        self.arme = None
        self.baton_magie = None
        self.type = type
        self.statut = statut
        self.etat = etat

    def attaque_magique_cible(self, cible):
        degats = self.attaque_magique
        if self.arme is not None:
            degats *= self.arme.attaque_magique
        if self.casque is not None:
            degats *= self.casque.attaque_magique
        if self.armure is not None:
            degats *= self.armure.attaque_magique
        if self.botte is not None:
            degats *= self.botte.attaque_magique
        degats *= type_calculeur(self.type, cible.type)
        degats = int(degats)
        degats /= cible.defense_magique
        if cible.armure is not None:
            degats /= cible.armure.defense_magique
        if cible.casque is not None:
            degats /= cible.casque.defense_magique
        if cible.botte is not None:
            degats /= cible.botte.defense_magique
        if degats <= 0:
            degats += 1 - degats
        chance = random.randint(0, 16)
        if chance == 5 and self.critique > 1:
            degats *= self.critique
        degats = int(degats)
        cible.take_damage(degats)

    def attaque_physique_cible(self, cible):
        degats = self.attaque_physique
        if self.arme is not None:
            degats *= self.arme.attaque_physique
        if self.casque is not None:
            degats *= self.casque.attaque_physique
        if self.armure is not None:
            degats *= self.armure.attaque_physique
        if self.botte is not None:
            degats *= self.botte.attaque_physique
        degats *= type_calculeur(self.type, cible.type)
        degats = int(degats)
        degats /= cible.defense_physique
        if cible.armure is not None:
            degats /= cible.armure.defense_physique
        if cible.casque is not None:
            degats /= cible.casque.defense_physique
        if cible.botte is not None:
            degats /= cible.botte.defense_physique
        if degats <= 0:
            degats += 1 - degats
        chance = random.randint(0, 16)
        if chance == 5 and self.critique > 1:
            degats *= self.critique
        degats = int(degats)
        cible.take_damage(degats)

    def take_damage(self, damages):
        self.vie -= damages

    def soin_objet(self, objet):
        self.vie += objet.soin
        if self.vie > self.viemax:
            self.vie = self.viemax

    def get_casque(self, casque):
        self.casque = casque

    def get_armure(self, armure):
        self.armure = armure

    def get_botte(self, botte):
        self.botte = botte

    def get_arme(self, arme):
        self.arme = arme
        self.change_type()

    def change_type(self):
        self.type = (self.type[0], self.arme.type)

    def mana_objet(self, objet):
        self.mana += objet.mana
        if self.mana > self.manamax:
            self.mana = self.manamax


def type_calculeur(J1, J2):
    Matrice_type = [['feu', 'glace', 'plante'], ['eau', 'feu', 'terre'], ['elec', 'vol', 'eau'],
                    ['plante', 'eau', 'glace'], ['terre', 'feu', 'elec'], ['vol', 'plante', 'terre'],
                    ['glace', 'vol', 'elec']]
    tuple_J1 = J1
    tuple_J2 = J2
    if tuple_J1 == ('neutre', 'neutre') or tuple_J2 == ('neutre', 'neutre'):
        return 1
    else:
        score = 1
        for types in tuple_J1:
            for listes in Matrice_type:
                if listes[0] == types:
                    if tuple_J2[0] in listes[1:3]:
                        score *= 2
                    if tuple_J2[1] in listes[1:3]:
                        score *= 2
        for types in tuple_J2:
            for listes in Matrice_type:
                if listes[0] == types:
                    if tuple_J1[0] in listes[1:3]:
                        score /= 2
                    if tuple_J1[1] in listes[1:3]:
                        score /= 2
    return score










#feu, glace, elec, eau, plante, terre, vol
#feu -> glace, plante
#eau -> feu, terre
#elec -> vol, eau
#plante -> eau, glace          #eau, glace, feu, plante, terre
#terre -> feu, elec
#vol -> plante, terre
#glace -> vol, elec
