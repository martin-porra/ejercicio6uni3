from claseauto import auto
class autonuevo(auto):
    __version = ''

    def __init__(self,modelo,cantP,color,precio,marca,ver):
        super().__init__(modelo,cantP,color,precio,marca)
        self.__version = ver

    def importe(self):
        print('a')
    def mostra(self):
        self.mostrar()
        print('version: '+self.__version)

    def calcPrecioVenta(self):
        precioBase = super().precio()
        importe = float(precioBase) * (1 + 0.1)
        if self.__version == 'full':
            importe += 0.02 * float(precioBase)
        return importe

    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=None)
        dPadre = super().toJSON()
        dPadre['version'] = self.__version
        d['__atributos__'] = dPadre
        return d