from projet import *
import time
import matplotlib.pyplot as plt


def testPerfAjoutsItTasMin():
    Ly_TasArbre = []
    Ly_TasTab = []
    perf = open("perf_AjoutsIteratifs_TasMin.txt","w")
    tailles_listes = [1000,5000,10000,20000,50000,80000,120000,200000]
    for taille in tailles_listes:
        sommeTA = 0
        sommeTT = 0
        for i in range(1,6):
            fichier = "cles_alea/jeu_" + str(i) + "_nb_cles_" + str(taille) + ".txt"
            listeCles = FichierClesToListeCles(fichier,taille)
            tasArbre = TasMinArbre()
            tasTab = TasMinTableau()

            t1_TA = time.process_time()
            tasArbre.AjoutsIteratifs(listeCles)
            t2_TA = time.process_time()
            sommeTA += t2_TA - t1_TA

            t1_TT = time.process_time()
            tasTab.AjoutsIteratifs(listeCles)
            t2_TT = time.process_time()
            sommeTT += t2_TT - t1_TT

        tempsTA = sommeTA / 5
        tempsTT = sommeTT / 5
        Ly_TasArbre.append(tempsTA)
        Ly_TasTab.append(tempsTT)
        perf.write(str(taille) + " " + str(tempsTA) + " " + str(tempsTT) + '\n')

    perf.close()
    plt.plot(tailles_listes, Ly_TasArbre, 'o-', color = "r", label="Complexité tas arbre")
    plt.plot(tailles_listes, Ly_TasTab, 'o-', color = "b", label="Complexité tas tableau")
    plt.legend()
    plt.xlabel("taille tas (éléments)")
    plt.ylabel("temps (secondes)")
    plt.title("Complexité de Ajouts Itératifs pour Tas Min")
    plt.grid(True)
    plt.show()


testPerfAjoutsItTasMin()




def testPerfConstructionTasMin():
    Ly_TasArbre = []
    Ly_TasTab = []
    perf = open("perf_Construction_TasMin.txt","w")
    tailles_listes = [1000,5000,10000,20000,50000,80000,120000,200000]
    for taille in tailles_listes:
        sommeTA = 0
        sommeTT = 0
        for i in range(1,6):
            fichier = "cles_alea/jeu_" + str(i) + "_nb_cles_" + str(taille) + ".txt"
            listeCles = FichierClesToListeCles(fichier,taille)
            tasArbre = TasMinArbre()
            tasTab = TasMinTableau()

            t1_TA = time.process_time()
            tasArbre.Construction(listeCles)
            t2_TA = time.process_time()
            sommeTA += t2_TA - t1_TA

            t1_TT = time.process_time()
            tasTab.Construction(listeCles)
            t2_TT = time.process_time()
            sommeTT += t2_TT - t1_TT
        
        tempsTA = sommeTA / 5
        tempsTT = sommeTT / 5
        Ly_TasArbre.append(tempsTA)
        Ly_TasTab.append(tempsTT)
        perf.write(str(taille) + " " + str(tempsTA) + " " + str(tempsTT) + '\n')

    perf.close()
    plt.plot(tailles_listes, Ly_TasArbre, 'o-', color = "r", label="Complexité tas arbre")
    plt.plot(tailles_listes, Ly_TasTab, 'o-', color = "b", label="Complexité tas tableau")
    plt.legend()
    plt.xlabel("taille tas (éléments)")
    plt.ylabel("temps (secondes)")
    plt.title("Complexité de Construction pour Tas Min")
    plt.grid(True)
    plt.show()


# testPerfConstructionTasMin()


def testPerfUnionTasMin():
    # Lx = []
    Ly_TasArbre = []
    Ly_TasTab = []
    perf = open("perf_Union_TasMin.txt","w")
    tailles_listes = [(1000,5000),(5000,10000),(10000,20000),(1000,50000),
                      (20000,50000),(20000,80000),(10000,120000),(10000,200000)]
    for taille1,taille2 in tailles_listes:
        sommeTA = 0
        sommeTT = 0
        for i in range(1,6):
            fichier1 = "cles_alea/jeu_" + str(i) + "_nb_cles_" + str(taille1) + ".txt"
            fichier2 = "cles_alea/jeu_" + str(i) + "_nb_cles_" + str(taille2) + ".txt"
            listeCles1 = FichierClesToListeCles(fichier1,taille1)
            listeCles2 = FichierClesToListeCles(fichier2,taille2)
            tasArbre1 = TasMinArbre()
            tasArbre2 = TasMinArbre()
            tasTab1 = TasMinTableau()
            tasTab2 = TasMinTableau()

            tasArbre1.Construction(listeCles1)
            tasArbre2.Construction(listeCles2)
            tasTab1.Construction(listeCles1)
            tasTab2.Construction(listeCles2)

            t1_TA = time.process_time()
            tasArbre = tasArbre1.Union(tasArbre2)
            t2_TA = time.process_time()
            sommeTA += t2_TA - t1_TA

            t1_TT = time.process_time()
            tasTab = tasTab1.Union(tasTab2)
            t2_TT = time.process_time()
            sommeTT += t2_TT - t1_TT
        
        tempsTA = sommeTA / 5
        tempsTT = sommeTT / 5
        Ly_TasArbre.append(tempsTA)
        Ly_TasTab.append(tempsTT)
        perf.write(str(taille1+taille2) + " " + str(tempsTA) + " " + str(tempsTT) + '\n')

    perf.close()
    Lx = [taille1+taille2 for taille1,taille2 in tailles_listes]
    plt.plot(Lx, Ly_TasArbre, 'o-', color = "r", label="Complexité tas arbre")
    plt.plot(Lx, Ly_TasTab, 'o-', color = "b", label="Complexité tas tableau")
    plt.legend()
    plt.xlabel("taille tas (éléments)")
    plt.ylabel("temps (secondes)")
    plt.title("Complexité de Union pour Tas Min")
    plt.grid(True)
    plt.show()


# testPerfUnionTasMin()






