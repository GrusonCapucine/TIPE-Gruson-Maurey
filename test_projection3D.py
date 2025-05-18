from projection_etoiles3D import *

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#Création catalogue
tasc = [math.radians(x) for x in [30, 34, 55, 15, 50, 85, 25, 40, 60, 20]]
tdecl = [math.radians(x) for x in [10, 20, 30, -5, 5, -20, 0, 15, 35, -10]]
catalogue = [Etoile3D(tdecl[i], tasc[i], i, 1.0) for i in range (len(tdecl))]
ref_index = 0
ref_star = catalogue[ref_index]

#Projections des étoiles et base associée
etoiles_2D, u, v, w, c0 = calcul_projection_avec_base(catalogue, ref_index)
etoiles_proj = [(etoiles_2D[i].get_abs(), etoiles_2D[i].get_ord(), etoiles_2D[i].get_sguide()) for i in range(len(etoiles_2D))]


#Affichage
fig = plt.figure(figsize=(12, 6))
ax3d = fig.add_subplot(121, projection='3d') #affichage sphère
ax2d = fig.add_subplot(122)                  #affichage projection

#Sphère
phi, theta = np.mgrid[0:np.pi:30j, 0:2*np.pi:30j]
x = np.sin(phi) * np.cos(theta)
y = np.sin(phi) * np.sin(theta)
z = np.cos(phi)
ax3d.plot_surface(x, y, z, color='lightgray', alpha=0.3)

#Plan tangent
L = 0.5
U, V = np.meshgrid(np.linspace(-L, L, 2), np.linspace(-L, L, 2))
plane = np.array([c0[i] + U*u[i] + V*v[i] for i in range(3)])
ax3d.plot_surface(plane[0], plane[1], plane[2], alpha=0.5, color='orange')

#Placer les étoiles sur la sphère
for e in catalogue:
    x, y, z = conv_spher_cart(e.get_asc(), e.get_decl())
    ax3d.scatter(x, y, z, color='black' if e != ref_star else 'red') #Etoile réf en rouge
    ax3d.text(x, y, z, str(e.get_num()), fontsize=8)                 #Affichage numéro

#Afficher les vecteurs
ax3d.quiver(*c0, *u, length=0.3, color='blue', label='u')
ax3d.quiver(*c0, *v, length=0.3, color='green', label='v')
ax3d.quiver(*c0, *w, length=0.3, color='purple', label='w')

ax3d.set_title("Sphère, plan tangent et étoiles")
ax3d.legend()

#Placer les étoiles 2D sur le plan
for x, y, num in etoiles_proj:
    ax2d.scatter(x, y, color='black' if num != ref_star.get_num() else 'red') #Etoile ref en rouge
    ax2d.text(x+0.01, y+0.01, str(num), fontsize=9)                           #Affichage numéro

#Trace x=0 et y=0 sur le plan 2D
ax2d.axhline(0, color='gray', linestyle='--')
ax2d.axvline(0, color='gray', linestyle='--')

#Légende
ax2d.set_title("Projection 2D des étoiles sur le plan tangent")
ax2d.set_xlabel("u")
ax2d.set_ylabel("v")
ax2d.grid(True)

plt.tight_layout()
plt.show()
