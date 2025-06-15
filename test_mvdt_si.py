from mvdt_si import *

res = calcul_vues("./Photos_etoiles/photo.JPG", "./hygfull.csv")

print (len(res))
for (num_guide, (x,y)) in res :
    print("Etoile " + str(num_guide) + " : coordonnées " +str(x)+", "+str(y))
