class Etoile3D :

    def __init__(self, decl, asc, num, magn):
        self.__decl = decl
        self.__asc = asc
        self.__num = num
        self.__magn = magn

    #Accesseurs
    def get_asc (self):
        return self.__asc

    def get_decl(self):
        return self.__decl

    def get_num(self):
        return self.__num

    def get_magn(self):
        return self.__magn

    #Pas de transformateur

class Etoile2D :

    def __init__(self, x, y, magn=None, idx=0) :
        self.__x = x
        self.__y = y
        self.__sguide = -1
        self.__magn = magn
        #Pour associer les etoiles2D avant et après changement de base
        self.__idxetoile2D = idx

    #Accesseurs
    def get_abs (self):
        return self.__x

    def get_ord(self):
        return self.__y

    def get_sguide(self):
        return self.__sguide

    def get_magn(self):
        return self.__magn

    def get_idx (self) :
        return self.__idxetoile2D

    def new_coord (self, x, y):
        #Création d'une nouvelle étoile dans le nouveau système
        new_star = Etoile2D(x, y, self.__magn, self.__idxetoile2D)
        new_star.set_sguide(self.__sguide)
        return new_star

    #Transformateur
    def set_sguide(self, s):
        self.__sguide = s


class DoubleTriangle :

    def __init__(self, a, b, c, d, e, ref):
        self.__c1 = a
        self.__c2 = b
        self.__c3 = c
        self.__c4 = d
        self.__c5 = e
        self.__a1 = None
        self.__a2 = None
        self.__a3 = None
        self.__a4 = None
        self.__a5 = None
        self.__a6 = None
        self.__ref = ref

    #Accesseurs
    def get_length(self):
        return (self.__c1, self.__c2, self.__c3, self.__c4, self.__c5)

    def get_angles(self):
        return (self.__a1, self.__a2, self.__a3, self.__a4, self.__a5, self.__a6)

    def get_ref(self):
        return self.__ref

    #Transformateur
    def new_angles(self, na1, na2, na3, na4, na5, na6):
        self.__a1 = na1
        self.__a2 = na2
        self.__a3 = na3
        self.__a4 = na4
        self.__a5 = na5
        self.__a6 = na6
