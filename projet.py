import numpy as np
from math import *
import sys
import os
import re
import binascii


#Q1.1
class Cle128 :
    # Representation d'une cle 128 bits en 4 entiers non
    # signes de 32 bits
    def __init__(self,v1,v2,v3,v4):
        self.v1 = np.uint32(v1)
        self.v2 = np.uint32(v2)
        self.v3 = np.uint32(v3)
        self.v4 = np.uint32(v4)

    def __str__(self):
       return f"({self.v1}, {self.v2}, {self.v3}, {self.v4})"
    

#Q1.2
def inf(cle1,cle2):
    # Retourne True si cle1 est strictement inferieure a cle2
    if (cle1.v1 > cle2.v1) :
        return False
    elif (cle1.v1 < cle2.v1) :
        return True
    if (cle1.v2 > cle2.v2) :
        return False
    elif (cle1.v2 < cle2.v2) :
        return True
    if (cle1.v3 > cle2.v3) :
        return False
    elif (cle1.v3 < cle2.v3) :
        return True
    if (cle1.v4 > cle2.v4) :
        return False
    return False

#Q1.3
def eg(cle1,cle2) :
    # Retourne True si cle1 est egale a cle2
    return cle1.v1 == cle2.v1 and cle1.v2 == cle2.v2 and cle1.v3 == cle2.v3 and cle1.v4 == cle2.v4

#Q2.4

#structure Arbre Binaire
class Noeud:
    def __init__(self,cle):
        self.cle = cle
        self.nbNoeuds = 1
        self.parent = None
        self.gauche = None
        self.droite = None


class TasMinArbre :
    def __init__(self):
        self.racine = None

    def Ajout(self, cle):
        # Ajoute une cle au tas
        nouveau_noeud = Noeud(cle) # Creer le nouveau noeud a ajouter
        if not self.racine: # Si la racine est vide, ajouter le nouveau noeud a la racine
            self.racine = nouveau_noeud 
        else : # Sinon, ajouter le nouveau noeud a la fin de l'arbre
            self.AjoutRec(self.racine,nouveau_noeud) 


    def AjoutRec(self, noeud, nouveau_noeud):
        # Fonction recursive qui ajoute un nouveau noeud au tas a partir du
        # sous-arbre courant noeud, incremente le nombre de noeuds et reorganise
        # le tas en structure de tas min correcte

        if noeud.gauche is None : # si le noeud n'a pas de fils gauche
            noeud.gauche = nouveau_noeud # alors, ajouter le nouveau noeud a gauche
            nouveau_noeud.parent = noeud # ajouter le parent du nouveau noeud
        elif noeud.droite is None : # idem si le noeud n'a pas de fils droit
            noeud.droite = nouveau_noeud
            nouveau_noeud.parent = noeud
        
        else: # Sinon, noeud a un enfant gauche et droite, chercher de quel cote ajouter
            hauteur = floor(log(noeud.nbNoeuds,2)) # taille_noeud = 2^(hauteur+1) - 1
            taille_enfant_complet = (pow(2,hauteur) - 1) # (taille_noeud - racine)/2 pour un enfant

            # Si enfant gauche complet : verifier si droite est complet
            if noeud.gauche.nbNoeuds == taille_enfant_complet:

                # Si enfant droite complet : ajouter a gauche
                if noeud.droite.nbNoeuds == taille_enfant_complet:
                    self.AjoutRec(noeud.gauche, nouveau_noeud)
                else: # Sinon, enfant droite pas complet : ajouter a droite
                    self.AjoutRec(noeud.droite, nouveau_noeud)

            else: # Sinon, enfant gauche pas complet : ajouter a gauche
                self.AjoutRec(noeud.gauche, nouveau_noeud)

        noeud.nbNoeuds += 1 # Mise a jour du nombre de noeuds
        self.remonter(nouveau_noeud) # Reordonner le tas



    def AjoutsIteratifs(self,listeCles):
        # Ajoute une liste de cles au tas en appelant la fonction Ajout
        for cle in listeCles: # Pour chaque cle dans la liste de cles
            self.Ajout(cle)  # inserer la cle dans le tas et la remontee est faite automatiquement dans Ajout


    def remonter(self,noeud):
        # Reorganise le tas en structure de tas min correcte : remonte le noeud
        # tant qu'il est plus petit que son parent

        # Tant que le noeud n'est pas la racine et que le noeud est plus petit que son parent
        while noeud.parent is not None and inf(noeud.cle,noeud.parent.cle):
            noeud.parent.cle,noeud.cle = noeud.cle,noeud.parent.cle # echanger le parent et le noeud
            noeud = noeud.parent # Remonter d'un etage dans l'arbre



    def supprMin(self):
        # Supprime le minimum d'un tas min arbre (la racine du tas), arrange le tas en une structure
        # de tas min correcte et renvoie le minimum supprime.

        if self.racine is None: # Tas vide
            return None
        if self.racine.gauche is None and self.racine.droite is None: # Tas compose d'un unique noeud
            min = self.racine.cle  
            self.racine = None  
            return min # Retourner le min supprime (la racine)
        
        # Sinon, etape 1 : recuperer le dernier noeud du tas et le supprimer du tas
        dernier_noeud = self.supprDernierNoeud(self.racine)
        min = self.racine.cle
        self.racine.cle = dernier_noeud.cle # etape 2 : remplacer la racine par le dernier noeud

        # etape 3 : descendre le noeud pour respecter la structure de tas min (le noeud doit être
        # plus petit que ses fils)
        self.descente(self.racine) 
        return min



    def supprDernierNoeud(self, noeud):
        # Fonction recursive qui cherche le dernier noeud d'un tas (a partir du sous-arbre noeud),
        # le supprime du tas, met a jour le nombre de noeuds et retourne le dernier noeud.

        if noeud is None:
            return None
        
        # Si le noeud n'a pas de fils, le noeud est le dernier noeud du tas
        if noeud.gauche is None and noeud.droite is None:

            # Si le noeud a un parent : regarder quel fils de son parent il est pour le
            # supprimer du tas
            if noeud.parent:
                if noeud.parent.gauche == noeud: # si le noeud est le fils gauche de son parent
                    noeud.parent.gauche = None  # alors supprimer le fils gauche
                else:
                    noeud.parent.droite = None  # sinon noeud est le fils droit
            else: # Sinon, pas de parent : noeud est la racine
                self.racine = None
            return noeud
        
        # Sinon, noeud a au moins un fils non nul (gauche enfant unique ou gauche et droite)
        else :
            noeud.nbNoeuds -= 1 # decrementer pour le noeud a supprimer
            if noeud.droite is None: # pas d'enfant droit : supprimer a gauche
                return self.supprDernierNoeud(noeud.gauche)
            
            # Sinon, chercher si le dernier noeud est a gauche ou droite
            hauteur = floor(log(noeud.nbNoeuds,2)) # taille_tas = 2^(hauteur+1) - 1
            taille_enfant_complet = pow(2,hauteur) - 1 # (taille_tas - racine)/2 pour un enfant

            # Si enfant gauche complet : verifier si enfant droite complet
            if noeud.gauche.nbNoeuds == taille_enfant_complet:
                if noeud.droite.nbNoeuds == taille_enfant_complet: # enfant droite complet : dernier noeud a droite
                    return self.supprDernierNoeud(noeud.droite)
                
                else: # Sinon, enfant droit pas complet : regarder si l'etage le plus bas est occupe ou vide
                    taille_enfant_complet_minus = pow(2,hauteur-1) - 1  # nb noeuds d'un enfant sans le dernier etage
                    
                    # Si le dernier etage est occupe : supprimer a droite
                    if noeud.droite.nbNoeuds - taille_enfant_complet_minus > 0: 
                        return self.supprDernierNoeud(noeud.droite)
                    else: # Sinon, dernier etage vide : dernier noeud a gauche
                        return self.supprDernierNoeud(noeud.gauche)
                    
            else: # Sinon, gauche pas complet : dernier noeud a gauche
                return self.supprDernierNoeud(noeud.gauche)



    def descente(self, noeud):
        # Reorganise le tas en structure de tas min correcte a partir d'un noeud (la racine).
        # Descend le noeud dans le tas tant que ce noeud est plus grand que son enfant.

        # etape 1 : trouver le nouveau min du tas avant de descendre
        if noeud.gauche:

            # Si le nouveau min est l'enfant gauche
            if noeud.droite and inf(noeud.gauche.cle, noeud.cle) and inf(noeud.gauche.cle, noeud.droite.cle):
                noeud.gauche.cle, noeud.cle = noeud.cle, noeud.gauche.cle
                noeud = noeud.gauche
            # Si le nouveau min est l'enfant droite
            elif noeud.droite and inf(noeud.droite.cle, noeud.cle) and inf(noeud.droite.cle, noeud.gauche.cle):
                noeud.droite.cle, noeud.cle = noeud.cle, noeud.droite.cle
                noeud = noeud.droite
            # Sinon, pas d'enfant droite (car les cles sont differentes donc une doit être inferieure
            # a l'autre)
            elif inf(noeud.gauche.cle, noeud.cle):
                noeud.gauche.cle, noeud.cle = noeud.cle, noeud.gauche.cle
                noeud = noeud.gauche

        # etape 2 : tant que le noeud n'a pas atteint le bas du tas ou tant qu'il y a encore des cles a echanger
        while noeud.gauche and (inf(noeud.gauche.cle,noeud.cle) or (noeud.droite and inf(noeud.droite.cle,noeud.cle))):
            if inf(noeud.gauche.cle, noeud.cle): # echanger a gauche
                noeud.gauche.cle, noeud.cle = noeud.cle, noeud.gauche.cle
                noeud = noeud.gauche
            else: # sinon, echanger a droite
                noeud.droite.cle, noeud.cle = noeud.cle, noeud.droite.cle
                noeud = noeud.droite


    def Construction(self,listeCles):
        # Construit le tas min arbre contenant les cles de listeCles.
        # Hypothese : le tas donne en parametre est vide.

        if listeCles == []:
            return
        self.AjoutConstruction(listeCles) # etape 1 : construire un tas non ordonne
        self.MiseAJourNbNoeuds(self.racine) # etape 2 : mettre a jour le nombre de noeuds pour chaque noeud
        self.RemonterConstruction(self.racine) # etape 3 : faire des remontees pour les noeuds non ordonnes dans le tas


    def AjoutConstruction(self,listeCles):
        # Construit le tas avec les cles de listeCles sans l'ordonner en tas min.
        # Hypothese : le tas donne en parametre est vide

        self.racine = Noeud(listeCles[0]) # creer la racine
        self.AjoutConstructionRec(self.racine,listeCles,0) # ajouter les autres cles


    def AjoutConstructionRec(self, noeud, listeCles, position):
        # Fonction recursive qui a un noeud donne, cree ses enfants gauche et droite en
        # recuperant leur cle correspondante dans listeCles a l'aide de position.
        # Remarque : calculer la position dans listeCles de l'enfant s'inspire de tas min
        # tableau. Pour un noeud i, son enfant gauche est a la position 2i+1 et son
        # enfant droite a la position 2i+2.

        if noeud is None or position >= len(listeCles):
            return
        
        gauche_position = 2 * position + 1 # position a ajouter comme enfant gauche
        droite_position = 2 * position + 2 # position a ajouter comme enfant droite

        if gauche_position < len(listeCles): # si la position de l'enfant gauche existe dans le tas
            noeud.gauche = Noeud(listeCles[gauche_position]) # creer son enfant gauche et l'ajouter au tas
            noeud.gauche.parent = noeud # ajouter le parent de l'enfant gauche
            self.AjoutConstructionRec(noeud.gauche, listeCles, gauche_position) # ajouter les enfants de l'enfant gauche

        if droite_position < len(listeCles): # même traitement pour enfant droite
            noeud.droite = Noeud(listeCles[droite_position])
            noeud.droite.parent = noeud
            self.AjoutConstructionRec(noeud.droite, listeCles, droite_position)


    def RemonterConstruction(self, noeud):
        # Fonction recursive qui reordonne le tas en tas min correct en faisant des remontees
        # sur les noeuds.

        if noeud is None: # Si le noeud est vide
            return  
        self.RemonterConstruction(noeud.gauche)  # Faire la remontee de l'enfant gauche
        self.RemonterConstruction(noeud.droite)  # et celle de l'enfant droite

        # Tant que le noeud n'est pas la racine et que le noeud est plus petit que son parent
        while noeud.parent is not None and inf(noeud.cle , noeud.parent.cle):
            noeud.cle, noeud.parent.cle = noeud.parent.cle, noeud.cle # echanger le noeud et le parent
            noeud = noeud.parent # continuer de remonter



    def MiseAJourNbNoeuds(self,noeud):
        # Fonction qui met a jour le nombre de noeuds (taille) du sous-arbre noeud

        if noeud is None: # Rien a traiter
            return
        self.MiseAJourNbNoeuds(noeud.gauche) # mettre a jour le nombre de noeuds des enfants
        self.MiseAJourNbNoeuds(noeud.droite)

        # Mise a jour du nombre de noeuds selon si les enfants de noeud existent
        if noeud.gauche is None and noeud.droite is None:
            noeud.nbNoeuds = 1
        elif noeud.gauche is None:
            noeud.nbNoeuds = noeud.droite.nbNoeuds + 1
        elif noeud.droite is None:
            noeud.nbNoeuds = noeud.gauche.nbNoeuds + 1
        else:
            noeud.nbNoeuds = noeud.gauche.nbNoeuds + noeud.droite.nbNoeuds + 1



    def obtenirListeCles(self):
        # Fonction qui retourne la liste des cles dans le tas

        listeCles = []
        self.obtenirListeClesRec(self.racine,listeCles)
        return listeCles
    

    def obtenirListeClesRec(self,noeud,listeCles):
        # Fonction recursive qui, a une liste de cles, ajoute les cles de noeud et celles de ses
        # enfants.

        if noeud is None:
            return
        listeCles.append(noeud.cle)
        self.obtenirListeClesRec(noeud.gauche,listeCles)
        self.obtenirListeClesRec(noeud.droite,listeCles)


    def Union(self,tas2):
        # Fonction qui retourne le tas fusion de deux tas.
        # Hypothese : les cles de tas1 et tas2 sont distinctes les unes des autres

        tas = TasMinArbre()
        listeCles = self.obtenirListeCles() # recuperer la liste des cles du tas1
        listeCles += tas2.obtenirListeCles() # concatener la liste de cles du tas2 a celle du tas 2
        tas.Construction(listeCles) # construire un nouveau tas a partir de la nouvelle liste de cles
        return tas
    


def afficher_arbre(noeud, profondeur=0):
    # Fonction utilisee lors des tests pour afficher un tas min arbre

    if noeud is not None:
        print(" " * (profondeur * 4) + f"-- {str(noeud.cle)}")
        afficher_arbre(noeud.gauche, profondeur + 1)
        afficher_arbre(noeud.droite, profondeur + 1)



#--------------------- TAS MIN TABLEAU -------------------------------------#

# structure tableau
class TasMinTableau:
    def __init__(self):
        self.tas=[]


    def AjoutsIteratifs(self,listeCles):
        # Fonction qui ajoute en iteratif au tas les cles de listeCles en faisant appel à
        # la fonction ajout.
        for cle in listeCles:
            self.ajout(cle)

    def ajout(self,element):
        # Ajoute un element au tas et reordonne le tas en structure de tas min correcte

        self.tas.append(element) # Ajoute l'element a la fin du tas
        ifils = len(self.tas) - 1 # indice du fils dans le tas
        ipere = (ifils-1) // 2 # indice du pere dans le tas

        # Tant que le fils est plus petit que son pere et que nous n'avons pas atteint la racine
        while (ipere >= 0 and inf(self.tas[ifils], self.tas[ipere] )) : 
            self.tas[ifils],self.tas[ipere] = self.tas[ipere],self.tas[ifils] # echanger le pere et le fils
            ifils = ipere
            ipere = (ifils-1) // 2 # remonter dans l'arbre
    

    def supprMin(self):
        # Supprime le minimum d'un tas min tableau (la racine du tas), trie le tableau en une
        # structure de tas min correcte et renvoie le minimum supprime.

        if len(self.tas) == 0: # si le tas est vide
            return None
        if len(self.tas) == 1: # si le tas ne contient qu'un element
            return self.tas.pop()

        # Sinon, supprimer la racine (le min du tas) et reordonner le tas
        min_element = self.tas[0]  # l'element minimum est a la racine
        self.tas[0] = self.tas.pop()  # remplacer la racine par le dernier element du tas
        taille = len(self.tas)
        i = 0 # position de la racine que nous devons bien placer dans le tas min

        while True:
            gauche = 2 * i + 1  # indice du fils gauche
            droite = 2 * i + 2  # indice du fils droit
            indice_min = i  # indice du plus petit element entre le pere et ses fils

            # Comparer qui est plus petit entre le noeud i et ses enfants gauche et droite
            if gauche < taille and inf(self.tas[gauche] , self.tas[indice_min]): # si le fils gauche est plus petit que le pere
                indice_min = gauche  # l'indice du plus petit est le fils gauche

            if droite < taille and inf(self.tas[droite] , self.tas[indice_min]): # idem fils droit
                indice_min = droite

            if indice_min != i:  # si le pere n'est pas le plus petit, il faut echanger le pere et le fils
                self.tas[i], self.tas[indice_min] = self.tas[indice_min], self.tas[i]
                i = indice_min  # descendre dans l'arbre
            else:
                break # sinon, reordonnement termine

        return min_element # retourner l'element min supprime


    def Construction(self, listeCles):
        # Fonction qui construit un tas min tableau a partir des cles de listeCles
        # Hypothese : le tas passe en parametre est vide

        self.tas = listeCles # listeCles devient le tas non ordonne
        taille = len(self.tas)

        # Parcourir le tableau du bas en haut sans s'occuper des feuilles
        for i in range(taille // 2, -1, -1):
            self.RemonterConstruction(i) # reordonner le noeud i


    def RemonterConstruction(self, indice):
        # Fonction qui reordonne un noeud en position indice dans le tas, de sorte que le
        # noeud soit plus petit que ses enfants

        taille = len(self.tas)
        while True :
            gauche = 2 * indice + 1 # indice enfant gauche
            droite = 2 * indice + 2 # indice enfant droite
            indice_min = indice # indice du plus petit element entre le pere et ses fils

            # si le fils gauche est plus petit que le pere
            if gauche < taille and inf(self.tas[gauche] , self.tas[indice_min]):
                indice_min = gauche # l'indice du plus petit cherche est le fils gauche

            # si le fils droit est plus petit que le pere
            if droite < taille and inf(self.tas[droite] , self.tas[indice_min]):
                indice_min = droite

            if indice_min != indice: # si le pere n'est pas le plus petit, il faut echanger le pere et le fils
                self.tas[indice], self.tas[indice_min] = self.tas[indice_min], self.tas[indice]
                indice = indice_min # descendre dans l'arbre

            else: # le noeud est a la bonne place dans le tas : plus d'echange a faire
                break



    def afficher_arbre(self, indice=0, profondeur=0):
        # Fonction utilisee lors des tests pour afficher un tas min tableau
        if indice < len(self.tas):
            print(" " * (profondeur * 4) + f"-- {self.tas[indice]}")
            self.afficher_arbre(2 * indice + 1, profondeur + 1)  # Fils gauche
            self.afficher_arbre(2 * indice + 2, profondeur + 1)  # Fils droit


            

    #Q2.6
    def Union(self,tas2):
        # Fonction qui retourne l'union de deux tas ne contenant aucune cle commune
        
        tas = TasMinTableau() # Creer un nouveau tas vide dans lequel
        tas.tas = self.tas + tas2.tas # Ajouter les elements des deux tas pour obtenir un tas non ordonne
        tas.Construction(tas.tas) # Construire le tas
        return tas # Retourner le tas union des deux tas
    




#--------------------------------------------------------------------------#

#Q3.10

class Node:
    def __init__(self, cle):
        self.cle = cle

    def __str__(self):
        return f"Node({self.cle})"
    
    def print_tree(self, level):
        print(' ' * level*2 + str(self.cle))
    

class TasBinomial:
    def __init__(self,cle=None):
        if cle is None:
           self.racine = None
           self.degre = 0
           self.children = []
        else:
           self.racine = Node(cle)
           self.degre = 0
           self.children = [] # noeuds enfants du noeud racine

    def __str__(self):
        return f"TasBinomial(degre={self.degre}, racine={self.racine}, children={[str(child) for child in self.children]})"


    def EstVide(self):  # retourne True si le tas est vide, False sinon
        return self.racine is None

    
    def Degre(self):    # retourne le degre du tas
        return self.degre
    
    def Union2Tid(self, tas): # union de deux tas binomiaux de meme degre
        if self == tas: # si les deux tas sont identiques
            print("Les deux tas sont identiques")
            return TasBinomial()    # retourner un tas vide
        if self.racine is None or tas.racine is None:   # si un des deux tas est vide
            print("Un des deux tas est vide")
            return TasBinomial()    # retourner un tas vide
        if self.degre != tas.degre: # si les deux tas n'ont pas le meme degre
            print("Les deux tas n'ont pas le même degre")
            return TasBinomial()    # retourner un tas vide
        if inf(self.racine.cle, tas.racine.cle):    # si la racine du premier tas (self) est plus petite que celle du deuxieme
            self.children.append(tas)   # ajouter le tas a la liste des enfants du premier tas (self)
            self.degre += 1 
            return self
        else:   # sinon, la racine du deuxieme tas est plus petite que celle du premier (self)
            tas.children.append(self)   # ajouter le premier tas (self) a la liste des enfants du deuxieme tas
            tas.degre += 1
            return tas



    # def Decapite(self): #renvoie la file binomiale obtenue en supprimant la racine du tas
    #     file = FileBinomiale()
    #     for i in range(len(self.children)):
    #         file = file.AjoutMin(self.children[i])
    #     return file
    
    # def File(self): # renvoie la file binomiale reduite au tournoi
    #     file = FileBinomiale()
    #     file.liste.append(self)
    #     return file
    
    def Decapite(self): #renvoie la file binomiale obtenue en supprimant la racine du tas
        return FileBinomiale(self.children)

    def File(self):
        # renvoie la file binomiale reduite au tournoi
        return FileBinomiale([self])
    

    def print_tree(self, level=0): # affichage de l'arbre ne fonctionne pas si on utilise Union2Tid et que les deux tas n'ont pas le meme degre
        try:
            if self.racine is not None:
                print(' ' * level + str(self.racine.cle))
                for i in range(len(self.children)):
                    self.children[i].print_tree(level + 1)
        except AttributeError:
            print("Le tas est None")

    def print_tas(self,level=0):
        if self is None:
            print("Le tas est None")
        else:
            tas_str = str(self.racine.cle) +' '*level+ "["
            for i in range(len(self.children)):
                tas_str += self.children[i].print_tas(level +1)
            tas_str += "]"
            return tas_str
        
    def afficher_tas_binomial(self, niveau=0):
        if not self.racine:
            return ""
        indentation = "  " * niveau
        result = f"{indentation}{self.racine}\n"

        for enfant in self.children:
            result += enfant.afficher_tas_binomial(niveau + 1)

        return result 


class FileBinomiale:
    def __init__(self, liste_tas=[]):
        self.liste = liste_tas

    def __str__(self):
        file_str = "FileBinomiale(liste=["
        for tas in self.liste:
            file_str += "\n" + tas.print_tas()
        file_str += "])"
        return file_str
    
    def estVide(self): # retourne True si la file est vide, False sinon
        return self.liste == []

    def MinDegre(self): # retourne le tas de degre minimum
        if self.estVide():  # si la file est vide,
            return TasBinomial()    # retourner un tas vide
        min = self.liste[-1]    # sinon, le tas de degre minimum est le dernier tas de la file
        return min  

    def Reste(self):  # retourne le reste de la file privee de son tournoi de degre minimum
        if self.estVide():  # si la file est vide
            return FileBinomiale()
        self.liste.pop()    # supprimer le dernier tas de la file
        return self

    def AjoutMin(self, tas):  # ajoute le tas a la file, avec le degre de tas < MinDegre(self)
        """"Hypothese : le tas est de degre inferieur au MinDegre de la file"""
        if not tas.EstVide():
            self.liste.append(tas)
        return self

    def trier(self):  # trier la file par degre decroissant
        self.liste.sort(key=lambda tas: tas.degre, reverse=True ) # trier la liste par degre decroissant
    
    def UnionFile(self, file2): # union de deux files binomiales, O(log(n+m))
        return self.UFret(file2, TasBinomial())

            
    def UFret(self, file2, T): # union de deux files binomiales, algorithme donne dans le cours
        if T.EstVide():
            if self.estVide():
                return file2
            if file2.estVide():
                return self
            T1 = self.MinDegre()
            T2 = file2.MinDegre()
            if T1.Degre() < T2.Degre():
                tmp_reste = self.Reste()
                Ufile = (tmp_reste).UnionFile(file2)
                return Ufile.AjoutMin(T1)
            if T2.Degre() < T1.Degre():
                tmp_reste2 = file2.Reste()
                Ufile = (tmp_reste2).UnionFile(self)
                return Ufile.AjoutMin(T2)
            if T1.Degre() == T2.Degre():
                F1 = self.Reste()
                F2 = file2.Reste()
                tmp = T1.Union2Tid(T2)
                return F1.UFret(F2,tmp )
        else:
            if self.estVide():
                tmp= T.File()
                return tmp.UnionFile(file2)
            if file2.estVide():
                tmp = T.File()
                return tmp.UnionFile(self)
            T1 = self.MinDegre()
            T2 = file2.MinDegre()
            if T.Degre() < T1.Degre() and T.Degre() < T2.Degre():
                Ufile = self.UnionFile(file2)
                return Ufile.AjoutMin(T)
            if T.Degre() == T1.Degre() and T.Degre() == T2.Degre():
                F1 = self.Reste()
                F2 = file2.Reste()
                tmp = T1.Union2Tid(T2)
                ufret = F1.UFret(F2, tmp)
                return ufret.AjoutMin(T)
            if T.Degre() == T1.Degre() and T.Degre() < T2.Degre():
                F1 = self.Reste()
                tmp= T1.Union2Tid(T)
                return F1.UFret(file2, tmp)
            if T.Degre() == T2.Degre() and T.Degre() < T1.Degre():
                F2 = file2.Reste()
                tmp= T2.Union2Tid(T)
                return F2.UFret(self, tmp)

    def afficher_file_binomiale(self):
        result = ""
        for tas in self.liste:
            result += tas.afficher_tas_binomial()
        return result





    def Ajout(self, tas):  # ajoute le tas a la file, O(log(n))
        if self.estVide() : # si la file est vide
            self.liste.append(tas) # on ajoute le tas a la file
            return self
        else :  # sinon, la file n'est pas vide
            file2 = tas.File()  # on cree une file avec le tas
            return self.UnionFile(file2)    # on fait l'union de la file et de la nouvelle file obtenue





    def SupprMin(self): # supprime le tas de degre minimum de la file, O(log(n))
        if self.estVide():  # si la file est vide
            return None
        min_tas = self.liste[0] # sinon, on recupere le premier tas de la file
        for i in range(1,len(self.liste)):  # on parcourt la file pour trouver le tas avec la cle minimum
            tas = self.liste[i] 
            if inf(tas.racine.cle,min_tas.racine.cle): # tas courant possede le min
                min_tas = tas   
        
        self.liste.remove(min_tas)  # on supprime le tas contenant le min de la file
        file = min_tas.Decapite()   # la file binomiale obtenue en supprimant ce min (racine du tas)
        self = self.UnionFile(file) # on fait l'union de la file et de la nouvelle file obtenue en supprimant la racine du tas  
        return self
    


    def Construction(self, listeCles):  # construit une file binomiale a partir d'une liste de cles, O(n log(n))
        file = self 
        for cle in listeCles:   # pour chaque cle de la liste
            tas = TasBinomial(cle)  # on cree un tas avec la cle
            file = file.Ajout(tas)  # on ajoute le tas a la file
        return file




#----------------------------------------------#



def leftrotate(x, c):   # fonction de rotation a gauche
    return ((x << c) | (x >> (32 - c))) & 0xFFFFFFFF

def md(msg):

    # Definir r comme suit :
    r = [
        7, 12, 17, 22,  7, 12, 17, 22,  7, 12, 17, 22,  7, 12, 17, 22,  # 0..15
        5,  9, 14, 20,  5,  9, 14, 20,  5,  9, 14, 20,  5,  9, 14, 20,  # 16..31
        4, 11, 16, 23,  4, 11, 16, 23,  4, 11, 16, 23,  4, 11, 16, 23,  # 32..47
        6, 10, 15, 21,  6, 10, 15, 21,  6, 10, 15, 21,  6, 10, 15, 21   # 48..63
    ]

    # Initialiser k comme un tableau de 64 zeros
    k = [0] * 64

    # MD5 utilise des sinus d'entiers pour ses constantes :
    for i in range(64):
        # k[i] = int(abs(sin(i + 1)) * (2**32))
        k[i] = floor(abs(sin(i + 1)) * (2**32))

    # Preparation des variables :
    h0 = 0x67452301
    h1 = 0xEFCDAB89
    h2 = 0x98BADCFE
    h3 = 0x10325476


    #Preparation du message (padding) :
    #ajouter le bit "1" au message
    msg = msg.encode()  # convertir le string en bytes
    original_length_in_bits = (8 * len(msg))
    msg += b'\x80'  # ajouter le bit "1" au message

    # #ajouter le bit "0" jusqu'a ce que la taille du message en bits soit egale a 448 (mod 512)
    padding = (448 - (len(msg) * 8)) % 512 //8 # Calculer le nombre d'octets de valeur 0 a ajouter
    msg += b'\x00' * padding    # ajouter des octets de valeur 0


    #ajouter la taille du message initial(avant le padding) codee en 64-bit little-endian au message
    msg += original_length_in_bits.to_bytes(8, byteorder='little')
    #.to_bytes(8, byteorder='little') : convertir la taille du message en chaine bytes, le parametre 8 indique la taille de la chaine bytes (64bits)

    #Decoupage en blocs de 512 bits :
    for i in range(0, len(msg), 64): # pour chaque bloc de 512 bits
        bloc = msg[i:i + 64]

        #Decoupage en blocs de 512bits en 16 mots de 32 bits :

        w = [int.from_bytes(bloc[j:j + 4], byteorder='little') for j in range(0, 64, 4)] # on recupere les 16 mots de 32 bits
        # bloc[j:j+4] : on recupere 4 octets (32 bits) du bloc 
        # int.from_bytes(bloc[j:j+4], byteorder='little') : on convertit les 4 octets en entier de 32bits
        # for j in range(0, len(bloc), 4) : on parcourt le bloc de 4 en 4 octets (32 bits)

        #Initialisation des valeurs de hachage
        a = h0
        b = h1
        c = h2
        d = h3

        #Boucle principal
        for i in range(64): # pour chaque tour de boucle (64 tours) de 0 a 63
            if i <= 15:
                f = (b & c) | ((~b) & d)    # f = (b and c) or ((not b) and d)
                g = i   
            elif i <= 31:
                f = (d & b) | ((~d) & c)    # f = (d and b) or ((not d) and c)
                g = (5*i + 1) % 16
            elif i <= 47:
                f = b ^ c ^ d        # f = b xor c xor d
                g = (3*i + 5) % 16
            else:
                f = c ^ (b | (~d))  # f = c xor (b or (not d))
                g = (7*i) % 16      # g = (7*i) mod 16

            tmp = d
            d = c
            c = b
            tmp2 = (f + a + k[i] + w[g]) & 0xFFFFFFFF
            b = (b + leftrotate(tmp2, r[i])) & 0xFFFFFFFF
            a = tmp

        #Ajout du resultat au bloc precedent
        h0 = (h0 + a) & 0xFFFFFFFF  # On effectue un ET logique avec 0xFFFFFFFF pour ne garder que les 32 bits, car python utilise des entiers de taille infinie
        h1 = (h1 + b) & 0xFFFFFFFF
        h2 = (h2 + c) & 0xFFFFFFFF
        h3 = (h3 + d) & 0xFFFFFFFF

    
    empreinte = (h0.to_bytes(4, 'little') + h1.to_bytes(4, 'little') + h2.to_bytes(4, 'little') + h3.to_bytes(4, 'little'))
    return empreinte.hex()




#--------------------------------------------------------------------------#

# 5 - Arbre de recherche

class NoeudABR:
    def __init__(self,cle):
        self.cle = cle
        self.gauche = None
        self.droite = None


class ABR :
    def __init__(self, cle=None):
        if cle is None:
            self.racine = None
        else:
            self.racine = NoeudABR(cle)


    def EstABRVide(self):   # retourne True si l'arbre est vide, False sinon
        return self.racine is None

    
    def AjoutABR(self, cle):    # ajoute la cle a l'arbre
        nouveau_noeud = NoeudABR(cle)   # creer un nouveau noeud avec la cle
        if self.EstABRVide():   # si l'arbre est vide
            self.racine = nouveau_noeud # le nouveau noeud devient la racine
        else:   # sinon, l'arbre n'est pas vide
            if inf(self.racine.cle, cle):   # si la cle est plus grande que la cle du noeud courant
                if self.racine.droite is None:  # si le noeud courant n'a pas de fils droit
                    self.racine.droite = nouveau_noeud  # le nouveau noeud devient le fils droit du noeud courant
                else:   # sinon, on part dans le sous arbre droit du noeud courant
                    self.AjoutABRrec(self.racine.droite, nouveau_noeud) 
            elif inf(cle, self.racine.cle): # si la cle est plus petite que la cle du noeud courant
                if self.racine.gauche is None:  # si le noeud courant n'a pas de fils gauche
                    self.racine.gauche = nouveau_noeud  # le nouveau noeud devient le fils gauche du noeud courant
                else:   # sinon, on part dans le sous arbre gauche du noeud courant
                    self.AjoutABRrec(self.racine.gauche, nouveau_noeud) 
            else:   # sinon, la cle est egale a la cle du noeud courant
                print("La cle est deja dans l'arbre")

    def AjoutABRrec(self, noeud, nouveau_noeud):    # ajoute la cle a l'arbre, fonction recursive
        if noeud is None:   # si le noeud est vide
            noeud = nouveau_noeud
        elif inf(nouveau_noeud.cle, noeud.cle):  # si la cle est plus petite que la cle du noeud courant
            if noeud.gauche is None:    # si le noeud courant n'a pas de fils gauche
                noeud.gauche = nouveau_noeud
            else:   # sinon, on part dans le sous arbre gauche du noeud courant
                self.AjoutABRrec(noeud.gauche, nouveau_noeud)
        elif inf(noeud.cle, nouveau_noeud.cle): # si la cle est plus grande que la cle du noeud courant
            if noeud.droite is None:    # si le noeud courant n'a pas de fils droit
                noeud.droite = nouveau_noeud
            else:   # sinon, on part dans le sous arbre droit du noeud courant
                self.AjoutABRrec(noeud.droite, nouveau_noeud)
        else:   # sinon, la cle est egale a la cle du noeud courant
            print("La cle est deja dans l'arbre")



    def RechercheABR(self, noeud, cle): # recherche si la cle est dans l'arbre
        if noeud is None:   # si le noeud est vide
            return False    
        if eg(cle, noeud.cle):  # si la cle est egale a la cle du noeud
            return True
        if inf(cle, noeud.cle): # si la cle est plus petite que la cle du noeud courant
            return self.RechercheABR(noeud.gauche, cle) # rechercher a gauche
        else:   # sinon, la cle est plus grande que la cle du noeud courant
            return self.RechercheABR(noeud.droite, cle) # rechercher a droite

    def AjoutListeCles(self, listeCles):  # ajoute les cles de la liste a l'arbre
        for cle in listeCles:   # pour chaque cle de la liste
            self.AjoutABR(cle)  # ajouter la cle a l'arbre

    def SupprABR(self, cle):    # supprime la cle de l'arbre
        if eg(cle, self.racine.cle):    # si la cle est egale a la cle de la racine
            self.racine = self.supprRacine(self.racine) # supprimer la racine de l'arbre
        else:   # sinon, la cle n'est pas egale a la cle de la racine
            self.supprRec(self.racine, cle) # supprimer la cle dans l'arbre


    def supprRec(self, noeud, cle): # supprime la cle de l'arbre, fonction recursive
        if noeud is None:   # si le noeud est vide
            return None
        if eg(cle, noeud.cle):  # si la cle est egale a la cle du noeud
            return self.supprRacine(noeud)  # supprimer la racine
        if inf(cle, noeud.cle): # si la cle est plus petite que la cle du noeud courant
            noeud.gauche = self.supprRec(noeud.gauche, cle) # supprimer la cle dans le sous arbre gauche
        else:   # sinon, la cle est plus grande que la cle du noeud courant
            noeud.droite = self.supprRec(noeud.droite, cle) # supprimer la cle dans le sous arbre droit
        return noeud    # retourner le noeud
    


    def supprRacine(self, noeud):   # supprimer la racine, si c'est l'element a supprimer
        if noeud.gauche is None and noeud.droite is None:   # si le noeud est une feuille
            return None
        if noeud.gauche is None:    # si le noeud n'a pas de fils gauche
            tmp = noeud.droite
            noeud.droite = None
            return tmp  # on retourne le fils droit
        if noeud.droite is None:    # si le noeud n'a pas de fils droit
            tmp = noeud.gauche
            noeud.gauche = None
            return tmp  # on retourne le fils gauche
        noeud.cle = self.min(noeud.droite)  # on remplace la racine par le minimum du sous arbre droit, on peut egalement prendre le maximum du sous arbre gauche
        noeud.droite = self.supprRec(noeud.droite, noeud.cle)  # on supprime le minimum du sous arbre droit
        return noeud    # on retourne le noeud
    
    def min(self, noeud):   # retourne le minimum de l'arbre
        while noeud.gauche is not None: # tant que le fils gauche n'est pas vide
            noeud = noeud.gauche    # on descend dans l'arbre
        return noeud.cle    # on retourne le minimum de l'arbre
    
    def hauteurMax(self, noeud):    # retourne la hauteur maximale de l'arbre
        if noeud is None:
            return 0
        return 1 + max(self.hauteurMax(noeud.gauche), self.hauteurMax(noeud.droite))    
    
    def hauteurMin(self, noeud):    # retourne la hauteur minimale de l'arbre
        if noeud is None:
            return 0
        return 1 + min(self.hauteurMin(noeud.gauche), self.hauteurMin(noeud.droite))
    
    def nombreNoeuds(self, noeud):  # retourne le nombre de noeuds de l'arbre (en comptant la racine)
        if noeud is None:
            return 0
        return 1 + self.nombreNoeuds(noeud.gauche) + self.nombreNoeuds(noeud.droite)
    

    

# -------------------------------------------------------------------------------------------- #    
# Fonctions utiles pour les tests de performance    
    
def lire_fichier(nom_fichier):  # on lit le fichier et on retourne les lignes dans un tableau
    with open(nom_fichier, 'r') as fichier:
        lignes = fichier.readlines()
    return lignes


def CreerCle(ligne):
    hexa = ligne.split('0x') # on separe avec 0x
    hexa= hexa[1] # on recupere la partie hexa
    hexa = hexa.zfill(32) # on complete avec des 0
    parties = re.findall(r'.{1,8}', hexa) # on separe en 4 parties de 8 bits
    p1 = int(parties[0],16)
    p2 = int(parties[1],16)
    p3 = int(parties[2],16)
    p4 = int(parties[3],16)
    cle = Cle128(p1,p2,p3,p4)
    return cle

def FichierClesToListeCles(fichier,taille):
    # a partir d'un fichier contenant une liste de cles (en hexa) de taille specifique,
    # retourne la liste de Cle128 associee
    listeCles = []
    f = open(fichier,"r")
    for i in range(taille):
        ligne = f.readline().rstrip() # lire ligne et supprimer caractere fin de chaine
        cle = CreerCle(ligne)
        listeCles.append(cle)
    f.close()
    return listeCles


def HashToCle(hash):
    parties = re.findall(r'.{1,8}', hash) # on separe en 4 parties de 8 bits
    p1 = int(parties[0],16)
    p2 = int(parties[1],16)
    p3 = int(parties[2],16)
    p4 = int(parties[3],16)
    cle = Cle128(p1,p2,p3,p4)
    return cle