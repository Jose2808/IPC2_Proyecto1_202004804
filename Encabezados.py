from Nodos import NodoC

class columnas:
    def __init__ (self):
        self.primero = None
        self.ultimo = None
    
    def nuevoNodo(self, nodo):
        if self.primero == None:
            self.primero = nodo
            self.ultimo = nodo
        else:
            if nodo.x < self.primero.x:
                nodo.derecha = self.primero
                self.primero.izquierda = nodo
                self.primero = nodo
            else:
                puntero = self.primero
                while puntero.derecha is not None:
                    if nodo.x < puntero.derecha.x:
                        nodo.izquierda = puntero
                        nodo.derecha = puntero.derecha
                        puntero.derecha = nodo
                        puntero.derecha.izquierda = nodo
                        break
                    puntero = puntero.derecha
                if puntero.derecha == None:
                    puntero.derecha = nodo
                    nodo.izquierda = puntero
                    self.ultimo = nodo

    def buscar(self, x):
        puntero = self.primero
        while puntero is not None:
            if puntero.x == x:
                return puntero
            puntero = puntero.derecha
        return None

    def recorrer(self):
        puntero = self.primero
        while puntero != None:
            print("Columna en x: ", puntero.x)
            puntero = puntero.derecha

    def mayorX(self):
        puntero = self.primero
        if puntero is not None:
            while puntero.derecha is not None:
                puntero = puntero.derecha
            return puntero.x
        else:
            return 0

    def menorX(self):
        return self.primero

class filas:
    def __init__ (self):
        self.primero = None
        self.ultimo = None
    
    def nuevoNodo(self, nodo):
        if self.primero == None:
            self.primero = nodo
            self.ultimo = nodo
        else:
            if nodo.y < self.primero.y:
                nodo.abajo = self.primero
                self.primero.arriba = nodo
                self.primero = nodo
            else:
                puntero = self.primero
                while puntero.abajo is not None:
                    if nodo.y < puntero.abajo.y:
                        nodo.abajo = puntero.abajo
                        nodo.arriba = puntero
                        puntero.abajo = nodo
                        puntero.abajo.arriba = nodo
                        break
                    puntero = puntero.abajo
                if puntero.abajo is None:
                    puntero.abajo = nodo
                    nodo.arriba = puntero
                    self.ultimo = nodo

    def buscar(self, y):
        puntero = self.primero
        while puntero is not None:
            if puntero.y == y:
                return puntero
            puntero = puntero.abajo
        return None

    def recorrer(self):
        puntero = self.primero
        while puntero is not None:
            print("Fila en la posición: ", puntero.y)
            puntero = puntero.abajo
        return None

    def mayorY(self):
        puntero = self.primero
        if puntero is not None:
            while puntero.abajo is not None:
                puntero = puntero.abajo
            return puntero.y
        else:
            return 0

    def menorY(self):
        return self.primero


