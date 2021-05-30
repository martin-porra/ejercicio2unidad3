
class sabor:
    __numero = 0
    __nombre = ''
    __descripcion = ''
    vendidos=0
    def __init__(self,des,nom,num):
        self.__descripcion = des
        self.__nombre = nom
        self.__numero = num

    def nombre(self):
      return  self.__nombre

    def vendi(self):
     self.vendidos = self.vendidos +1

    def ven(self):
     return self.vendidos

    def num(self):
       return  self.__numero

    def __lt__(self, otro):
        bandera = False
        if self.vendidos >= otro.ven():
            bandera = True
        return bandera