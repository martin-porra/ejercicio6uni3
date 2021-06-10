import abc
from abc import ABC
class auto(ABC):
 __modelo = ''
 __cantP =  0
 __color = ''
 __precio = 0
 __marca = ''
 def __init__(self,modelo,cantP,color,precio,marca):
  self.__modelo = modelo
  self.__cantP = cantP
  self.__color = color
  self.__precio = precio
  self.__marca = marca
 def modelo(self):
  return self.__modelo
 def cantp(self):
  return self.__cantP
 def precio(self):
   return self.__precio
 def mostrar(self):
  print('marca: '+self.__marca)
  print('modelo: '+self.__modelo)
  print('cantidadpuertas: '+ str(self.__cantP))
  print('color: ' + self.__color)
  print('precio: ' + str(self.__precio))

 @abc.abstractmethod
 def calcPrecioVenta(self):
  pass

 def modificar(self):
  try:
   print('precio acutal: ' + str(self.__precio))
   print('ingresar precio nuevo')
   precio = int(input())
   self.__precio = precio
   print('precio modificado')
  except ValueError:
   print('Error: El precio base debe ser un entero')

 def toJSON(self):
   d = dict(
    modelo=self.__modelo,
    cantP=self.__cantP,
    color=self.__color,
    precioB=self.__precio,
    marca=self.__marca)
   return d