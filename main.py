from graphviz.backend import view
from graphviz.dot import Graph
from Matriz import Matriz
from Lista import Lista, ListaCamino, ListaNodos, Lista_prioridad
from Nodo import Nodo
from Matriz import Matriz
from colorama import Fore
import xml.etree.ElementTree as ET
import xml.dom.minidom
from graphviz import Graph

end_program = False
terrenos = Lista()
terreno_actual = Matriz()
terreno_actual_aux = Matriz()
camino = ListaNodos()
terreno_res = ''

def carga():
    try:
        respuesta = input("Ingrese la ruta del archivo a procesar\n")
    except:
        print("Ocurrió un error en la lectura del archivo por favor intente de nuevo")
        carga()
    objetoTree = ET.parse(respuesta)
    root = objetoTree.getroot()
    for terreno in root.findall("terreno"):
        terreno_actual = Nodo(terreno.get("nombre"))
        try:
            terreno_actual.m = int(terreno.get("m"))
            terreno_actual.n = int(terreno.get("n"))
        except:
            for dimension in terreno.findall("dimension"):
                for m in dimension.findall("m"):
                    terreno_actual.m = int(m.text)
                for n in dimension.findall("n"):
                    terreno_actual.n = int(n.text)
        mapa = Matriz()
        for posicionI in terreno.findall("posicioninicio"):
            for x in posicionI.findall("x"):
                terreno_actual.inicioX = int(x.text)
            for y in posicionI.findall("y"):
                terreno_actual.inicioY = int(y.text)
        for posicionF in terreno.findall("posicionfin"):
            for x in posicionF.findall("x"):
                terreno_actual.finalX = int(x.text)
            for y in posicionF.findall("y"):
                terreno_actual.finalY = int(y.text)
        for posiciones in terreno.findall("posicion"):
            mapa.agregarNodo(int(posiciones.text), int(posiciones.get("x")), int(posiciones.get("y" )))
        if mapa.mayorX() > terreno_actual.n or mapa.mayorY() > terreno_actual.m:
            continue
        terrenos.insertar(terreno_actual)
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
        global terreno_res
        print("Ingrese el nombre del terreno a procesar")

        #Obtención de la entrada del usuario
        terreno_res = input()
        nodo_terreno = terrenos.verificarTerreno(terreno_res)
        if nodo_terreno == None:
            print("El terreno que usted ha ingresado no se encuentra en el programa")
        terreno_actual = nodo_terreno.getMapa()

        #Algoritmo para encontrar el camino más corto
        print("*************************************************")
        print(" CALCULANDO MEJOR RUTA Y SU COSTE DE COMBUSTIBLE ")
        print("*************************************************")
        print("")
        print("")
        lista = Lista_prioridad()
        nodo_actual = terreno_actual.obtenerNodo(nodo_terreno.inicioX, nodo_terreno.inicioY)
        camino.insertarNodo(nodo_actual.nodo)
        while ((nodo_actual.nodo.x != nodo_terreno.finalX) or (nodo_actual.nodo.y != nodo_terreno.finalY)):
            vecinos = terreno_actual.obtenerHermanos(nodo_actual.nodo.x, nodo_actual.nodo.y)
            if vecinos.inicio is not None:
                puntero = vecinos.inicio
                while puntero is not None:
                    puntero.nodo.setData(nodo_actual)
                    lista.insertar(puntero.nodo)
                    puntero = puntero.siguiente
            nodo_actual.nodo.visitado = True
            nodo_actual = lista.pop()
            camino.insertarNodo(nodo_actual.nodo)
        print("************************************************")
        print("          RUTA ENCONTRADA EXITOSAMENTE          ")
        print("************************************************")
        print("")
        print("EL COSTO DE COMBUSTIBLE DE LA RUTA MÁS ÓPTIMA ES: ")
        print("Coordenadas    x: ", nodo_actual.nodo.x , "y: ", nodo_actual.nodo.y, "Gasto de combustible: ", nodo_actual.nodo.data)
        print("")
        print("")

        #Procedimiento para obtener el recorrido del camino más corto
        ultimo = camino.inicio
        ruta = ListaCamino()
        while ultimo.siguiente is not None:
            ultimo = ultimo.siguiente
        while ultimo != None:
            ruta.insertarNodo(ultimo.nodo)
            ultimo = ultimo.nodo.nodoPadre
        nodo = 0
        
        #Ciclo para escribir la matriz con 0's y 1's
        for i in range(terreno_actual.cabecera_columnas.primero.x , nodo_terreno.m  + terreno_actual.cabecera_columnas.primero.x):
            for j in range(terreno_actual.cabecera_filas.primero.y, nodo_terreno.n + terreno_actual.cabecera_filas.primero.y):
                if ruta.verificarPunto(j, i):
                    print(Fore.LIGHTRED_EX,str(nodo + 1) + Fore.WHITE,"  |   ", end ="")
                else:
                    print(Fore.WHITE,str(nodo) + "   |   ", end ="")
            j = j+1
            print("\n")
        i = i+1  
    elif int(respuesta) == 3:
        print("Escriba la ruta de onde quiere guardar el archivo")
        ruta_archivo = input()
        #Ciclos para obtener el recorrido que realizó el algoritmo
        ultimo = camino.inicio
        ruta = ListaCamino()
        while ultimo.siguiente is not None:
            ultimo = ultimo.siguiente
        combustible = ultimo.nodo.data
        while ultimo != None:
            ruta.insertarNodo(ultimo.nodo)
            ultimo = ultimo.nodo.nodoPadre

        #Creación de la estructura xml con los datos de salida
        nodo_terreno = terrenos.verificarTerreno(terreno_res)
        raiz = ET.Element('terreno', nombre = nodo_terreno.dato)
        inicio = ET.SubElement(raiz, "posicioninicio")
        ET.SubElement(inicio, "x").text = str(nodo_terreno.inicioX)
        ET.SubElement(inicio, "y").text = str(nodo_terreno.inicioY)
        final = ET.SubElement(raiz, "posicionfin")
        ET.SubElement(final, "x").text = str(nodo_terreno.finalX)
        ET.SubElement(final, "y").text = str(nodo_terreno.finalX)
        ET.SubElement(raiz, "combustible").text = str(combustible)
        puntero = ruta.inicio
        while puntero is not None:
            ET.SubElement(raiz, "posicion", x = str(puntero.nodo.x), y = str(puntero.nodo.y)).text = str(puntero.nodo.data)
            puntero = puntero.siguiente
        archivo = ET.tostring(raiz, "unicode", "xml")
        xml1 = xml.dom.minidom.parseString(archivo)
        xml2 = xml1.toprettyxml()

        #Escritura del archivo xml
        try:
            miArchivo = open(ruta_archivo + "\salida.xml", "w")
            miArchivo.write(xml2)
            print("El archivo se ha escrito satisfactoriamente")
        except:
            print("Ocurrió un error al escribir el archivo, por favor inténtelo de nuevo")
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