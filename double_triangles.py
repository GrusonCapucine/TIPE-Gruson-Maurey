from classes import *
from projection_etoiles2D import *
from random import randint

"""
#Choix arbitraire du nombre d'étoiles de référence à modifier selon les résultats des test
global lamb
lamb = 10
"""


def random_star (etoiles, idx_ref) :
    i = randint (0, len(etoiles)-1)
    while (idx_ref[i]) :
        i = randint (0, len(etoiles)-1)
    idx_ref[i] = True
    return etoiles[i]


def nearest_stars (ref, etoiles):
    assert (len(etoiles) >= 5)

    plus_proches = []
    m0 = (ref.get_abs(), ref.get_ord())

    for e in etoiles:
        if (e==ref) :
            continue

        x, y = e.get_abs(), e.get_ord()
        d = distance2D(m0, (x,y))

        #Si moins de 4 étoiles trouvées
        if len(plus_proches) < 4:
            plus_proches.append((d, e))

        else:
            #Cherche la plus grande distance  parmi les 4
            dist_max, idx_max = -1, -1
            for i in range (len(plus_proches)):
                dist = plus_proches[i][0]
                if dist > dist_max:
                    dist_max = dist
                    idx_max = i

            #Remplace si e est plus proche
            if d < dist_max:
                plus_proches[idx_max] = (d, e)

    return plus_proches


def al_kashi(a, b, c):
    # Formule du cosinus : cos(C) = (a² + b² - c²)/(2ab)
    A = math.acos((b**2 + c**2 - a**2) / (2 * b * c))
    B = math.acos((a**2 + c**2 - b**2) / (2 * a * c))
    C = math.acos((a**2 + b**2 - c**2) / (2 * a * b))
    return A, B, C


def create_triangle(m0, m1, m2, m3):
    p0 = (m0.get_abs(), m0.get_ord())
    p1 = (m1.get_abs(), m1.get_ord())
    p2 = (m2.get_abs(), m2.get_ord())
    p3 = (m3.get_abs(), m3.get_ord())

    c01 = distance2D(p0, p1)
    c02 = distance2D(p0, p2)
    c03 = distance2D(p0, p3)
    c12 = distance2D(p1, p2)
    c23 = distance2D(p2, p3)

    triangle = DoubleTriangle(c01, c02, c03, c12, c23, m0)
    a1, a2, a3 = al_kashi(c01, c12, c02)
    a4, a5, a6 = al_kashi(c02, c03, c23)
    triangle.new_angles(a1, a2, a3, a4, a5, a6)

    return triangle


def calcul_double_vue(ref, etoiles):
    m0 = ref

    plus_proches = nearest_stars(ref, etoiles)
    #Tri sur la distance
    plus_proches.sort(key = lambda x: x[0])

    proches = [e for (_, e) in plus_proches]

    m1=proches[0]
    m2=proches[1]
    m3 = proches[2]
    m4 = proches [3]

    #Première vue {m0, m1, m2} et {m0, m2, m3}
    triangles1 = create_triangle(m0, m1, m2, m3)
    #Deuxième vue {m0, m2, m3} et {m0, m3, m4}
    triangles2 = create_triangle(m0, m2, m3, m4)

    return triangles1, triangles2


def calcul_doubles_triangles (etoiles, est_guide):
    nb_ref = len(etoiles)

    doubles_triangles = []
    idx_ref = [False]*len(etoiles)

    for _ in range (nb_ref) :
        ref = random_star (etoiles, idx_ref)

        t1, t2 = calcul_double_vue(ref, etoiles)
        doubles_triangles.append (t1)
        if (not (est_guide)): #Une seule vue pour les étoiles du guide
            doubles_triangles.append (t2)

    return doubles_triangles
