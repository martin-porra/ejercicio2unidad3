from clasesabor import  sabor
class helado:
    __gramos = 0


    def __init__(self,gra):
        self.__gramos = gra
        self.__sabores = []

    def aña(self,sabor):
     self.__sabores.append(sabor)

    def gram(self):
     return  self.__gramos

    def sab(self):
     for x in range(0,len(self.__sabores)):
      print(self.__sabores[x].nombre())

    def band(self,v):
     ban = False
     for x in range(0,len(self.__sabores)):
       if self.__sabores[x].num() == v:
        ban = True
     return ban

    def tot(self):
        to = 0
        can = len(self.__sabores)
        to = int(self.__gramos) / int(can)
        return to

    def sabor(self):
        return self.__sabores