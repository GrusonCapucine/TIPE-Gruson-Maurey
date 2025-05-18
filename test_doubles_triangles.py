from double_triangles import *

etoiles = [
    Etoile2D(1, 2, 5),
    Etoile2D(4, 4, 3),
    Etoile2D(-1, 2, 4),
    Etoile2D(5, 1, 2),
    Etoile2D(7, 3, 4)
]

db_triangles = calcul_doubles_triangles(etoiles, false)

for i in range (len(db_triangles)):
    print(str(db_triangles[i].get_ref())+"\n")
