import os
from sys import path

def FunModificarParametro(directorioObjetivo, nombreArchivo, lineaACambiar, valorModificado):
    os.chdir(directorioObjetivo)

    archivo = open(nombreArchivo,"r")
    contenido = ""
    listaContenido = archivo.readlines()
    if len(listaContenido) == 0:
        print("*************************ERROR, DOCUMENTO VACIO*******************************************")
        return 
    listaContenido[lineaACambiar] = valorModificado + "\n"
    contenido = "".join(listaContenido)
    archivo.close()

    archivo = open(nombreArchivo, "w")
    archivo.write(contenido)
    archivo.close()

    return contenido
