from projection_etoiles2D import *
import matplotlib.pyplot as plt
import math


# Exemple de données
etoiles = [
    Etoile2D(1, 2, 5),
    Etoile2D(4, 4, 3),
    Etoile2D(-1, 2, 4),
    Etoile2D(5, 1, 2),
    Etoile2D(7, 3, 4)
]
ref_index = 0

# Projection
etoiles_proj, u, v, m0 = calcul_projection_avec_base_2D(etoiles, ref_index)


plt.figure(figsize=(12, 5))

#Coordonnées initiales
plt.subplot(1, 2, 1)
for i in range (len(etoiles)):
    e = etoiles[i]
    c = 'red' if i == ref_index else 'black'
    plt.scatter(e.get_abs(), e.get_ord(), color=c)
    plt.text(e.get_abs()+0.1, e.get_ord()+0.1, f"{i}", fontsize=12)

plt.axis('equal')
plt.title("Coordonnées initiales")
plt.grid ("True")
plt.axhline(0, color='gray', linestyle='--')
plt.axvline(0, color='gray', linestyle='--')


#Coordonnées projetées
plt.subplot(1, 2, 2)
for i in range(len(etoiles_proj)):
    e = etoiles_proj[i]
    c = 'red' if i == ref_index else 'black'
    plt.scatter(e.get_abs(), e.get_ord(), color=c)
    plt.text(e.get_abs()+0.1, e.get_ord()+0.1, f"{i}", fontsize=12)

#Vecteurs u et v depuis origine m0
plt.quiver(0, 0, u[0], u[1], angles='xy', scale_units='xy', scale=1, color='blue', label='u')
plt.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1, color='green', label='v')

plt.legend()
plt.axis('equal')
plt.title("Coordonnées projetées avec base (u, v)")
plt.grid ("True")
plt.axhline(0, color='gray', linestyle='--')
plt.axvline(0, color='gray', linestyle='--')

plt.tight_layout()
plt.show()


print(f"Norme de u : {math.sqrt(u[0]**2 + u[1]**2)}")
print(f"Norme de v : {math.sqrt(v[0]**2 + v[1]**2)}")
