from Matriz import Matriz
from Lista import Lista
from Encabezados import columnas
from Nodos import NodoC, NodoF, NodoM
from Matriz import Matriz
import xml.etree.ElementTree as xml

end_program = False
terrenos = Lista()


def carga():
    #respuesta = input("Ingrese la ruta del archivo a procesar\n")
    objetoTree = xml.parse("prueba.xml")
    root = objetoTree.getroot()
    for terreno in root.findall("terreno"):
        terrenos.insertar(terreno.get("nombre"))
        print("Posición de inicio: ")
        mapa = Matriz()
        for posicionI in terreno.findall("posicioninicio"):
            for x in posicionI.findall("x"):
                print(x.text)
            for y in posicionI.findall("y"):
                print(y.text)
        print("Posición de finalización: ")
        for posicionF in terreno.findall("posicionfin"):
            for x in posicionF.findall("x"):
                print(x.text)
            for y in posicionF.findall("y"):
                print(y.text)
        for posiciones in terreno.findall("posicion"):
            mapa.agregarNodo(int(posiciones.text), int(posiciones.get("x")), int(posiciones.get("y" )))
            #print("Posicion x: " + posiciones.get("x"))
            #print("Posicion y: " + posiciones.get("y"))
            #print("Coste de combustible: " + posiciones.text)
        mapa.mostrarColumnas()
        terrenos.asignarMapa(terreno.get("Nombre"), mapa)
        
        
        


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
        print("Ingrese el nombre del terreno a procesar")
        terreno_res = input()
        nodo_terreno = terrenos.verificarTerreno(terreno_res)
        if nodo_terreno == None:
            print("El terreno que usted ha ingresado no se encuentra en el programa")
        terreno_actual = nodo_terreno.getMapa()
        terreno_actual.mostrarColumnas()
    elif int(respuesta) == 3:
        print("Usted ha seleccionado la tercera opción")
    elif int(respuesta) == 4:
        print("José Andrés Montenegro Santos")
        print("202004804")
        print("Introducción a la Programación y Computación 2 sección: A")
        print("Ingeniería en Ciencias y Sistemas")
        print("4to Semestre")
    elif int(respuesta) == 5:
        print("Usted ha seleccionado la tercera opción")
    elif int(respuesta) == 6:
        global end_program
        end_program = True
    

def main():
    menuPrincipal()

while not end_program:
    if __name__ == "__main__":
        main()