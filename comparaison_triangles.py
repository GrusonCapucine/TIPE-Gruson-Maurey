from double_triangles import *
from classes import *


def calcul_sj (star_map, guide):
    triangles_m0s = calcul_doubles_triangles(star_map, false)
    triangles_hk = calcul_doubles_triangles(guide, true)
    scores = {} #Dict qui associe triangle_map -> (score, triangle_guide)

    for f1 in triangles_m0s :
        angles1 = f1.get_angles()
        lenghts1 = f1.get_lenght()
        s_list = []

        for f2 in triangles_hk:
            angles2 = f2.get_angles()
            lenghts2 = f2.get_lenght()

            diff_angles = sum(abs(angles1[i] - angles2[i]) for i in range(6))
            diff_lengths = sum(abs(lengths1[j] - lengths2[j]) for j in range(5))

            s = diff_angles + diff_lengths
            s_list.append((s, f2))

        scores[f1] = s_list

    return scores
