from Nodo import Nodo
class Lista:
    def __init__(self):
        self.inicio = None

    def insertar(self, dato):
        nuevo_nodo = Nodo(dato)
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


    def recorrer(self):
        puntero = self.inicio
        while puntero.siguiente is not None:
            print(puntero.getDato() +"---->"+puntero.siguiente.getDato())
            puntero = puntero.siguiente



