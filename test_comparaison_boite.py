from comparaison_triangles import *
from projection_etoiles3D import *
from systeme_boites import *

tasc = [math.radians(x) for x in [30, 34, 55, 15, 50, 85, 25, 40, 60, 20]]
tdecl = [math.radians(x) for x in [10, 20, 30, -5, 5, -20, 0, 15, 35, -10]]
catalogue = [Etoile3D(tdecl[i], tasc[i], (str(i)+'a'), 1.0) for i in range (len(tdecl))]

#Etoile 2D volontairement extraites du catalogue pour le test
#Verifie uniquement la cohérence des triangles et boites
etoiles2D  = calcul_projection_3D(catalogue, 0)

i=0
for m0 in etoiles2D :
    m0.set_sguide(-1)
    m0.set_idx(i)
    i+=1

print ("***Test triangles et comparaison***\n")
guide = calcul_projection_3D(catalogue, 0)

scores = calcul_sj(etoiles2D, guide)

asso = assos_Ds_de_M (scores)


for m0,d0 in asso.items() :
    xm0, ym0 = m0.get_abs(), m0.get_ord()
    xd00, yd00 = d0[0].get_abs(), d0[0].get_ord()
    xd01, yd01 = d0[1].get_abs(), d0[1].get_ord()

    print("m0 indice " + str(m0.get_idx()))
    print("Coord m0 :" + str(xm0) + ", " + str(ym0))
    print("Coord d0 " +str(d0[0].get_sguide()) + " : " + str(xd00) + ", " + str(yd00))
    print("Coord d0 " +str(d0[1].get_sguide()) + " : " + str(xd01) + ", " + str(yd01))

    print("\n")




print ("\n***Test boites***\n")

best_star_map = []
rmax = -1

#Recherche de la meilleure vue
for i in range (len(etoiles2D)):
    star_map = calcul_projection_2D(etoiles2D, i)

    for j in range (len(catalogue)):
        guide = calcul_projection_3D(catalogue, j)

        marquage_m0 (star_map, guide)
        r = resultat_identification(star_map)

        if (r>rmax) :
            rmax = r
            best_star_map = [e.new_coord(e.get_abs(), e.get_ord()) for e in star_map]
            for b, e in zip(best_star_map, star_map):
                b.set_sguide(e.get_sguide())

    #Associer coordonnées étoiles photos avec numéro étoile réelle
res = []

for m0 in best_star_map :
    num_guide = m0.get_sguide()

    #Garder uniquement les étoiles associées au guide
    if (num_guide == -1) :
        continue

    idx = m0.get_idx()
    m0_init = etoiles2D[idx]
    coord_init = (m0_init.get_abs(), m0_init.get_ord())

    res.append((num_guide, coord_init))


for (num_guide, (x,y)) in res :
    print("Etoile " + str(num_guide) + " : coordonnées " +str(x)+", "+str(y))

print("\n")

for e in etoiles2D :
    print ("Etoile " + str(e.get_idx()) + " : coordonnées " +str(e.get_abs())+", "+str(e.get_ord()))
