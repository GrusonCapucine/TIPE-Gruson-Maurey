from systeme_boites import *
from projection_etoiles3D import *
from projection_etoiles2D import *
from traitement_image import *
from utilisation_csv import *

def calcul_vues (photo, catalogue_csv) :
    coord_photo = detect_stars(photo)
    etoiles2D = coord_to_etoile2D(coord_photo)
    catalogue = e3D_from_csv(catalogue_csv)
    best_star_map = []
    rmax = -1

    print(len(etoiles2D))
    print(len(catalogue))
    #Recherche de la meilleure vue
    for i in range (len(etoiles2D)):
        #star_map = calcul_projection_2D(etoiles2D, i)

        for j in range (len(catalogue)):
            print("num boucle :" +str(i) + " " +str(j))
            star_map = calcul_projection_2D(etoiles2D, i)
            guide = calcul_projection_3D(catalogue, j)

            marquage_m0 (star_map, guide)
            for m0 in star_map :
                print(m0.get_idx(), m0.get_sguide())

            r = resultat_identification(star_map)
            print ("Res : " +str(r))
            print ("\n")

            if (r>rmax) :
                rmax = r
                best_star_map = [e.new_coord(e.get_abs(), e.get_ord()) for e in star_map]
                for b, e in zip(best_star_map, star_map):
                    b.set_sguide(e.get_sguide())

    #Associer coordonnées étoiles photos avec numéro étoile réelle
    res = []

    for m0 in best_star_map :
        num_guide = m0.get_sguide()

        if (num_guide == -1) :
            continue

        idx = m0.get_idx()
        m0_init = etoiles2D[idx]
        coord_init = (m0_init.get_abs(), m0_init.get_ord())

        res.append((num_guide, coord_init))

    return res
