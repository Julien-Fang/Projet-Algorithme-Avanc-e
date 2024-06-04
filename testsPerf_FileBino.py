from projet import *
import time
import matplotlib.pyplot as plt


def testPerfConstructionFileBinomiale():
    Ly_FileBinomiale = []
    perf = open("perf_Construction_FileBinomiale.txt","w")
    tailles_listes = [1000,5000,10000,20000,50000,80000,120000,200000]
    # tailles_listes = [1000,5000,10000,20000]
    for taille in tailles_listes:
        sommeFB = 0
        for i in range(1,6): 
            fichier = "cles_alea/jeu_" + str(i) + "_nb_cles_" + str(taille) + ".txt"
            listeCles = FichierClesToListeCles(fichier,taille)
            fileBinomiale = FileBinomiale()

            t1_FB = time.process_time()
            fileBinomiale = fileBinomiale.Construction(listeCles)
            t2_FB = time.process_time()
            sommeFB += t2_FB - t1_FB
        
        tempsFB = sommeFB / 5
        Ly_FileBinomiale.append(tempsFB)
        perf.write(str(taille) + " " + str(tempsFB) + '\n')

    perf.close()
    plt.plot(tailles_listes, Ly_FileBinomiale, 'o-', color = "r", label="Complexité file binomiale")
    plt.legend()
    plt.xlabel("taille file binomiale (éléments)")
    plt.ylabel("temps (secondes)")
    plt.title("Complexité de Construction pour File Binomiale")
    plt.grid(True)
    plt.show()


testPerfConstructionFileBinomiale()







def testPerfUnionFileBinomiale():
    Ly_FileBinomiale = []
    perf = open("perf_Union_FileBinomiale.txt","w")
    tailles_listes = [(1000,5000),(5000,10000),(10000,20000),(1000,50000),
                      (20000,50000),(20000,80000),(10000,120000),(10000,200000)]
    for taille1,taille2 in tailles_listes:
        sommeFB = 0
        for i in range(1,6):
            fichier1 = "cles_alea/jeu_" + str(i) + "_nb_cles_" + str(taille1) + ".txt"
            fichier2 = "cles_alea/jeu_" + str(i) + "_nb_cles_" + str(taille2) + ".txt"
            listeCles1 = FichierClesToListeCles(fichier1,taille1)
            listeCles2 = FichierClesToListeCles(fichier2,taille2)

            fileBinomiale1 = FileBinomiale()
            fileBinomiale2 = FileBinomiale()

            fileBinomiale1 = fileBinomiale1.Construction(listeCles1)
            fileBinomiale2 = fileBinomiale2.Construction(listeCles2)

            t1_FB = time.process_time()
            fileBinomiale = fileBinomiale1.UnionFile(fileBinomiale2)
            t2_FB = time.process_time()
            sommeFB += t2_FB - t1_FB
            # print("sommeFB : ", sommeFB)

        tempsFB = sommeFB / 5
        # print("tempsFB : ", tempsFB)
        Ly_FileBinomiale.append(tempsFB)
        perf.write(str(taille1+taille2) + " " +  str(tempsFB) + '\n')

    perf.close()
    Lx = [taille1+taille2 for taille1,taille2 in tailles_listes]
    plt.plot(Lx, Ly_FileBinomiale, 'o-', color = "r", label="Complexité file binomiale")
    plt.legend()
    plt.xlabel("taille file binomiale (éléments)")
    plt.ylabel("temps (secondes)")
    plt.title("Complexité de Union pour File Binomiale")
    plt.grid(True)
    plt.show()


# testPerfUnionFileBinomiale()







