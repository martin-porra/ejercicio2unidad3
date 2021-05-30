from clasemanejadorsabores import  manejadorsabor
from clasemanejadorhelado import  manejadorhelados
import  os

def menu():
 os.system('cls')
 print ("Selecciona una opción")
 print ("\t1 - añadir sabor")
 print ("\t2 - calcular gramos vendidos del sabor")
 print ("\t3 - sabores mas vendidos")
 print('"\t4 - elegir helado para saber que sabores se eligio ')

if __name__ == '__main__':
 sabores = manejadorsabor()
 helados = manejadorhelados()
 a = True
 while a == True:
  menu()
  opcion = input()
  if opcion == '1':
   helados.añadir()
  elif opcion == '2':
   helados.estimar()
  elif opcion == '3':
   sabores.vendidos()
  elif opcion == '4':
    helados.hela()
  else:
   a = False
   print('opcion incorrecta')
 print('programa terminado')


