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

    def __init__(self, x, y, magn) :
        self.__x = x
        self.__y = y
        self.__magn = magn
        self.__sguide = None

    #Accesseurs
    def get_abs (self):
        return self.__x

    def get_ord(self):
        return self.__y

    def get_sguide(self):
        return self.__sguide

    def get_magn(self):
        return self.__magn

    def new_coord (self, x, y):
        #Création d'une nouvelle étoile dans le nouveau système
        new_star = Etoile2D(x, y, self.__magn)
        new_star.set_sguide(self.__sguide)
        return new_star

    #Transformateur
    def set_sguide(self, s):
        self.__sguide = s


class DoubleTriangle :

    def __init__(self, a, b, c):
        self.__c1 = a
        self.__c2 = b
        self.__c3 = c
        self.__a1 = None
        self.__a2 = None
        self.__a3 = None

    #Accesseurs
    def get_length(self):
        return (self.__c1, self.__c2, self.__c3)

    def get_angles(self):
        return (self.__a1, self.__a2, self.__a3)

    #Transformateur
    def new_angles(self, na1, na2, na3):
        self.__a1 = na1
        self.__a2 = na2
        self.__a3 = na3
