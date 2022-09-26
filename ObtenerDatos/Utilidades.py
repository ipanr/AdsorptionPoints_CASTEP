import os

def CambiarDirectorio(directorioPadre, nombreCarpeta):
    os.chdir(os.path.join(directorioPadre, nombreCarpeta))
    return

def BuscarPalabra(nombreArchivo, lineaInicial, PalabraClave):
    archivo = open(nombreArchivo, "r")
    lineasDelArchivo = archivo.readlines()
    energia = ""

    for posicion in range(lineaInicial,len(lineasDelArchivo)):
        if PalabraClave in lineasDelArchivo[posicion]:
            energia += lineasDelArchivo[posicion][16:32] + " "
            break
        if "Current total energy" in lineasDelArchivo[posicion]:
            energia += lineasDelArchivo[posicion][24:40] + " "
            break
    return energia

def HacerArchivoDeEnergias(directorioPadre, nombreFinal, energias):
    os.chdir(directorioPadre)
    archivo = open(nombreFinal, "w")
    archivo.write(energias)
    archivo.close()
    return
