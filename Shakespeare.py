from projet import *
import time
import matplotlib.pyplot as plt


def Shakespeare():
    abr_hash = ABR()
    liste_mots = []
    dico = dict() # dictionnaire des mots
    occurences = dict() # cle : hash, valeur : liste de mots correspondant au hash
    f = open("Shakespeare.txt","r") # fichier qui contient le nom des fichiers de "/Shakespeare"
    fwords = open("Shakespeare_words.txt","w")
    fhash = open("Shakespeare_hash.txt","w")
    t1 = time.time()
    for i in range(37):
        fichier = f.readline().rstrip()
        fd = open(fichier,"r")
        mots = fd.readlines()
        for mot in mots:
            mot = mot.rstrip() # enlever saut de ligne
            hash = md(mot)
            cle = HashToCle(hash)

            # if mot not in liste_mots: # pas encore lu
            #     abr_hash.AjoutABR(cle)
            #     liste_mots.append(mot)
            #     fwords.write(mot + "\n")
            #     fhash.write(hash + "\n")
            #     if hash not in occurences: # première occurrence de hash pour un mot
            #         occurences[hash] = [mot]
            #     else:
            #         liste = occurences.get(hash)
            #         occurences[hash] = liste.append(mot)
            
            if mot not in dico: # on n'a pas encore croisé le mot
                dico[mot] = hash
                if hash not in occurences: # première occurrence de hash pour un mot
                    occurences[hash] = [mot]
                else:
                    liste = occurences.get(hash)
                    occurences[hash] = liste.append(mot)
                abr_hash.AjoutABR(cle)
                liste_mots.append(mot)
                fwords.write(mot + "\n")
                fhash.write(hash + "\n")

    t2 = time.time()
    # print("Temps traitement Shakespeare avec recherche abr :" + str(t2-t1) + "\n")
    print("Temps traitement Shakespeare avec dico :" + str(t2-t1) + "\n")
    fd.close()
    f.close()
    fwords.close()
    fhash.close()
    return abr_hash,liste_mots,occurences

# Shakespeare()

def Shakespeare_occ():
    abr_hash,liste_mots,occurrences = Shakespeare()
    foccurrences = open("Shakespeare_occurrences.txt","w")

    for hash in occurrences:
        liste = occurrences[hash]
        if len(liste) > 1:
            foccurrences.write(hash + " : ")
            for mot in liste:
                foccurrences.write(mot + " ")
            foccurrences.write("\n")

    foccurrences.close()

# Shakespeare_occ()




def testABR():
    print("\n----------Créer ABR + Ajout + Rechercher ------------\n")
    abr = ABR()
    abr.AjoutABR(Cle128(3, 4, 5, 6))
    abr.AjoutABR(Cle128(2, 3, 4, 5))
    abr.AjoutABR(Cle128(1, 2, 3, 4))
    abr.AjoutABR(Cle128(5, 8, 10, 1))
    abr.AjoutABR(Cle128(8, 6, 95, 0))
    abr.AjoutABR(Cle128(7, 4, 5, 6))
    abr.AjoutABR(Cle128(4, 4, 5, 6))
    print(abr.RechercheABR(abr.racine, Cle128(2, 3, 4, 5))) # True
    print(abr.RechercheABR(abr.racine, Cle128(10, 3, 4, 5)))   # False
    print(abr.RechercheABR(abr.racine, Cle128(5, 8, 10, 1)))    # True
    print(abr.RechercheABR(abr.racine, Cle128(8, 6, 95, 0)))    # True
    afficher_arbre(abr.racine)

    print("\n---------- AjoutListeCles abr1 ------------\n")
    abr1 = ABR()
    cle1 = Cle128(1, 44, 30, 40)
    cle2 = Cle128(2, 20, 65, 98)
    cle3 = Cle128(3, 60, 70, 80)
    cle4 = Cle128(4, 3, 8, 2)
    cle5 = Cle128(5, 1, 6, 4)
    cle6 = Cle128(6, 10, 3, 17)
    cle7 = Cle128(7, 21, 11, 14)
    cle8 = Cle128(8, 33, 90, 12)
    abr1.AjoutListeCles([cle5,cle7,cle1,cle6,cle3,cle2,cle8,cle4])
    afficher_arbre(abr1.racine)

    print("\n---------- 2 Cles deja present dans abrr ------------\n")
    abrr= ABR()
    abrr.AjoutListeCles([cle3,cle1,cle2,cle3,cle1])
    afficher_arbre(abrr.racine)

    print("\n---------- SupprABR dans abr1 ------------\n")
    abr1.SupprABR(cle1)
    afficher_arbre(abr1.racine)

    print("\n---------- SupprABR abr2 ------------\n")
    abr2 = ABR()
    abr2.AjoutListeCles([cle8,cle7,cle5,cle6,cle4,cle3,cle2,cle1])
    afficher_arbre(abr2.racine)
    abr2.SupprABR(cle5)
    afficher_arbre(abr2.racine)

    print("\n---------- SupprABR abr3 ------------\n")
    abr3 = ABR()
    abr3.AjoutListeCles([cle5,cle7,cle1,cle6,cle3,cle2,cle8,cle4])
    afficher_arbre(abr3.racine)
    abr3.SupprABR(cle5)
    print("--------------------------")
    afficher_arbre(abr3.racine)


# testABR()
    
def testABR2():
    print("Pour Shakespeare_hash.txt\n")
    lignes = open("Shakespeare_hash.txt", "r").readlines()
    abr = ABR()
    for ligne in lignes:
        abr.AjoutABR(HashToCle(ligne))

    hauteurMinGauche = abr.hauteurMin(abr.racine.gauche)
    hauteurMinDroit = abr.hauteurMin(abr.racine.droite)
    print("hauteurMinGauche : ",hauteurMinGauche)
    print("hauteurMinDroit : ",hauteurMinDroit)

    hauteurMaxGauche = abr.hauteurMax(abr.racine.gauche)
    hauteurMaxDroit = abr.hauteurMax(abr.racine.droite)
    print("hauteurMaxGauche : ",hauteurMaxGauche)
    print("hauteurMaxDroit : ",hauteurMaxDroit)

    nbNoeudsTotal = abr.nombreNoeuds(abr.racine)
    nbNoeudsGauche = abr.nombreNoeuds(abr.racine.gauche)
    nbNoeudsDroit = abr.nombreNoeuds(abr.racine.droite)
    print("nbNoeudsTotal : ",nbNoeudsTotal)
    print("nbNoeudsGauche : ",nbNoeudsGauche)
    print("nbNoeudsDroit : ",nbNoeudsDroit)


# testABR2()


def testABR3():
    print("Cles Aleatoires : \n")
    tailles_listes= [1000,5000,10000,20000,50000,80000,120000,200000]
    NBTotalHauteurMinGauche = 0
    NBTotalHauteurMinDroit = 0
    NBTotalHauteurMaxGauche = 0
    NBTotalHauteurMaxDroit = 0
    NBTotalNoeudsTotal = 0
    NBTotalNoeudsGauche = 0
    NBTotalNoeudsDroit = 0

    
    for taille in tailles_listes:

        for i in range (1,6):

            file = "cles_alea/jeu_" + str(i) + "_nb_cles_" + str(taille) + ".txt"
            listeCles = FichierClesToListeCles(file,taille)
            abr = ABR()
            abr.AjoutListeCles(listeCles)

            print("----------------------------")
            print("Pour ",file,"\n")

            hauteurMinGauche = abr.hauteurMin(abr.racine.gauche)
            hauteurMinDroit = abr.hauteurMin(abr.racine.droite)
            NBTotalHauteurMinGauche += hauteurMinGauche
            NBTotalHauteurMinDroit += hauteurMinDroit
            print("hauteurMinGauche : ",hauteurMinGauche)
            print("hauteurMinDroit : ",hauteurMinDroit)

            hauteurMaxGauche = abr.hauteurMax(abr.racine.gauche)
            hauteurMaxDroit = abr.hauteurMax(abr.racine.droite)
            NBTotalHauteurMaxGauche += hauteurMaxGauche
            NBTotalHauteurMaxDroit += hauteurMaxDroit
            print("hauteurMaxGauche : ",hauteurMaxGauche)
            print("hauteurMaxDroit : ",hauteurMaxDroit)

            nbNoeudsTotal = abr.nombreNoeuds(abr.racine)
            nbNoeudsGauche = abr.nombreNoeuds(abr.racine.gauche)
            nbNoeudsDroit = abr.nombreNoeuds(abr.racine.droite)
            NBTotalNoeudsTotal += nbNoeudsTotal
            NBTotalNoeudsGauche += nbNoeudsGauche
            NBTotalNoeudsDroit += nbNoeudsDroit
            print("nbNoeudsTotal : ",nbNoeudsTotal)
            print("nbNoeudsGauche : ",nbNoeudsGauche)
            print("nbNoeudsDroit : ",nbNoeudsDroit)

    print("\n--------------Nb Total--------------\n")
    print("Nb Total HauteurMinGauche : ",NBTotalHauteurMinGauche)
    print("Nb Total HauteurMinDroit : ",NBTotalHauteurMinDroit)
    print("Nb Total HauteurMaxGauche : ",NBTotalHauteurMaxGauche)
    print("Nb Total HauteurMaxDroit : ",NBTotalHauteurMaxDroit)
    print("Nb Total NoeudsTotal : ",NBTotalNoeudsTotal)
    print("Nb Total NoeudsGauche : ",NBTotalNoeudsGauche)
    print("Nb Total NoeudsDroit : ",NBTotalNoeudsDroit)

# testABR3()