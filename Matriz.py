from Nodo import Nodo
from Encabezados import columnas, filas
from Nodos import NodoC, NodoF, NodoM

class Matriz:
    def __init__ (self):
        self.cabecera_filas = filas()
        self.cabecera_columnas = columnas()
    
    def agregarNodo(self, dato, x, y):
        nodo_nuevo = NodoM(dato, x, y)
        encabezado_fila = self.cabecera_filas.buscar(y)

        if encabezado_fila == None:
            encabezado_fila = NodoF(y)
            encabezado_fila.acceso = nodo_nuevo
            self.cabecera_filas.nuevoNodo(encabezado_fila)
        else:
            if nodo_nuevo.x < encabezado_fila.acceso.x:
                nodo_nuevo.derecha = encabezado_fila.acceso
                encabezado_fila.acceso.izquierda = nodo_nuevo
                encabezado_fila.acceso = nodo_nuevo
            else:
                
                puntero = encabezado_fila.acceso
                while puntero.derecha is not None:
                    if nodo_nuevo.x < puntero.derecha.x:
                        nodo_nuevo.derecha = puntero.derecha
                        nodo_nuevo.izquierda = puntero
                        puntero.derecha.izquierda = nodo_nuevo
                        puntero.derecha = nodo_nuevo
                        break
                    puntero = puntero.derecha

                if puntero.derecha is None:
                    puntero.derecha = nodo_nuevo
                    nodo_nuevo.izquierda = puntero

        encabezado_columna = self.cabecera_columnas.buscar(x)

        if encabezado_columna == None:
            encabezado_columna = NodoC(x)
            encabezado_columna.acceso = nodo_nuevo
            self.cabecera_columnas.nuevoNodo(encabezado_columna)
        else:
            if nodo_nuevo.y < encabezado_columna.acceso.y:
                nodo_nuevo.abajo = encabezado_columna.acceso
                encabezado_columna.acceso.arriba = nodo_nuevo
                encabezado_columna.acceso = nodo_nuevo
            else:
                puntero = encabezado_columna.acceso
                while puntero.abajo is not None:
                    if nodo_nuevo.y < puntero.abajo.y:
                        nodo_nuevo.abajo = puntero.abajo
                        nodo_nuevo.arriba = puntero
                        puntero.abajo.arriba = nodo_nuevo
                        puntero.abajo = nodo_nuevo
                        break
                    puntero = puntero.abajo
                if puntero.abajo == None:
                    puntero.abajo = nodo_nuevo
                    nodo_nuevo.arriba = puntero

    def mostrarColumnas(self):
        encabezado_columna = self.cabecera_columnas.primero
        while encabezado_columna is not None:
            puntero = encabezado_columna.acceso
            print("\n Columna", puntero.x)
            print("Fila         Valor")
            while puntero is not None:
                print(puntero.y, "        ", puntero.data)
                puntero = puntero.abajo
            encabezado_columna = encabezado_columna.derecha
        print("--------------FIN------------")




