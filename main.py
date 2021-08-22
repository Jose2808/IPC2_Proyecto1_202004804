from graphviz.backend import view
from graphviz.dot import Graph
from Matriz import Matriz
from Lista import Lista, Lista_prioridad
from Nodo import Nodo
from Matriz import Matriz
import xml.etree.ElementTree as xml
from graphviz import Graph

end_program = False
terrenos = Lista()
terreno_actual = Matriz()
terreno_actual_aux = Matriz()

def carga():
    #respuesta = input("Ingrese la ruta del archivo a procesar\n")
    objetoTree = xml.parse("prueba2.xml")
    root = objetoTree.getroot()
    for terreno in root.findall("terreno"):
        terreno_actual = Nodo(terreno.get("nombre"))
        #terrenos.insertar(terreno.get("nombre"))
        terreno_actual.m = int(terreno.get("m"))
        terreno_actual.n = int(terreno.get("n"))
        mapa = Matriz()
        for posicionI in terreno.findall("posicioninicio"):
            for x in posicionI.findall("x"):
                terreno_actual.inicioX = int(x.text)
                #print(terreno_actual.inicioX)
            for y in posicionI.findall("y"):
                terreno_actual.inicioY = int(y.text)
                #print(y.text)
        for posicionF in terreno.findall("posicionfin"):
            for x in posicionF.findall("x"):
                terreno_actual.finalX = int(x.text)
                #print(x.text)
            for y in posicionF.findall("y"):
                terreno_actual.finalY = int(y.text)
                #print(y.text)
        for posiciones in terreno.findall("posicion"):
            #if int(posiciones.get("x")) > terreno_actual.n or int(posiciones.get("y")) > terreno_actual.m:
                #continue
            mapa.agregarNodo(int(posiciones.text), int(posiciones.get("x")), int(posiciones.get("y" )))
            #print("Posicion x: " + posiciones.get("x"))
            #print("Posicion y: " + posiciones.get("y"))
            #print("Coste de combustible: " + posiciones.text)
        if mapa.mayorX() > terreno_actual.n or mapa.mayorY() > terreno_actual.m:
            continue
        terrenos.insertar(terreno_actual)
        #mapa.mostrarColumnas()
        terrenos.asignarMapa(terreno.get("Nombre"), mapa)
        terrenos.asignarMapaAlgoritmo(terreno.get("Nombre"), mapa)

    print("Carga realizada exitosamente")      

def generarGrafico():
    global terreno_actual_aux
    gra = Graph()
    contador = 0
    puntero = terreno_actual_aux.cabecera_columnas.primero.acceso
    while puntero is not None:
        gra.node(str(contador), str(puntero.data))
        contador = contador +1
        puntero = puntero.derecha
    print(terreno_actual_aux.cabecera_columnas.primero.acceso.data)
    gra.render('Machine.gv.pdf', view = True)


def menuPrincipal():
    
    print("Menu Principal:")
    print("\t1. Cargar Archivo")
    print("\t2. Procesar Archivo")
    print("\t3. Escribir Archivo de salida")
    print("\t4. Mostrar Datos del estudiante")
    print("\t5. Generar gráfica")
    print("\t6. Salida")
    print("")
    print("Escriba la opción que desea realizar: ")
    respuesta = input()
 
    if int(respuesta) == 1:
        carga()
    elif int(respuesta) == 2:
        global terreno_actual
        print("Ingrese el nombre del terreno a procesar")
        terreno_res = input()
        nodo_terreno = terrenos.verificarTerreno(terreno_res)
        if nodo_terreno == None:
            print("El terreno que usted ha ingresado no se encuentra en el programa")
        terreno_actual = nodo_terreno.getMapa()
        print("************************************************")
        print("             PROCESANDO TERRENO                 ")
        print("************************************************")
        print("")
        print("")
        lista = Lista_prioridad()
        #terreno_actual.mostrarColumnas()
        nodo_actual = terreno_actual.obtenerNodo(nodo_terreno.inicioX, nodo_terreno.inicioY)
        while ((nodo_actual.nodo.x != nodo_terreno.finalX) or (nodo_actual.nodo.y != nodo_terreno.finalY)):
            vecinos = terreno_actual.obtenerHermanos(nodo_actual.nodo.x, nodo_actual.nodo.y)
            if vecinos.inicio is not None:
                puntero = vecinos.inicio
                while puntero is not None:
                    puntero.nodo.setData(nodo_actual)
                    lista.insertar(puntero.nodo)
                    #print("x: ", puntero.nodo.x, "y: ", puntero.nodo.y, "Combustible: ", puntero.nodo.data)
                    puntero = puntero.siguiente
            nodo_actual.nodo.visitado = True
            #lista.recorrer()
            #print("")
            #print("")
            nodo_actual = lista.pop()
        print(nodo_actual.nodo.data)
        print("************************************************")
        print("        TERRENO PROCESADO EXITOSAMENTE          ")
        print("************************************************")
        print("")
        print("EL COSTO DE COMBUSTIBLE DE LA RUTA MÁS ÓPTIMA ES: ")
        print("Coordenadas    x: ", nodo_actual.nodo.x , "y: ", nodo_actual.nodo.y, "Gasto de combustible: ", nodo_actual.nodo.data)
        print("")
        print("")
    elif int(respuesta) == 3:
        print("Usted ha seleccionado la tercera opción")
    elif int(respuesta) == 4:
        print("José Andrés Montenegro Santos")
        print("202004804")
        print("Introducción a la Programación y Computación 2 sección: A")
        print("Ingeniería en Ciencias y Sistemas")
        print("4to Semestre")
    elif int(respuesta) == 5:
        generarGrafico()
    elif int(respuesta) == 6:
        global end_program
        end_program = True
    
def main():
    menuPrincipal()

while not end_program:
    if __name__ == "__main__":
        main()