from double_triangles import *
from classes import *


#Renvoie un dict qui associe :
#triangle_map -> (score, triangle_guide)

def calcul_sj (star_map, guide):
    try :
        triangles_m0s = calcul_doubles_triangles(star_map, False)
        triangles_hk = calcul_doubles_triangles(guide, True)
    except (ZeroDivisionError) as e:
        raise ZeroDivisionError

    scores = {}

    for f1 in triangles_m0s :
        angles1 = f1.get_angles()
        lengths1 = f1.get_length()
        scores[f1] = (float('inf'), None)

        for f2 in triangles_hk:
            angles2 = f2.get_angles()
            lengths2 = f2.get_length()

            diff_angles = sum(abs(angles1[i] - angles2[i]) for i in range(6))
            diff_lengths = sum(abs(lengths1[j] - lengths2[j]) for j in range(5))

            s = diff_angles + diff_lengths
            if (s<scores[f1][0]) : #Score minimal
                scores[f1] = (s, f2)

    return scores


#Sélection des Ks étoiles de triangles_hk à faire


def assos_Ds_de_M (scores) :
    asso = {}
    for (tr_m0, (_, tr_d0)) in scores.items():
        m0 = tr_m0.get_ref()
        d0 = tr_d0.get_ref()
        if (m0 in asso) :
            asso[m0].append(d0)
        else :
            asso[m0] = [d0]
    return asso
