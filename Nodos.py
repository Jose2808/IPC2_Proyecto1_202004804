class NodoM:
    def __init__ (self, data, x, y):
        self.data = data
        self.x = x
        self.y = y
        self.arriba = None
        self.abajo = None
        self.derecha = None
        self.izquierda = None

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

