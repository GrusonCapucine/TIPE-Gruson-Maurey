from comparaison_triangles import *

def marquage_m0 (star_map, guide) :
    scores = calcul_sj (star_map, guide)
    asso = assos_Ds_de_M (scores)

    for m0 in asso.keys() :
        xm, ym = m0.get_abs(), m0.get_ord()
        ds = asso[m0] #Liste des étoiles D du guide avec des triangles proches

        for d0 in ds :
            xd, yd = d0.get_abs(), d0.get_ord()
            numd = d0.get_sguide()

            #Si les étoiles entre dans la même "boite"
            if (abs(xd-xm) <= 0.1 and abs(yd-ym) <= 0.1) :
                if (m0.get_sguide() == -1) :
                    m0.set_sguide(numd)

                #Comparaison des magnitudes
                else :
                    magn0 = asso[m0][0].get_magn()
                    magn1 = d0.get_magn()
                    if (magn1 < magn0) :
                        m0.set_sguide(numd)
                    #Sinon garder le numéro de l'autre étoile D

    return star_map


def resultat_identification (star_map) :
    r = 0
    for m0 in star_map :
        if (m0.get_sguide() != -1) :
            r += 1
    return r
