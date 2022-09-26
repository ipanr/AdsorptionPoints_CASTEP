from DefinirCoordenadas import DefinirCoordenadas, DefinirCoordenadasAtomosSecundarios, Vector3
from ModificarParametro import FunModificarParametro
from DuplicarDirectorios import DuplicarDirectorio
from EjecutarComandos import FunEjecutarComando
import os

#el numero de puntos será el numero de intervalos + 1
lIntervalos = 2
intervalosBaseUno = 6 #en total serán n+1 intervalos
intervalosBaseDos = 11 #en total serán n+1 intervalos

l = 0
x = 0
y = 0

#altura sobre la que se pondrá el atomo sobre la superficie
alturaVacio = 1.0

lineaConCoordenadasAtomicas = 15 #poner el valor n-1
nombreArchivoConParametros = "CuFeO2.cell"
nombreParaCastep = "CuFeO2"
base1 = Vector3(3.0631538     ,0.0000000    ,0.00000000)
base2 = Vector3(0.0000000     ,5.7504279     ,1.7796546)
vectorC = Vector3(0.0, -0.7967375, 2.5744165) #Debe ser la altura del punto mas bajo de los atomos, puede serla altura del atomo más alto de la estructura
elementoCentral = "C" #El elemento central a partir del cual se calcularán el resto de las posiciones de los atomos unidos a él
#Aquí van los elementos secundarios que se unan al elemento central. los porcentajes son posiciones respecto a los vectores base
elementoSecundario = "O"
porcentajesElementoSecundario = Vector3(0.3787,0.0 ,0)
porcentajesElementoTerciario = Vector3(-0.3787,0.0,0)
#Conjunto de mensajes en caso de que falle
fallaDuplicarDirectorio = "Hubo una falla al duplicar los directorios"

#se programó con la idea de un directorioPadre = r"/mnt/c/users/ipanr/desktop/CuFeO2"
directorioPadre = r"/home/isaac/Desktop/Resultados Tesis/CuFeO2/Energias con OG y CO2/CuFeO2 (0 0 6) 1A de nuevo"

lineaDeComando = r"mpirun -n 6 castep.mpi"
#lineaDeComando = r"./castep.serial"

for h in range(lIntervalos + 1):
    for a in range (intervalosBaseUno + 1):
        for b in range (intervalosBaseDos + 1):
            porcentajeL = h/lIntervalos
            porcentajeX = a/intervalosBaseUno
            porcentajeY = b/intervalosBaseDos 
            vectorPorcentajes = Vector3(porcentajeX, porcentajeY, porcentajeL)

            carpetaReceptora = "L" + str(h) + "C" + str(a) + "-" + str(b)
            directorioReceptor = os.path.join(directorioPadre , carpetaReceptora)

            carpetaBase = "Base"
            directorioBase = os.path.join(directorioPadre, carpetaBase)

            copiarDirectorio = DuplicarDirectorio(directorioPadre,directorioBase,directorioReceptor,7)

            if(copiarDirectorio):
                os.chdir(directorioReceptor)

                coordenadaElementoCentral = DefinirCoordenadas(base1, base2, vectorC, alturaVacio, vectorPorcentajes)
                puntoSecundario = DefinirCoordenadasAtomosSecundarios(base1,base2,vectorC, coordenadaElementoCentral,porcentajesElementoSecundario)
                puntoTerciario = DefinirCoordenadasAtomosSecundarios(base1,base2,vectorC, coordenadaElementoCentral,porcentajesElementoTerciario)
                textoPuntoCentralAEvaluar = elementoCentral + " " + str(coordenadaElementoCentral.x) + " " + str(coordenadaElementoCentral.y) + " " + str(coordenadaElementoCentral.z)
                textoPuntoSecundario = elementoSecundario + " " + str(puntoSecundario.x) + " " + str(puntoSecundario.y) + " " + str(puntoSecundario.z)
                textoPuntoTerciario = elementoSecundario + " " + str(puntoTerciario.x) + " " + str(puntoTerciario.y) + " " + str(puntoTerciario.z)

                FunModificarParametro(directorioReceptor,nombreArchivoConParametros,lineaConCoordenadasAtomicas, textoPuntoCentralAEvaluar)
                FunModificarParametro(directorioReceptor, nombreArchivoConParametros, lineaConCoordenadasAtomicas + 1, textoPuntoSecundario)
                FunModificarParametro(directorioReceptor, nombreArchivoConParametros, lineaConCoordenadasAtomicas + 2, textoPuntoTerciario)
                
                FunEjecutarComando(directorioReceptor, lineaDeComando , nombreParaCastep)

            else:
                print(fallaDuplicarDirectorio)
                break
