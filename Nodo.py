class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.m = 0
        self.n = 0
        self.inicioX = 0
        self.inicioY = 0
        self.finalX = 0
        self.finalY = 0
        self.mapa = None
        self.mapa_algoritmo = None
        self.siguiente = None
        

    def setMapa(self, mapa):
        self.mapa = mapa

    def setMapaAlgoritmo(self, mapa):
        self.mapa_algoritmo = mapa
    
    def setSiguiente(self, siguiente):
        self.siguiente = siguiente
    
    def setDato(self, dato):
        self.dato = dato

    def setInicioX(self, x):
        self.inicioX = x

    def setInicioY(self, y):
        self.inicioY = y

    def setFinalX(self, x):
        self.finalX = x

    def setFinalY(self, y):
        self.finalY = y

    def getInicioX(self):
        return self.inicioX

    def getDato(self):
        return self.dato

    def getSiguiente(self):
        return self.siguiente

    def getMapa(self):
        return self.mapa

    def getMapaAlgoritmo(self):
        return self.mapa_algoritmo

    