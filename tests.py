from projet import *
import time
import matplotlib.pyplot as plt
import hashlib











def test_MD5():
    aTester = {
        "": "d41d8cd98f00b204e9800998ecf8427e",
        "a": "0cc175b9c0f1b6a831c399e269772661",
        "abc": "900150983cd24fb0d6963f7d28e17f72",
        "message digest": "f96b697d7cb7938d525a2f31aaf161d0",
        "abcdefghijklmnopqrstuvwxyz": "c3fcd3d76192e4007dfb496cca67e13b",
        "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789": "d174ab98d277d9f5a5611c2c9f419d9f",
        "12345678901234567890123456789012345678901234567890123456789012345678901234567890": "57edf4a22be3c955ac49da2e2107b67a",
    }
    for msg, hash in aTester.items():
        assert(md(msg) == hash)

# test_MD5()






#--------------------------------------------------------------------------#

#Jeux de Test 
cle1 = Cle128(10, 20, 30, 41)
cle2 = Cle128(10, 20, 30, 40)
cle3 = Cle128(50, 60, 70, 80)

cle4 = Cle128(5, 3, 8, 2)
cle5 = Cle128(7, 1, 6, 4)
cle6 = Cle128(9, 10, 11, 12)

def testInf_Eg():
    #Jeux de Test de Inf
    print("Test de la fonction inf:")
    print(inf(cle1, cle2))  # Devrait afficher False (cle1 == cle2)
    print(inf(cle1, cle3))  # Devrait afficher True (cle1 < cle3)
    print(inf(cle3, cle1))  # Devrait afficher False (cle3 > cle1)

    #Jeux de Test de eg
    print("\nTest de la fonction eg:")
    print(eg(cle1, cle2))  # Devrait afficher True (cle1 == cle2)
    print(eg(cle1, cle3))  # Devrait afficher False (cle1 != cle3)
    print(eg(cle3, cle1))  # Devrait afficher False (cle3 != cle1)

# testInf_Eg()


def testTasMin():
    #Jeux de test pour Arbre Binaire
    print("\nTest de Arbre Binaire:")
    tas = TasMinArbre()

    tas.Ajout(cle1)
    # afficher_arbre(tas.racine)
    # print("\n")
    tas.Ajout(cle2)
    # afficher_arbre(tas.racine)
    # print("\n")
    tas.Ajout(cle3)
    # afficher_arbre(tas.racine)
    # print("\n")
    tas.Ajout(cle4)
    # afficher_arbre(tas.racine)
    # print("\n")
    tas.Ajout(cle5)
    # afficher_arbre(tas.racine)
    # print("\n")
    tas.Ajout(cle6)

    afficher_arbre(tas.racine)

    
    print("-----------------SUPPRMIN TAS ARBRE 1-------------")
    min_element = tas.supprMin()
    afficher_arbre(tas.racine)

    print("-----------------SUPPRMIN TAS ARBRE 2-------------")
    min_element = tas.supprMin()
    afficher_arbre(tas.racine)

    print("-----------------SUPPRMIN TAS ARBRE 3-------------")
    min_element = tas.supprMin()
    afficher_arbre(tas.racine)

    print("-----------------SUPPRMIN TAS ARBRE 4-------------")
    min_element = tas.supprMin()
    afficher_arbre(tas.racine)

    print("-----------------SUPPRMIN TAS ARBRE 5-------------")
    min_element = tas.supprMin()
    afficher_arbre(tas.racine)

    print("-----------------SUPPRMIN TAS ARBRE 6-------------")
    min_element = tas.supprMin()
    afficher_arbre(tas.racine)

    print("-----------------SUPPRMIN TAS ARBRE 7-------------")
    min_element = tas.supprMin()
    afficher_arbre(tas.racine)

    #Jeux de test pour Tableau
    print("\nTest de Tableau:")
    tas = TasMinTableau()
    tas.ajout(cle1)
    tas.ajout(cle2)
    tas.ajout(cle3)
    tas.ajout(cle4)
    tas.ajout(cle5)
    tas.ajout(cle6)
    tas.afficher_arbre()
    min_element = tas.supprMin()

    print("--------------SUPPRMIN TAS TAB 1 --------")
    tas.afficher_arbre()

    print("--------------SUPPRMIN TAS TAB 2 --------")
    min_element = tas.supprMin()
    tas.afficher_arbre()


    print("--------------SUPPRMIN TAS TAB 3 --------")
    min_element = tas.supprMin()
    tas.afficher_arbre()

    print("--------------SUPPRMIN TAS TAB 4 --------")
    min_element = tas.supprMin()
    tas.afficher_arbre()

    print("--------------SUPPRMIN TAS TAB 5 --------")
    min_element = tas.supprMin()
    tas.afficher_arbre()

    print("--------------SUPPRMIN TAS TAB 6 --------")
    min_element = tas.supprMin()
    tas.afficher_arbre()

    print("--------------SUPPRMIN TAS TAB 7 --------")
    min_element = tas.supprMin()
    tas.afficher_arbre()

    print("-----------------TEST TAS ARBRE-------------\n")

    tas2 = TasMinArbre()
    tas2.Ajout(Cle128(5, 44, 30, 40))
    afficher_arbre(tas2.racine)
    tas2.Ajout(Cle128(4, 20, 65, 98))
    afficher_arbre(tas2.racine)
    tas2.Ajout(Cle128(3, 60, 70, 80))
    afficher_arbre(tas2.racine)
    tas2.Ajout(Cle128(15, 3, 8, 2))
    afficher_arbre(tas2.racine)
    tas2.Ajout(Cle128(2, 1, 6, 4))
    afficher_arbre(tas2.racine)
    tas2.Ajout(Cle128(20, 10, 3, 17))
    afficher_arbre(tas2.racine)
    tas2.Ajout(Cle128(9, 21, 11, 14))
    afficher_arbre(tas2.racine)
    tas2.Ajout(Cle128(16, 33, 90, 12))
    afficher_arbre(tas2.racine)



    #Jeux de test pour AjoutsIteratifs
    print("\nTest de AjoutsIteratifs du tableau:")
    tas = TasMinTableau()

    tas.AjoutsIteratifs([cle1, cle2, cle3, cle4, cle5, cle6])
    tas.afficher_arbre()
    min_element = tas.supprMin()
    print("----------------------")
    tas.afficher_arbre()

    #Jeux de test pour Construire Arbre
    print("\n----------------Construction Arbre------------------")
    tas = TasMinArbre()
    tas.Construction([cle1, cle2, cle3, cle4, cle5, cle6])
    afficher_arbre(tas.racine)
    print("NOMBRE DE NOEUD : ", tas.racine.nbNoeuds)
    min_element = tas.supprMin()
    print("-----------SUPPRMIN 1fois DE Construction-----------")
    afficher_arbre(tas.racine)
    print("NOMBRE DE NOEUD : ", tas.racine.nbNoeuds)
    min_element = tas.supprMin()
    print("-----------SUPPRMIN 2fois DE Construction-----------")
    afficher_arbre(tas.racine)
    print("NOMBRE DE NOEUD : ", tas.racine.nbNoeuds)
    min_element = tas.supprMin()
    print("-----------SUPPRMIN 3fois DE Construction-----------")
    afficher_arbre(tas.racine)
    print("NOMBRE DE NOEUD : ", tas.racine.nbNoeuds)
    min_element = tas.supprMin()
    print("-----------SUPPRMIN 4fois DE Construction-----------")
    afficher_arbre(tas.racine)
    print("NOMBRE DE NOEUD : ", tas.racine.nbNoeuds)
    min_element = tas.supprMin()
    print("-----------SUPPRMIN 5fois DE Construction-----------")
    afficher_arbre(tas.racine)
    print("NOMBRE DE NOEUD : ", tas.racine.nbNoeuds)
    min_element = tas.supprMin()
    print("-----------SUPPRMIN 6fois DE Construction-----------")
    afficher_arbre(tas.racine)
    # print("NOMBRE DE NOEUD : ", tas.racine.nbNoeuds)
    min_element = tas.supprMin()
    print("-----------SUPPRMIN 7fois DE Construction-----------")
    afficher_arbre(tas.racine)
    # print("NOMBRE DE NOEUD : ", tas.racine.nbNoeuds)


    print("\n--------------------Test de Union ARBRE--------------------")
    tas3 = TasMinArbre()
    tas3.AjoutsIteratifs([cle1, cle2, cle3, cle4, cle5, cle6])

    tas4 = TasMinArbre()
    tas4.Ajout(Cle128(5, 44, 30, 40))
    tas4.Ajout(Cle128(4, 20, 65, 98))
    tas4.Ajout(Cle128(3, 60, 70, 80))
    tas4.Ajout(Cle128(15, 3, 8, 2))
    tas4.Ajout(Cle128(2, 1, 6, 4))
    tas4.Ajout(Cle128(20, 10, 3, 17))
    tas4.Ajout(Cle128(9, 21, 11, 14))
    tas4.Ajout(Cle128(16, 33, 90, 12))
    print("---------------------------------OK--------------------------")
    nouveau_tas = TasMinArbre()
    nouveau_tas = tas3.Union(tas4)
    afficher_arbre(nouveau_tas.racine)





    #Jeux de test pour Construction Tableau
    print("\nTest de Construction Tableau:")
    tas = TasMinTableau()
    tas.Construction([cle1, cle2, cle3, cle4, cle5, cle6])
    tas.afficher_arbre()
    min_element = tas.supprMin()
    print("----------------------")
    tas.afficher_arbre()

    #Jeux de test pour Union

    print("\n--------------------Test2 de Union ARBRE--------------------")
    tas1 = TasMinArbre()
    tas1.AjoutsIteratifs([cle1, cle2, cle3, cle4, cle5, cle6])

    cle7 = Cle128(6, 9, 10, 20)
    cle8 = Cle128(30, 40, 50, 60)
    cle9 = Cle128(70, 80, 90, 100)
    cle10 = Cle128(110, 120, 130, 140)

    tas2 = TasMinArbre()
    tas2.AjoutsIteratifs([cle7, cle8, cle9, cle10])

    print("\n---------------------------------OK--------------------------\n")
    nouveau_tas = TasMinArbre()
    nouveau_tas = tas1.Union(tas2)
    afficher_arbre(nouveau_tas.racine)

    print("\n--------------------Test de Union TABLEAU--------------------")
    tas1 = TasMinTableau()
    tas1.AjoutsIteratifs([cle1, cle2, cle3, cle4, cle5, cle6])
    tas2 = TasMinTableau()

    tas2.AjoutsIteratifs([cle7, cle8, cle9, cle10])
    tas = TasMinTableau()
    tas = tas1.Union(tas2)
    tas.afficher_arbre()

    print("\n--------------------Autre test de suppr min arbre--------------------")
    tas = TasMinArbre()
    tas.Ajout(Cle128(0, 44, 30, 40))
    tas.Ajout(Cle128(1, 44, 30, 40))
    tas.Ajout(Cle128(4, 44, 30, 40))
    tas.Ajout(Cle128(2, 44, 30, 40))
    tas.Ajout(Cle128(7, 44, 30, 40))
    tas.Ajout(Cle128(6, 44, 30, 40))
    tas.Ajout(Cle128(8, 44, 30, 40))
    tas.Ajout(Cle128(5, 44, 30, 40))
    afficher_arbre(tas.racine)
    print("----------suppr min 1------------")
    tas.supprMin()
    afficher_arbre(tas.racine)
    print("----------suppr min 2------------")
    tas.supprMin()
    afficher_arbre(tas.racine)
    print("----------suppr min 3------------")
    tas.supprMin()
    afficher_arbre(tas.racine)
    print("----------suppr min 4------------")
    tas.supprMin()
    afficher_arbre(tas.racine)
    print("----------suppr min 5------------")
    tas.supprMin()
    afficher_arbre(tas.racine)
    print("----------suppr min 6------------")
    tas.supprMin()
    afficher_arbre(tas.racine)
    print("----------suppr min 7------------")
    tas.supprMin()
    afficher_arbre(tas.racine)
    print("----------suppr min 8------------")
    tas.supprMin()
    afficher_arbre(tas.racine)

    print("\n--------------------Autre test de suppr min tableau--------------------")
    tas = TasMinTableau()
    tas.ajout(Cle128(0, 44, 30, 40))
    tas.ajout(Cle128(1, 44, 30, 40))
    tas.ajout(Cle128(4, 44, 30, 40))
    tas.ajout(Cle128(2, 44, 30, 40))
    tas.ajout(Cle128(7, 44, 30, 40))
    tas.ajout(Cle128(6, 44, 30, 40))
    tas.ajout(Cle128(8, 44, 30, 40))
    tas.ajout(Cle128(5, 44, 30, 40))
    tas.afficher_arbre()
    print("----------suppr min 1------------")
    tas.supprMin()
    tas.afficher_arbre()
    print("----------suppr min 2------------")
    tas.supprMin()
    tas.afficher_arbre()
    print("----------suppr min 3-----------")
    tas.supprMin()
    tas.afficher_arbre()
    print("----------suppr min 4------------")
    tas.supprMin()
    tas.afficher_arbre()
    print("----------suppr min 5------------")
    tas.supprMin()
    tas.afficher_arbre()
    print("----------suppr min 6------------")
    tas.supprMin()
    tas.afficher_arbre()
    print("----------suppr min 7------------")
    tas.supprMin()
    tas.afficher_arbre()
    print("----------suppr min 8------------")
    tas.supprMin()
    tas.afficher_arbre()

testTasMin()


def testCreerCle():
    #Jeux de test pour CreerClé
    print("\nTest de CreerClé:")
    cle1 = CreerCle("0xdf6943ba6d51464f6b02157933bdd9ad")
    cle2 = CreerCle("0x5f003a2587337655af8a166be8439a49")
    cle3 = CreerCle("0x1573c8d156d03e633c20c36f1b70862")

    print("Cle 1 \n")
    print(cle1.v1)
    print(cle1.v2)
    print(cle1.v3)
    print(cle1.v4)
    print("Cle 2 \n")
    print(cle2.v1)
    print(cle2.v2)
    print(cle2.v3)
    print(cle2.v4)
    print("Cle 3 \n")
    print(cle3.v1)
    print(cle3.v2)
    print(cle3.v3)
    print(cle3.v4)

    #Tester egalité clé
    cle4 = CreerCle("0x1573c8d156d03e633c20c36f1b70862")
    print("\nEgalité clé 3 et clé 4 :")
    print(eg(cle3, cle4))  # True (cle3 == cle4)
    print("\nEgalité clé 1 et clé 2 :")
    print(eg(cle1, cle2))  # False (cle1 != cle2)
    print("\nEgalité clé 1 et clé 3 :")
    print(eg(cle1, cle3))  # False (cle1 != cle3)

    cle1 = CreerCle("0xdf6943ba6d51464f6b02157933bdd9ad")
    cle2 = CreerCle("0x5f003a2587337655af8a166be8439a49")
    cle3 = CreerCle("0x1573c8d156d03e633c20c36f1b70862")

    #Tester inf clé
    print("\nInf clé 1 et clé 2 :")
    print(inf(cle1, cle2))  # False (cle1 > cle2)
    print("\nInf clé 1 et clé 3 :")
    print(inf(cle1, cle3))  # False (cle1 > cle3)
    print("\nInf clé 3 et clé 1 :")
    print(inf(cle3, cle1))  # True (cle3 < cle1)
    print("\nInf clé 3 et clé 4 :")
    print(inf(cle3, cle4))  # False (cle3 == cle4)

# testCreerCle()


def testTasBinomial():
    #Jeux de test pour le Tas Binomial
    print("\n----------TAS1------------\n")

    cle1 = Cle128(5, 44, 30, 40)
    cle2 = Cle128(4, 20, 65, 98)
    cle3 = Cle128(3, 60, 70, 80)
    cle4 = Cle128(15, 3, 8, 2)
    cle5 = Cle128(2, 1, 6, 4)
    cle6 = Cle128(20, 10, 3, 17)
    cle7 = Cle128(9, 21, 11, 14)
    cle8 = Cle128(16, 33, 90, 12)

    tasB = TasBinomial(cle1)
    tasB= tasB.Union2Tid(TasBinomial(cle2))

    tasB1= TasBinomial(cle3)
    tasB1= tasB1.Union2Tid(TasBinomial(cle4))

    tasB = tasB.Union2Tid(tasB1)

    tasB.print_tree()

    print("\n----------TAS2------------\n")
    tasB2 = TasBinomial(cle5)
    tasB2 = tasB2.Union2Tid(TasBinomial(cle6))
    tasB3 = TasBinomial(cle7)
    tasB3 = tasB3.Union2Tid(TasBinomial(cle8))

    tasB2 = tasB2.Union2Tid(tasB3)
    tasB2.print_tree()
    print("\n----------FUSION TAS1 TAS2------------\n")
    tasB = tasB.Union2Tid(tasB2)
    tasB.print_tree()

    print("\n----------Decapite------------\n")
    fileDecapiter = tasB.Decapite()
    print(fileDecapiter)

    print("\n----------File------------\n")
    tasB.print_tree()
    fileF = tasB.File()

    print("\n----------MinDegre------------\n")
    fileFBis = fileF
    tasMinDegre = fileFBis.MinDegre()
    print(tasMinDegre)

    print("\n----------Reste------------\n")
    print("1")
    print(fileF)
    TasReste = TasBinomial(Cle128(1, 44, 30, 40))
    fileF.Ajout(TasReste)
    print("mine\n")
    print(fileF)
    TasReste1 = TasBinomial(Cle128(2, 20, 65, 98))
    TasReste1 = TasReste1.Union2Tid(TasBinomial(Cle128(3, 60, 70, 80)))
    fileF.Ajout(TasReste1)
    print("2")
    print(fileF)
    fileReste = fileF.Reste()
    print("3")
    print(fileReste)

    print("\n----------Construction------------\n")
    fileConstruite = FileBinomiale()
    cle1 = Cle128(1, 44, 30, 40)
    cle2 = Cle128(2, 20, 65, 98)
    cle3 = Cle128(3, 60, 70, 80)
    cle4 = Cle128(4, 3, 8, 2)
    cle5 = Cle128(5, 1, 6, 4)
    cle6 = Cle128(6, 10, 3, 17)
    cle7 = Cle128(7, 21, 11, 14)
    cle8 = Cle128(8, 33, 90, 12)
    cle9 = Cle128(9, 44, 30, 40)
    cle10 = Cle128(10, 20, 65, 98)

    fileConstruite = fileConstruite.Construction([cle1,cle2,cle3,cle4,cle5,cle6,cle7,cle8,cle9,cle10])
    print(fileConstruite)

# testTasBinomial()


def testFileBinomiale():
    cle1 = Cle128(5, 44, 30, 40)
    cle2 = Cle128(4, 20, 65, 98)
    cle3 = Cle128(3, 60, 70, 80)
    cle4 = Cle128(15, 3, 8, 2)
    cle5 = Cle128(2, 1, 6, 4)
    cle6 = Cle128(20, 10, 3, 17)
    cle7 = Cle128(9, 21, 11, 14)
    cle8 = Cle128(16, 33, 90, 12)

    fb= FileBinomiale()

    tb1 = TasBinomial(cle1)
    tb2 = TasBinomial(cle2)
    tb3 = TasBinomial(cle3)
    print("\n----------estVide------------\n")
    print("fb est vide ?",fb.estVide()) # True

    print("\n----------AjoutMin------------\n")
    fbAjoutMin = FileBinomiale()
    tb1 = TasBinomial(cle1)
    tb2 = TasBinomial(cle2)
    tb3 = TasBinomial(cle3)
    fbAjoutMin.AjoutMin(tb1)
    print(fbAjoutMin.afficher_file_binomiale())
    fbAjoutMin.AjoutMin(tb2)
    print(fbAjoutMin.afficher_file_binomiale())
    fbAjoutMin.AjoutMin(tb3)
    print(fbAjoutMin.afficher_file_binomiale())
    

    
    print("\n----------Ajout------------\n") #faut commencer par ajouter les tas les plus grands

    fbAjout = FileBinomiale()
    tasAjout3 = TasBinomial(cle3)
    tasAjout3 = tasAjout3.Union2Tid(TasBinomial(cle4))
    tasAjout4 = TasBinomial(cle5)
    tasAjout4 = tasAjout4.Union2Tid(TasBinomial(cle6))
    tasAjout3 = tasAjout3.Union2Tid(tasAjout4)
    fbAjout.Ajout(tasAjout3)
    print("fbAjout : ")
    print(fbAjout.afficher_file_binomiale())
    print("-------------")
    tasAjout1 = TasBinomial(cle1)
    tasAjout1 = tasAjout1.Union2Tid(TasBinomial(cle2))
    fbAjout.Ajout(tasAjout1)
    print(fbAjout.afficher_file_binomiale())
    print("-------------")
    tasAjout2 = TasBinomial(cle2)
    fbAjout.Ajout(tasAjout2)
    print("fbAjout : ")
    print(fbAjout.afficher_file_binomiale())


    print("\n----------Reste------------\n")
    fbReste = FileBinomiale()
    TasReste1 = TasBinomial(Cle128(2, 20, 65, 98))
    TasReste1 = TasReste1.Union2Tid(TasBinomial(Cle128(3, 60, 70, 80)))
    fbReste.AjoutMin(TasReste1)
    print(fbReste)
    fbReste.AjoutMin(TasBinomial(Cle128(4, 3, 8, 2)))
    print(fbReste)
    fbReste.AjoutMin(TasBinomial(Cle128(5, 1, 6, 4)))
    print(fbReste.afficher_file_binomiale())
    fileReste = fbReste.Reste()
    print("fileReste : ")
    print(fileReste.afficher_file_binomiale())

    print("\n----------UnionFile------------\n")
    fbUnion1 = FileBinomiale()
    fbUnion2 = FileBinomiale()
    fbUnion3 = FileBinomiale()
    fbUnion1.AjoutMin(TasBinomial(Cle128(1, 44, 30, 40)))
    fbUnion1.AjoutMin(TasBinomial(Cle128(2, 20, 65, 98)))
    print("fbUnion1 : ")
    print(fbUnion1.afficher_file_binomiale())
    fbUnion2.AjoutMin(TasBinomial(Cle128(3, 60, 70, 80)))
    fbUnion1= fbUnion1.UnionFile(fbUnion2)
    print("fbUnion1 : ")
    print(fbUnion1.afficher_file_binomiale())
    fbUnion3.AjoutMin(TasBinomial(Cle128(4, 3, 8, 2)))
    fbUnion1 = fbUnion1.UnionFile(fbUnion3)
    print("fbUnion1 : ")
    print(fbUnion1.afficher_file_binomiale())


    print("\n----------MinDegre------------\n")
    fbMinDegre = FileBinomiale()
    fbMinDegre.AjoutMin(TasBinomial(Cle128(1, 44, 30, 40)))
    fbMinDegre.AjoutMin(TasBinomial(Cle128(2, 20, 65, 98)))
    fbMinDegre.AjoutMin(TasBinomial(Cle128(3, 60, 70, 80)))
    fbMinDegre.AjoutMin(TasBinomial(Cle128(4, 3, 8, 2)))
    fbMinDegre.AjoutMin(TasBinomial(Cle128(5, 1, 6, 4)))
    print(fbMinDegre.afficher_file_binomiale())
    tasMinDegre = fbMinDegre.MinDegre()
    print(tasMinDegre)


    print("\n----------SupprMin------------\n")
    fbSupprMin = FileBinomiale()
    tasSupprMin1 = TasBinomial(cle1)
    tasSupprMin1 = tasSupprMin1.Union2Tid(TasBinomial(cle2))
    fbSupprMin.AjoutMin(tasSupprMin1)
    tasSupprMin2 = TasBinomial(cle3)
    tasSupprMin2 = tasSupprMin2.Union2Tid(TasBinomial(cle4))
    fbSupprMin.AjoutMin(tasSupprMin2)
    tasSupprMin3 = TasBinomial(cle5)
    tasSupprMin3 = tasSupprMin3.Union2Tid(TasBinomial(cle6))
    fbSupprMin.AjoutMin(tasSupprMin3)
    print(fbSupprMin)
    print("-------1------")
    fbSupprMinRetour= fbSupprMin.SupprMin()
    print(fbSupprMin)
    print("-------2------")
    fbSupprMinRetour=fbSupprMin.SupprMin()
    print(fbSupprMin)
    print("-------3------")
    fbSupprMinRetour=fbSupprMin.SupprMin()
    print(fbSupprMin)
    print("-------4------")
    fbSupprMinRetour=fbSupprMin.SupprMin()
    print(fbSupprMin)


# testFileBinomiale()


def testMD5():
    print("\n----------MD5------------\n")
    md5 = md("0x0123456789abcdef0123456789abcdef")
    print(md5)

    print("\n----------MD5 du mot 'the'------------\n")
    md5 = md("the")
    print(md5)

    print("\n----------MD5 verifier'------------\n")
    md5_vrai = hashlib.md5(b"the").digest()  # digest : renvoie le hachage sous forme de bytes
    print(md5_vrai)                 
    
    md5_vrai = binascii.hexlify(md5_vrai).decode() 
    print("md5 :",md5)
    print("md5_vrai :",  md5_vrai) 

    if md5 == md5_vrai:
        print("MD5 correct")
    else:
        print("MD5 incorrect")

    print("\n----------MD5 test2------------\n")
    test2 = md("projet algo")
    print("test : ",test2)
    test2_vrai = hashlib.md5(b"projet algo").digest() 
    test2_vrai = binascii.hexlify(test2_vrai).decode()
    print("test2_vrai : ",test2_vrai)
    if test2 == test2_vrai:
        print("MD5 correct")
    else:
        print("MD5 incorrect")


# testMD5()


