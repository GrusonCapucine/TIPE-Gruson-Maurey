from systeme_boites.py import *
from projection3D import *
from projection2D import *
from traitement_image import *
from utilisation_csv import *

def calcul_vues (photo, catalogue_csv) :
    etoiles2D = etoiles_from_pic(photo)
    catalogue = 3D_from_csv(catalogue_csv)
    best_star_map = []
    rmax = -1

    #Recherche de la meilleure vue
    for i in range (len(etoiles2D)):
        star_map = calcul_projection_2D(etoiles2D, i)
        guide = calcul_projection_3D(catalogue, i)

        marquage_m0 (star_map, guide)
        r = resultat_identification(star_map)

        if (r>rmax) :
            rmax = r
            best_star_map = star_map

    #Associer coordonnées étoiles photos avec numéro étoile réelle
    res = []

    for m0 in best_star_map :
        num_guide = m0.get_sguide()

        idx = m0.get_idx()
        m0_init = etoiles2D[idx]
        coord_init = (m0_init.get_abs(), m0_init.get_ord())

        res.append((num_guide, coord_init))

    return res
