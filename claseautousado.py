from claseauto import auto
from datetime import date
class autousado(auto):
    __patente = ''
    __año = 0
    __kilometraje = 0

    def __init__(self,modelo,cantP,color,precio,marca,pate,anio,kili):
        super().__init__(modelo,cantP,color,precio,marca)
        self.__patente = pate
        self.__año = anio
        self.__kilometraje = kili
    def mostra(self):
        self.mostrar()
        print('patente: '+self.__patente)
        print('año: '+ str(self.__año))
        print('kilometraje: '+ str(self.__kilometraje))

    def pate(self):
        return self.__patente

    def calcPrecioVenta(self):
        anioActual = date.today().year
        antiguedad = anioActual - self.__año
        precioBase = super().precio()
        importe = precioBase * (1 - 0.01 * antiguedad)
        if self.__kilometraje > 100000:
            importe -= 0.02 * precioBase
        return importe
    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=None)
        dPadre = super().toJSON()
        dPadre['patente'] = self.__patente
        dPadre['anio'] = self.__año
        dPadre['kilometraje'] = self.__kilometraje
        d['__atributos__'] = dPadre
        return d