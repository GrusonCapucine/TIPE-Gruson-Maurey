import csv
from classes import *


def e3D_from_csv (catalogue_csv) :
    etoiles3D = []

    with open(catalogue_csv, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for ligne in reader:
            ligne = [champ.strip() for champ in ligne]

            if len(ligne) < 4:
                print("Ligne ignorée (incomplète) :", ligne)
                continue

            asc = float(ligne[7])
            decl = float(ligne[8])
            num = int(ligne[0])
            magn = float(ligne[10])

            if (asc < 6 and asc > 4):
                if (decl < 1 and decl > 0.2):
                    etoile = Etoile3D(decl, asc, num, magn)
                    etoiles3D.append (etoile)

    return etoiles3D
