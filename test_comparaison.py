from comparaison_triangles import *
from projection_etoiles3D import *


tasc = [math.radians(x) for x in [30, 34, 55, 15, 50, 85, 25, 40, 60, 20]]
tdecl = [math.radians(x) for x in [10, 20, 30, -5, 5, -20, 0, 15, 35, -10]]
catalogue = [Etoile3D(tdecl[i], tasc[i], i, 1.0) for i in range (len(tdecl))]

#Etoile 2D volontairement extraites du catalogue pour le test
etoiles2D  = calcul_projection_3D(catalogue, 0)
guide = calcul_projection_3D(catalogue, 0)

scores = calcul_sj(etoiles2D, guide)

"""
i=1
for triangle_m0 in scores.keys() :
    m0 = triangle_m0.get_ref()
    xm0, ym0 = m0.get_abs(), m0.get_ord()

    d0 = scores[triangle_m0][1].get_ref()
    xd0, yd0 = d0.get_abs(), d0.get_ord()

    '''print(str(triangle_m0.get_ref()))
    print("score " + str(scores[triangle_m0][0]))
    print("et étoile triangle associée : " + str(scores[triangle_m0][1].get_ref()))'''
    print("m0 numéro " + str(i//2) + " et d0 numéro : " +str(i))
    print("Coord m0 :" + str(xm0) + ", " + str(ym0))
    print("Coord d0 :" + str(xd0) + ", " + str(yd0))

    print("\n")
    i = i+1
"""

asso = assos_Ds_de_M (scores)

i=1
for m0,d0 in asso.items() :
    xm0, ym0 = m0.get_abs(), m0.get_ord()
    xd00, yd00 = d0[0].get_abs(), d0[0].get_ord()
    xd01, yd01 = d0[1].get_abs(), d0[1].get_ord()

    print("m0 numéro " + str(i))
    print("Coord m0 :" + str(xm0) + ", " + str(ym0))
    print("Coord d0 " +str(i) + " : " + str(xd00) + ", " + str(yd00))
    print("Coord d0 " +str(i+1) + " : " + str(xd01) + ", " + str(yd01))

    print("\n")
    i = i+1
