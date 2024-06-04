from projet import *
import time
import matplotlib.pyplot as plt




def etude_tempsSupprMin():
    lignes = open("Shakespeare_hash.txt","r").readlines()
    fd = open("etudeExp_SupprMin.txt", "w")
    listeCles = []
    for hash in lignes:
        cle = HashToCle(hash.rstrip())
        listeCles.append(cle)

    sommeTasArbre = 0
    sommeTasTab = 0
    sommeFile = 0
    for i in range(10):
        listeClesTMP = listeCles.copy()
        tasMinArbre = TasMinArbre()
        tasMinTab = TasMinTableau()
        fileBino = FileBinomiale()

        tasMinArbre.Construction(listeClesTMP)
        tasMinTab.Construction(listeClesTMP)
        fileBino = fileBino.Construction(listeClesTMP)

        t1_TasA = time.process_time()
        while tasMinArbre.racine is not None :
            tasMinArbre.supprMin()
        t2_TasA = time.process_time()
        sommeTasArbre += t2_TasA - t1_TasA

        t1_TasT = time.process_time()
        while tasMinTab.tas != [] :
            tasMinTab.supprMin()
        t2_TasT = time.process_time()
        sommeTasTab += t2_TasT - t1_TasT

        t1_File = time.process_time()
        while fileBino is not None :
            fileBino = fileBino.SupprMin()
        t2_File = time.process_time()
        sommeFile += t2_File - t1_File

    fig, ax = plt.subplots()

    tArbre = sommeTasArbre/10
    tTab = sommeTasTab/10
    tFile = sommeFile/10
    fd.write(str(tArbre) + " " + str(tTab) + " " + str(tFile))

    structures = ["Tas Min Arbre", "Tas Min Tableau", "File Binomiale"]
    temps = [tArbre, tTab, tFile]
    bar_colors = ['tab:red', 'tab:blue', 'tab:orange']

    ax.bar(structures, temps, color=bar_colors)

    ax.set_ylabel('temps (secondes)')
    ax.set_title("Comparaison des temps d'exécution de SupprMin")
    plt.grid(True)
    plt.show()
    fd.close()


etude_tempsSupprMin()



def etude_tempsAjout():
    lignes = open("Shakespeare_hash.txt","r").readlines()
    fd = open("etudeExp_Ajout.txt", "w")
    listeCles = []
    for hash in lignes:
        cle = HashToCle(hash.rstrip())
        listeCles.append(cle)

    sommeTasArbre = 0
    sommeTasTab = 0
    sommeFile = 0
    for i in range(10):
        listeClesTMP = listeCles.copy()
        tasMinArbre = TasMinArbre()
        tasMinTab = TasMinTableau()
        fileBino = FileBinomiale()

        t1_TasA = time.process_time()
        for cle in listeClesTMP :
            tasMinArbre.Ajout(cle)
        t2_TasA = time.process_time()
        sommeTasArbre += t2_TasA - t1_TasA

        t1_TasT = time.process_time()
        for cle in listeClesTMP :
            tasMinTab.ajout(cle)
        t2_TasT = time.process_time()
        sommeTasTab += t2_TasT - t1_TasT

        t1_File = time.process_time()
        for cle in listeClesTMP :
            tas = TasBinomial(cle)
            fileBino = fileBino.Ajout(tas)
        t2_File = time.process_time()
        sommeFile += t2_File - t1_File


    fig, ax = plt.subplots()

    tArbre = sommeTasArbre/10
    tTab = sommeTasTab/10
    tFile = sommeFile/10
    fd.write(str(tArbre) + " " + str(tTab) + " " + str(tFile))

    structures = ["Tas Min Arbre", "Tas Min Tableau", "File Binomiale"]
    temps = [tArbre, tTab, tFile]
    bar_colors = ['tab:red', 'tab:blue', 'tab:orange']

    ax.bar(structures, temps, color=bar_colors)

    ax.set_ylabel('temps (secondes)')
    ax.set_title("Comparaison des temps d'exécution de Ajout")
    plt.grid(True)
    plt.show()

    fd.close()


# etude_tempsAjout()


def etude_tempsConstruction():
    lignes = open("Shakespeare_hash.txt","r").readlines()
    fd = open("etudeExp_Construction.txt", "w")
    listeCles = []
    for hash in lignes:
        cle = HashToCle(hash.rstrip())
        listeCles.append(cle)

    sommeTasArbre = 0
    sommeTasTab = 0
    sommeFile = 0
    for i in range(10):
        listeClesTMP = listeCles.copy()
        tasMinArbre = TasMinArbre()
        tasMinTab = TasMinTableau()
        fileBino = FileBinomiale()

        t1_TasA = time.process_time()
        tasMinArbre.Construction(listeClesTMP)
        t2_TasA = time.process_time()
        sommeTasArbre += t2_TasA - t1_TasA

        t1_TasT = time.process_time()
        tasMinTab.Construction(listeClesTMP)
        t2_TasT = time.process_time()
        sommeTasTab += t2_TasT - t1_TasT

        t1_File = time.process_time()
        fileBino = fileBino.Construction(listeClesTMP)
        t2_File = time.process_time()
        sommeFile += t2_File - t1_File


    fig, ax = plt.subplots()

    tArbre = sommeTasArbre/10
    tTab = sommeTasTab/10
    tFile = sommeFile/10
    fd.write(str(tArbre) + " " + str(tTab) + " " + str(tFile))

    structures = ["Tas Min Arbre", "Tas Min Tableau", "File Binomiale"]
    temps = [tArbre, tTab, tFile]
    bar_colors = ['tab:red', 'tab:blue', 'tab:orange']

    ax.bar(structures, temps, color=bar_colors)

    ax.set_ylabel('temps (secondes)')
    ax.set_title("Comparaison des temps d'exécution de Construction")
    plt.grid(True)
    plt.show()

    fd.close()


# etude_tempsConstruction()


def etude_tempsUnion():
    lignes = open("Shakespeare_hash.txt","r").readlines()
    fd = open("etudeExp_Union.txt", "w")
    listeCles = []
    for hash in lignes:
        cle = HashToCle(hash.rstrip())
        listeCles.append(cle)

    sommeTasArbre = 0
    sommeTasTab = 0
    sommeFile = 0

    milieu = len(listeCles)//2
    listeCles1 = listeCles[:milieu]
    listeCles2 = listeCles[milieu:]

    for i in range(10):
        listeClesTMP1 = listeCles1.copy()
        listeClesTMP2 = listeCles2.copy()

        tasMinArbre1 = TasMinArbre()
        tasMinArbre2 = TasMinArbre()
        tasMinTab1 = TasMinTableau()
        tasMinTab2 = TasMinTableau()
        fileBino1 = FileBinomiale()
        fileBino2 = FileBinomiale()

        tasMinArbre1.Construction(listeClesTMP1)
        tasMinArbre2.Construction(listeClesTMP2)
        tasMinTab1.Construction(listeClesTMP1)
        tasMinTab2.Construction(listeClesTMP2)
        fileBino1 = fileBino1.Construction(listeClesTMP1)
        fileBino2 = fileBino2.Construction(listeClesTMP2)

        t1_TasA = time.process_time()
        tasMinArbre1.Union(tasMinArbre2)
        t2_TasA = time.process_time()
        sommeTasArbre += t2_TasA - t1_TasA

        t1_TasT = time.process_time()
        tasMinTab1.Union(tasMinTab2)
        t2_TasT = time.process_time()
        sommeTasTab += t2_TasT - t1_TasT

        t1_File = time.process_time()
        fileBino1.UnionFile(fileBino2)
        t2_File = time.process_time()
        sommeFile += t2_File - t1_File

    fig, ax = plt.subplots()

    tArbre = sommeTasArbre/10
    tTab = sommeTasTab/10
    tFile = sommeFile/10
    fd.write(str(tArbre) + " " + str(tTab) + " " + str(tFile))

    structures = ["Tas Min Arbre", "Tas Min Tableau", "File Binomiale"]
    temps = [tArbre, tTab, tFile]
    bar_colors = ['tab:red', 'tab:blue', 'tab:orange']

    ax.bar(structures, temps, color=bar_colors)

    ax.set_ylabel('temps (secondes)')
    ax.set_title("Comparaison des temps d'exécution de Union")
    plt.grid(True)
    plt.show()

    fd.close()


# etude_tempsUnion()