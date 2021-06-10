class Nodo:
    __objeto = None
    __siguiente =   None
    def __init__(self,obj):
        self.__objeto = obj
        self.__siguiente = None
    def setsiguiente(self,siguiente):
        self.__siguiente = siguiente
    def getsiguiente(self):
        return self.__siguiente
    def getdato(self):
        return self.__objeto