from classes import *

e3 = Etoile3D (50, 40, 0, 10000)
magn3 = e3.get_magn()
print("Magn3 " + str(magn3))

#print(e3.__magn)

e3.__magn = 4
magn2 = e3.get_magn()
print("Magn3 " + str(magn3) + "\n")

e2 = Etoile2D (10, 10, 10)
print("Magn2 " + str(e2.get_magn()))
e2.set_sguide (66)
print("Sguide2 " + str(e2.get_sguide())+"\n")

ne = e2.new_coord(11, 11)
print("nAbs " + str(ne.get_abs()))
print("nMagn " + str(ne.get_magn()))
print("nSguide " + str(ne.get_sguide()))
