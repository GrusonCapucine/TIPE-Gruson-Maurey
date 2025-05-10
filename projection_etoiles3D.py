from classes import *
import math

def distance (u1, u2) :
    x1,y1,z1 = u1
    x2,y2,z2 = u2
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)

    
def conv_spher_cart (asc, decl) :
    x = math.cos(asc) * math.cos(decl)
    y = math.sin(asc) * math.cos(decl)
    z = math.sin(decl)
    return (x, y, z)


def pdt_vect (u, v) :
    return ( u[1] * v[2] - u[2] * v[1],
             u[2] * v[0] - u[0] * v[2],
             u[0] * v[1] - u[1] * v[0]
            )


def pdt_scal (u, v):
    x1,y1,z1 = u
    x2,y2,z2 = v
    return x1*x2 + y2*y1 + z1*z2


def normalise(u) :
    n = distance (u, (0,0,0))
    return tuple (c/n for c in u)

def projection_plus_proche (catalogue, ref, c0):
    dist_min = float('inf')
    proj = None

    for e in catalogue :
        if (e!=ref) :
            temp = conv_spher_cart(e.get_asc(), e.get_decl())
            d = distance (temp, c0)
            if (d < dist_min):
                dist_min = d
                proj = temp

    return proj


def nouvelle_base (c0, c1):
    #Vecteur C0C1 (axe X)
    u = tuple(c1[i] - c0[i] for i in range(3))

    #Vecteur C0D0 (axe Z)
    w=c0

    #Vecteur C0A (axe Y)
    v = pdt_vect (w,u)

    #Normalisation des vecteurs
    norme_u = distance (u,(0,0,0))
    norme_v = distance (v,(0,0,0))

    u_norm = normalise(u)
    v_norm = normalise(v)

    return u_norm, v_norm


#Création fonction avec plusieurs sorties pour les tests
def calcul_projection_avec_base (catalogue, ref_index) :
    etoiles2D = []
    ref = catalogue[ref_index]

    #Coordonnées cartésiennes étoile de référence
    c0 = conv_spher_cart(ref.get_asc(), ref.get_decl())

    #Construction base
    c1 = projection_plus_proche(catalogue, ref, c0)
    u, v = nouvelle_base(c0, c1)
    w = normalise(c0)

    for e in catalogue:
        #Vecteur v_star position de l'étoile (rayon)
        v_star = conv_spher_cart(e.get_asc(), e.get_decl())

        #Produit scalaire entre v et w
        pdt = pdt_scal (v_star, w)

        if (pdt > 0 and e!=ref) : #Rayon non parallèle ou opposé au plan tangent
                                  #Etoile réf à traiter à part
            t = 1 / pdt
            px, py, pz = t*v_star[0], t*v_star[1], t*v_star[2]

            #Vecteur d déplacement étoile projétée et référence
            dx, dy, dz = px-w[0], py-w[1], pz-w[2]
            d =(dx,dy,dz)

            #Coordonnées dans la base (u, v)
            x = pdt_scal (d, u)
            y = pdt_scal (d, v)

            #Création de l'étoile2D
            proj = Etoile2D(x, y, e.get_magn())
            proj.set_sguide(e.get_num())
            etoiles2D.append(proj)

    proj_ref = Etoile2D(0, 0, ref.get_magn())
    proj_ref.set_sguide(ref.get_num())
    etoiles2D.append(proj_ref)

    return etoiles2D, u, v, w, c0

def calcul_projection_3D (catalogue, ref_index):
    etoiles2D, _, _, _, _ = calcul_projection_avec_base (catalogue, ref_index)
    return etoiles2D
