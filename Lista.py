from Nodo import Nodo
from Nodos import NodoM, NodoN, NodoP
class Lista:
    def __init__(self):
        self.inicio = None

    def insertar(self, dato):
        #nuevo_nodo = Nodo(dato)
        nuevo_nodo = dato
        if self.inicio == None:
            self.inicio = nuevo_nodo
        else:
            puntero = self.inicio
            while puntero.siguiente is not None:
                puntero = puntero.siguiente
            puntero.siguiente = nuevo_nodo

    def verificarTerreno(self, terreno):
        if self.inicio is None:
            print("La lista de terrenos se encuentra vacía")
        else:
            puntero = self.inicio
            while puntero.siguiente is not None :
                if puntero.getDato() == terreno:
                    break
                puntero = puntero.siguiente
            if puntero.getDato() == terreno:
                return puntero
            else:
                return None
            #puntero = puntero.siguiente

    
    def asignarMapa(self, terreno, mapa):
        puntero = self.inicio
        while puntero.siguiente is not None:
            if puntero.dato == terreno:
                break
            puntero = puntero.siguiente
        puntero.setMapa(mapa)

    def asignarMapaAlgoritmo(self, terreno, mapa):
        puntero = self.inicio
        while puntero.siguiente is not None:
            if puntero.dato == terreno:
                break
            puntero = puntero.siguiente
        puntero.setMapaAlgoritmo(mapa)
    
    def recorrer(self):
        puntero = self.inicio
        while puntero.siguiente is not None:
            print(puntero.getDato() +"---->"+puntero.siguiente.getDato())
            puntero = puntero.siguiente


class ListaNodos:
    def __init__ (self):
        self.inicio = None
    
    def insertarNodo(self, nodo):
        nodo_nuevo = NodoN(nodo)
        if self.inicio == None:
            self.inicio = nodo_nuevo
        else:
            puntero = self.inicio
            while puntero.siguiente is not None:
                puntero = puntero.siguiente
            puntero.siguiente = nodo_nuevo

    def recorrer(self):
        puntero = self.inicio
        while puntero is not None:
            print("x: ", puntero.nodo.x, "y: ", puntero.nodo.y, "combustible: ", puntero.nodo.data)
            puntero = puntero.siguiente

class Lista_prioridad:
    def __init__ (self):
        self.inicio = None
        self.final = None

    def analizarNodo(self, nodo):
        nuevo_nodo = NodoP(nodo)
        if self.inicio == None:
            self.inicio = nuevo_nodo
            
        else:
            puntero = self.inicio
            while puntero.siguiente is not None:
                if puntero.nodo.x == nuevo_nodo.nodo.x:
                    if puntero.nodo.y == nuevo_nodo.nodo.y:
                        if nuevo_nodo.nodo.data > puntero.nodo.data:
                            break
                        elif nuevo_nodo.nodo.data == puntero.nodo.data:
                            break
                        elif nuevo_nodo.nodo.data < puntero.nodo.data:
                            self.eliminarNodo(puntero)
                            self.insertar(nuevo_nodo)
                            break
                puntero = puntero.siguiente
            if puntero.siguiente is None:
                self.insertar(nuevo_nodo)

    def pop(self):
        temp = self.inicio
        if self.inicio.siguiente is not None:
            self.inicio = temp.siguiente
        return temp

    def eliminarNodo(self, nodo):
        puntero = self.inicio
        if self.inicio == nodo:
            temp = self.inicio 
            self.inicio = nodo
            self.inicio.siguiente = nodo.siguiente
            del temp

        while puntero.siguiente is not None:
            if puntero.siguiente.nodo == nodo:
                temp = puntero.siguiente
                puntero.siguiente = temp.siguiente
                del temp


    
    #def insertar(self, nodo):
        #nodo = NodoP(nodo_nuevo)
        #if self.inicio == None:
            #self.inicio = nodo
        #else:
            #if nodo.nodo.data < self.inicio.nodo.data:
                #nodo.siguiente = self.inicio
                #self.inicio = nodo
            #else:
                #puntero = self.inicio
                #while puntero.siguiente is not None:
                    #if nodo.nodo.data < puntero.siguiente.nodo.data:
                        #nodo.siguiente = puntero.siguiente
                        #puntero.siguiente = nodo
                        #break
                    #puntero = puntero.siguiente

                #if puntero.siguiente is None:
                    #puntero.siguiente = nodo

    def existe(self, nodo):
        puntero = self.inicio
        while puntero is not None:
            if puntero == nodo:
                return True 
            puntero = puntero.siguiente
        if puntero is None:
            return False


    def insertar(self, nodo):
        nodo_nuevo = NodoP(nodo)
        if self.inicio == None:
            self.inicio = nodo_nuevo
        
        elif self.existe(nodo_nuevo):
            pass
        elif nodo_nuevo.nodo.data < self.inicio.nodo.data:
            nodo_nuevo.siguiente = self.inicio
            self.inicio = nodo_nuevo
        else:
            puntero = self.inicio
            while puntero.siguiente is not None:
                if puntero.nodo.x == nodo_nuevo.nodo.x:
                    if puntero.nodo.y == nodo_nuevo.nodo.y:
                        break
                if nodo_nuevo.nodo.data <= puntero.siguiente.nodo.data:
                    nodo_nuevo.siguiente = puntero.siguiente
                    puntero.siguiente = nodo_nuevo
                    break
                puntero = puntero.siguiente
            if puntero.siguiente is None:
                puntero.siguiente = nodo_nuevo
                
            
    def recorrer(self):
        puntero = self.inicio
        while puntero is not None:
            print("x: ", puntero.nodo.x, "y: ", puntero.nodo.y, "combustible: ", puntero.nodo.data)
            puntero = puntero.siguiente




