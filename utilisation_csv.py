import csv
from classes import *


def 3D_from_csv (catalogue_csv) :
    etoiles3D = []

    with open(catalogue_csv, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for ligne in reader:
            asc = ligne[0]
            decl = ligne[1]
            num = ligne[2]
            magn = ligne[3]

            etoile = Etoile3D(decl, asc, num, magn)
            etoiles3D.append (etoile)
