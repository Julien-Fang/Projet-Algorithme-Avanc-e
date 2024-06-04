from projet import *
import time
import matplotlib.pyplot as plt






def testPerfCompConstruction():
    # Lx = []
    Ly_TasArbre = []
    Ly_TasTab = []
    Ly_File = []
    perf = open("perf_Comp_Construction.txt","w")
    tailles_listes = [1000,5000,10000,20000,50000,80000,120000,200000]
    # tailles_listes = [1000,5000,10000,20000]
    for taille in tailles_listes:
        sommeTA = 0
        sommeTT = 0
        sommeFile = 0
        for i in range(1,6):
            fichier = "cles_alea/jeu_" + str(i) + "_nb_cles_" + str(taille) + ".txt"
            listeCles = FichierClesToListeCles(fichier,taille)
            tasArbre = TasMinArbre()
            tasTab = TasMinTableau()
            file = FileBinomiale()

            t1_TA = time.time()
            tasArbre.Construction(listeCles)
            t2_TA = time.time()
            sommeTA += t2_TA - t1_TA
            # print(sommeTA)
            # print(sommeTT)

            t1_TT = time.time()
            tasTab.Construction(listeCles)
            t2_TT = time.time()
            sommeTT += t2_TT - t1_TT

            t1_File = time.time()
            file.Construction(listeCles)
            t2_File = time.time()
            sommeFile += t2_File - t1_File
        
        tempsTA = sommeTA / 5
        tempsTT = sommeTT / 5
        tempsFile = sommeFile / 5
        # Lx.append(taille)
        Ly_TasArbre.append(tempsTA)
        Ly_TasTab.append(tempsTT)
        Ly_File.append(tempsFile)
        perf.write(str(taille) + " " + str(tempsTA) + " " + str(tempsTT) + " " + str(tempsFile) + '\n')

    perf.close()
    Lx = tailles_listes
    plt.plot(Lx, Ly_TasArbre, "r", label="Complexité tas arbre")
    plt.plot(Lx, Ly_TasTab, "b", label="Complexité tas tableau")
    plt.plot(Lx, Ly_File, "g", label="Complexité file binomiale")
    plt.legend()
    plt.xlabel("taille structure (éléments)")
    plt.ylabel("temps (secondes)")
    plt.title("Complexité de Construction")
    plt.grid(True)
    plt.show()


# testPerfCompConstruction()


def testPerfCompUnion():
    # Lx = []
    Ly_TasArbre = []
    Ly_TasTab = []
    Ly_File = []
    perf = open("perf_Comp_Union.txt","w")
    tailles_listes = [(1000,5000),(5000,10000),(10000,20000),(1000,50000),
                      (20000,50000),(20000,80000),(10000,120000),(10000,200000)]
    for taille1,taille2 in tailles_listes:
        sommeTA = 0
        sommeTT = 0
        sommeFile = 0
        for i in range(1,6):
            fichier1 = "cles_alea/jeu_" + str(i) + "_nb_cles_" + str(taille1) + ".txt"
            fichier2 = "cles_alea/jeu_" + str(i) + "_nb_cles_" + str(taille2) + ".txt"
            listeCles1 = FichierClesToListeCles(fichier1,taille1)
            listeCles2 = FichierClesToListeCles(fichier2,taille2)
            tasArbre1 = TasMinArbre()
            tasArbre2 = TasMinArbre()
            tasTab1 = TasMinTableau()
            tasTab2 = TasMinTableau()
            file1 = FileBinomiale()
            file2 = FileBinomiale()

            tasArbre1.Construction(listeCles1)
            tasArbre2.Construction(listeCles2)
            tasTab1.Construction(listeCles1)
            tasTab2.Construction(listeCles2)
            file1 = file1.Construction(listeCles1)
            file2 = file2.Construction(listeCles2)

            t1_TA = time.time()
            tasArbre = tasArbre1.Union(tasArbre2)
            t2_TA = time.time()
            sommeTA += t2_TA - t1_TA
            # print(sommeTA)
            # print(sommeTT)

            t1_TT = time.time()
            tasTab = tasTab1.Union(tasTab2)
            t2_TT = time.time()
            sommeTT += t2_TT - t1_TT

            t1_File = time.time()
            file1.UnionFile(file2)
            t2_File = time.time()
            sommeFile += t2_File - t1_File


        
        tempsTA = sommeTA / 5
        tempsTT = sommeTT / 5
        tempsFile = sommeFile / 5
        # Lx.append(taille)
        Ly_TasArbre.append(tempsTA)
        Ly_TasTab.append(tempsTT)
        Ly_File.append(tempsFile)
        perf.write(str(taille1+taille2) + " " + str(tempsTA) + " " + str(tempsTT) + " " + str(tempsFile) + '\n')

    perf.close()
    Lx = [taille1+taille2 for taille1,taille2 in tailles_listes]
    plt.plot(Lx, Ly_TasArbre, "r", label="Complexité tas arbre")
    plt.plot(Lx, Ly_TasTab, "b", label="Complexité tas tableau")
    plt.plot(Lx, Ly_File, "g", label="Complexité file binomiale")
    plt.legend()
    plt.xlabel("taille structure (éléments)")
    plt.ylabel("temps (secondes)")
    plt.title("Complexité de Union")
    plt.grid(True)
    plt.show()


testPerfCompUnion()