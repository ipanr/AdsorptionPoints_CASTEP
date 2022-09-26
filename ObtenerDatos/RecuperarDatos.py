import os
from sys import path
import Utilidades
# Recupera los datos generados para la adsorción superficial
directorioPadre = r"/home/isaac/Desktop/Resultados Tesis/CuFeO2/Energias con OG y CO2/CuFeO2 (0 0 6) 0A 1B 0C"
nombreArchivo = "CuFeO2.castep"
lineaInicial = 0
PalabraClave = "Final energy"
nombreFinal = "Lista de energias O2 006 sobre B.txt"

stringEnergias = ""

# os.chdir(directorioPadre)
# contenido = ""
# archivo = open(nombreArchivo, "r")
# listaContenido = archivo.readlines()

lMax = 2
xMax = 6
yMax = 11

for l in range(lMax + 1):
    for x in range (xMax + 1):
        for y in range (yMax + 1):
            nombreCarpeta = "L" + str(l) + "C" + str(x) + "-" + str(y)
            Utilidades.CambiarDirectorio(directorioPadre, nombreCarpeta)
            stringEnergias += Utilidades.BuscarPalabra(nombreArchivo, lineaInicial, PalabraClave) + " "
            print("archivo leido " + nombreCarpeta)
        stringEnergias += "\n"
    stringEnergias += "\n"

Utilidades.HacerArchivoDeEnergias(directorioPadre, nombreFinal, stringEnergias)




