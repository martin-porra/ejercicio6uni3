import os
from clasemanejador import manejador
from ObjectEncode import  ObjectEncoder
def menu():
 print('--------------------------------------------------------------')
 print('[1]- Insertar un vehiculo en la coleccion en una posicion determinada.')
 print('[2]- Agregar un vehiculo a la coleccion.')
 print('[3]- Dada una posicion de la Lista: Mostrar por pantalla que tipo de objeto se encuentra almacenado en dicha posicion.')
 print('[4]- Dada la patente de un vehiculo usado, modificar el precio base, y luego mostrar el precio de venta.')
 print('[5]- Mostrar todos los datos, incluido el importe de venta, del vehiculo más económico.')
 print('[6]- Mostrar para todos los vehiculos que la concesionaria tiene a la venta, modelo, cantidad de puertas e importe de venta.')
 print('[7]- Almacenar los objetos de la coleccion Lista en el archivo "vehiculos.json".')
 print('[0]- Salir.')

if __name__ == '__main__':
 maneja = manejador()
 encoder = ObjectEncoder()
 lista = encoder.leerJSONArchivo('autos.json')
 maneja.llenar(lista)
 bande = True
 while bande == True:
  menu()
  op = input('ingresar opcion ')
  if op == '1':
   au = maneja.crear()
   print('ingrese indice a colocar')
   ind = int(input())
   maneja.insertar(au,ind)
  elif op == '2':
   os.system('cls')
   au = maneja.crear()
   maneja.agregar(au)
  elif op == '3':
   i = int(input('ingrese indice: '))
   maneja.mostrarporindice(i)
  elif op == '4':
    aut = maneja.patente()
    aut.modificar()
    impor = aut.calcPrecioVenta()
    print('precio actual: ' + str(impor))
  elif op == '5':
   maneja.autoeconomico()
  elif op == '6':
   maneja.mostrar7()
  elif op == '7':
   lista = maneja.toJSON()
   encoder.guardarJSONArchivo(lista, 'autos.json')
   print('Datos guardados.')
  else:
   print('opcion incorrecto')
   bande = False
 print('Fin')
