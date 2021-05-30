

from clasehelado import helado
from clasemanejadorsabores import manejadorsabor
from clasesabor import sabor

class manejadorhelados:
    __helados = []

    def __init__(self):
        self.__helados = []

    def añadir(self):
     print('ingresar gramos que se quiere')
     print('100gr, 150 gr, 250 gr, 500 gr y 1000gr')
     gramos = input()
     helad = helado(gramos)
     print('cuantos sabores desea?')
     cant = int(input())
     print('ingresar sabor/es que se desea')
     print('chocolate-1/frutilla-2/vainilla-3/dulde de leche-4/gridito-5/granizado-6')
     for x in range(0,cant):
      sabor = int(input())
      helad.aña(manejadorsabor.sabo(sabor-1))
      manejadorsabor.suma(sabor-1)


     self.__helados.append(helad)

    def mostrar(self):
        for x in range(0,len(self.__helados)):
         print('Gramos :' + self.__helados[x].gram())
         print('sabor/es:')
         self.__helados[x].sab()

    def estimar(self):
        print('chocolate-1/frutilla-2/vainilla-3/dulde de leche-4/gridito-5/granizado-6')
        print('ingresar numero de helado')
        total = 0
        num = input()
        for x in range(0,len(self.__helados)):
           if self.__helados[x].band(num) == True:
               total = self.__helados[x].tot() + total
               #print(total)
        print(total)

    def hela(self):
        sabo = []
        print('100gr, 150 gr, 250 gr, 500 gr y 1000gr')
        print('elgir tipo de helado')
        p = input()
        for x in range(0,len(self.__helados)):
            if self.__helados[x].gram() == p:
             list = []
             list = self.__helados[x].sabor()
             for g in range(0,len(list)):
              if not list[g].nombre() in sabo:
                 sabo.append(list[g].nombre())
        print(sabo)
