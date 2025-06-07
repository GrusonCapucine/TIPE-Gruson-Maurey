from comparaison_triangles import *

def marquage_m0(star_map, guide):
    scores = calcul_sj(star_map, guide)
    asso = assos_Ds_de_M(scores)

    for m0 in asso.keys():
        xm, ym = m0.get_abs(), m0.get_ord()
        ds = asso[m0]  # Liste des étoiles D du guide avec des triangles proches

        best_d0 = None
        best_magn = float('inf')

        for d0 in ds:
            xd, yd = d0.get_abs(), d0.get_ord()
            numd = d0.get_sguide()

            # Si les étoiles entrent dans la même "boîte"
            if abs(xd - xm) <= 0.1 and abs(yd - ym) <= 0.1:
                magn_d0 = d0.get_magn()

                # Comparaison des magnitudes
                if magn_d0 < best_magn:
                    best_d0 = d0
                    best_magn = magn_d0

        if best_d0 is not None:
            m0.set_sguide(best_d0.get_sguide())
        else :
            m0.set_sguide(-1)

    return star_map



def resultat_identification (star_map) :
    r = 0
    for m0 in star_map :
        if (m0.get_sguide() != -1) :
            r += 1
    return r
