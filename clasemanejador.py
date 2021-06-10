from claselista import  coleccion
from claseautousado import autousado
from claseautonuevo import  autonuevo
from claseauto import auto
import re
import json
class manejador:
    lista = None

    def __init__(self):
     self.__lista = coleccion()
    def llenar(self,ListaVehiculos):
      for i in range(len(ListaVehiculos)):
       dVehiculo = ListaVehiculos[i]
       class_name = dVehiculo.pop('__class__')
       class_=eval(class_name)
       atributos = dVehiculo['__atributos__']
       unVehiculo = class_(**atributos)
       self.__lista.agregarElemento(unVehiculo)

    def mostrar(self):
        self.__lista.mostrarElemento()

    def agregar(self, Auto):
        if isinstance(Auto, auto):
            self.__lista.agregarElemento(Auto)
        else:
            print('Error: No se puede agregar el auto')
    def insertar(self,Auto,indice):
        if isinstance(Auto,auto):
            self.__lista.insertarElemento(Auto,indice)
        else:
            print('Error: no se puede agregar el auto')


    def crear(self):
        print('ingrese datos de auto a añadir')
        model = input('modelo: ')
        cantp = input('canitdad de puertas: ')
        color = input('color: ')
        precio = input('precio: ')
        marca = input('marca: ')
        band = True
        print('el auto es nuevo o usado?')
        while band == True:
         ti = input('si es nuevo ingresar "N" si es usado ingresar "U" ')
         if ti.lower() == 'n':
          vers = input('version: ')
          auto = autonuevo(model, cantp, color, precio, marca, vers)
          band = False
         elif ti.lower() == 'u':
          patente = input('patente: ')
          anios = input('años: ')
          kilo = input('kilometraje: ')
          auto = autousado(model, cantp, color, precio, marca, patente,anios, kilo)
          band = False
         else:
           print('opcion incorrecta')
           ti = input('si es nuevo ingresar "N" si es usado ingresar "U"')
         return auto

    def mostrarporindice(self,indice):
        if indice >  self.__lista.max():
            print('Error: posicion supera la cantidad de componentes')
        elif indice < 1:
            print('Error: posicion invalida')
        else:
          a = self.__lista.mostrarElemento(indice)
          a.mostrar()
    def listar(self):
      self.__lista.listar()
    def patente(self):
        print('patentes de autos usados:')
        print('---------------------------------')
        for auto in self.__lista:
         if isinstance(auto, autousado):
            print(auto.pate())
        print('---------------------------------')
        patente = input('ingresar patente a buscar ')
        bande = True
        for auto in self.__lista:
            if isinstance(auto, autousado):
                if auto.pate() == patente:
                    aut = auto
                    bande = False
        if bande == True:
         print('No se encontro la patente buscada')
        return aut

    def autoeconomico(self):
        menor = 1000000000000000000
        autom = None
        for auto in self.__lista:
            preci = auto.calcPrecioVenta()
            if preci < menor:
                menor = preci
                autom = auto
        print('Los datos del Auto mas economico son:')
        autom.mostra()
        print(menor)
    def mostrar7(self):
        for auto in self.__lista:
            print('--------------------------------------')
            print(auto.modelo())
            print(auto.cantp())
            print(auto.calcPrecioVenta())

    def toJSON(self):
        l = []
        for auto in self.__lista:
            l.append(auto.toJSON())
        return l