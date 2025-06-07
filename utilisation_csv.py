import csv
from classes import *


def e3D_from_csv (catalogue_csv) :
    etoiles3D = []

    with open(catalogue_csv, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for ligne in reader:
            ligne = [champ.strip() for champ in ligne]

            if len(ligne) < 4:
                print("Ligne ignorée (incomplète) :", ligne)
                continue

            asc = float(ligne[0])
            decl = float(ligne[1])
            num = int(ligne[2])
            magn = float(ligne[3])

            etoile = Etoile3D(decl, asc, num, magn)
            etoiles3D.append (etoile)

    return etoiles3D
