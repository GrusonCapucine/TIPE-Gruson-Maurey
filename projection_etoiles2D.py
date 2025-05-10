from classes import *
import math

def distance2D(u1, u2):
    x1, y1 = u1
    x2, y2 = u2
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def normalise2D(u):
    norm = math.sqrt(u[0]**2 + u[1]**2)
    return (u[0]/norm, u[1]/norm)

def pdt_scal2D(u, v):
    return u[0]*v[0] + u[1]*v[1]

def etoile_plus_proche2D (etoiles, ref, m0) :
    dist_min = float('inf')
    etoile = None

    for e in etoiles :
        if (e!=ref) :
            temp = (e.get_abs(), e.get_ord())
            d = distance2D (temp, m0)
            if (d<dist_min) :
                dist_min = d
                etoile = temp
    return etoile


def calcul_projection_avec_base_2D (etoiles, ref_index):
    etoiles_proj = []
    ref = etoiles[ref_index]

    m0 = (ref.get_abs(), ref.get_ord())
    m1 = etoile_plus_proche2D(etoiles, ref, m0)

    u = (m1[0]-m0[0], m1[1]-m0[1])
    u = normalise2D(u)
    v = (-u[1], u[0]) #Vecteur orthogonal

    proj_ref = Etoile2D(0, 0, ref.get_magn())
    etoiles_proj.append(proj_ref)

    for e in etoiles:
        if (e!=ref) :
            mx, my = e.get_abs(), e.get_ord()
            dx, dy = mx - m0[0], my - m0[1]
            d = (dx, dy)
            x = pdt_scal2D(d, u)
            y = pdt_scal2D(d, v)

            proj = Etoile2D(x, y, e.get_magn())
            etoiles_proj.append(proj)

    return etoiles_proj, u, v, m0


def calcul_projection_2D (etoiles, ref_index):
    etoiles2D, _, _, _ = calcul_projection_avec_base_2D (etoiles, ref_index)
    return etoiles2D
