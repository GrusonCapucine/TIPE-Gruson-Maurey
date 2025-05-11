from classes import *
from random import randint


def random_star (etoiles) :
    i = randint (0, len(etoiles)-1)
    return etoiles[i]


def nearest_stars (m0, etoiles):
    assert (len(etoiles) >= 5)

    plus_proches = []

    for e in etoiles:
        if (e==m0) :
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

    return  plus_proches


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

    triangle = DoubleTriangle(c01, c02, c03, c12, c23)
    a1, a2, a3 = al_kashi(c01, c12, c02)
    a4, a5, a6 = al_kashi(c02, c03, c23)
    triangle.new_angles(a1, a2, a3, a4, a5, a6)

    return triangle


def calcul_doubles_triangles(ref, etoiles):
    triangles = []
    m0 = (ref.get_abs(), ref.get_ord())

    plus_proches = nearest_stars(m0, etoiles)
    #Tri d'abord sur la distance
    plus_proches.sort()

    proches = [e for (_, e) in plus_proches]

    m1=proches[0]
    m2=proches[1]
    m3 = proches[2]
    m4 = proches [3]

    #Première vue {m0, m1, m2} et {m0, m2, m3}
    triangles.append (create_triangle(m0, m1, m2, m3))
    #Deuxième vue {m0, m2, m3} et {m0, m3, m4}
    triangles.append (create_triangle(m0, m2, m3, m4))

    return triangles
