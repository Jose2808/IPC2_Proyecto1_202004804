class NodoM:
    def __init__ (self, data, x, y):
        self.data = data
        self.x = x
        self.y = y
        self.visitado = False
        self.arriba = None
        self.abajo = None
        self.derecha = None
        self.izquierda = None
        self.nodoPadre = None

    def setData(self, nodo):
        if self.nodoPadre == None:
            self.nodoPadre = nodo
            self.data = self.data + self.nodoPadre.nodo.data
        elif self.data < ((self.data - self.nodoPadre.nodo.data) + nodo.nodo.data):
            pass
        else:
            self.data = self.data - self.nodoPadre.nodo.data
            self.data = self.data + nodo.nodo.data
            self.nodoPadre = nodo

    def getData(self):
        return self.data

class NodoC:
    def __init__ (self, x):
        self.x = x
        self.derecha = None
        self.izquierda = None
        self.acceso = None

class NodoF:
    def __init__ (self, y):
        self.y = y
        self.arriba = None
        self.abajo = None
        self.acceso = None

class NodoN:
    def __init__ (self, nodo):
        self.siguiente = None
        self.nodo = nodo

class NodoP:
    def __init__ (self, nodo):
        self.siguiente = None
        self.nodo = nodo
