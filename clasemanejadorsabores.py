import csv
from clasesabor import  sabor

class manejadorsabor:
   __sabores = []
   def __init__(self):
    archivo = open('sabores.csv')
    reader = csv.reader(archivo, delimiter=(','))
    for fila in reader:
     sab = sabor(fila[0], fila[1], fila[2])
     self.__sabores.append(sab)
    archivo.close()

   def a(self):
     for x in range(0,len(self.__sabores)):
         print(self.__sabores[x].nombre())

   @classmethod
   def sabo(cls,x):
    return cls.__sabores[x]
   @classmethod
   def suma(cls,x):
       cls.__sabores[x].vendi()

   def vendidos(self):
       self.__sabores.sort()
       for x in range(0,len(self.__sabores)):
        print('sabor:' + self.__sabores[x].nombre())
        print('cantidad vendidas: ' + str(self.__sabores[x].ven()))


