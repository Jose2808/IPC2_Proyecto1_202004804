class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.mapa = None

    def setMapa(self, mapa):
        self.mapa = mapa
    
    def setSiguiente(self, siguiente):
        self.siguiente = siguiente
    
    def setDato(self, dato):
        self.dato = dato

    def getDato(self):
        return self.dato

    def getSiguiente(self):
        return self.siguiente

    def getMapa(self):
        return self.mapa