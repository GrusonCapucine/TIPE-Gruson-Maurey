from comparaison_triangles import *
from projection_etoiles3D import *
from systeme_boites import *

tasc = [math.radians(x) for x in [30, 34, 55, 15, 50, 85, 25, 40, 60, 20]]
tdecl = [math.radians(x) for x in [10, 20, 30, -5, 5, -20, 0, 15, 35, -10]]
catalogue = [Etoile3D(tdecl[i], tasc[i], i, 1.0) for i in range (len(tdecl))]

#Etoile 2D volontairement extraites du catalogue pour le test
#Verifie uniquement la cohérence des triangles et boites
etoiles2D  = calcul_projection_3D(catalogue, 0)
for m0 in etoiles2D :
    m0.set_sguide(-1)
guide = calcul_projection_3D(catalogue, 0)

scores = calcul_sj(etoiles2D, guide)

asso = assos_Ds_de_M (scores)

i=0
j=0
for m0,d0 in asso.items() :
    xm0, ym0 = m0.get_abs(), m0.get_ord()
    xd00, yd00 = d0[0].get_abs(), d0[0].get_ord()
    xd01, yd01 = d0[1].get_abs(), d0[1].get_ord()

    print("m0 indice " + str(i))
    print("Coord m0 :" + str(xm0) + ", " + str(ym0))
    print("Coord d0 " +str(j) + " : " + str(xd00) + ", " + str(yd00))
    print("Coord d0 " +str(j+1) + " : " + str(xd01) + ", " + str(yd01))

    print("\n")
    i = i+1
    j=j+2


marquage_m0 (etoiles2D, guide)

i=0
for m0 in etoiles2D :
    print("Etoile guide de m0 num " + str(i) + " : " + str(m0.get_sguide()))
    i+=1

r = resultat_identification (etoiles2D)
print("\nRésultat identification : " +str(r))
