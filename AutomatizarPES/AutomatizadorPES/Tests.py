from DefinirCoordenadas import DefinirCoordenadas, Vector3
import os
from ModificarParametro import FunModificarParametro
from EjecutarComandos import FunEjecutarComando
from DuplicarDirectorios import DuplicarDirectorio
from DefinirCoordenadas import DefinirCoordenadas

#-------------------------------------TESTS ModificarParametro---------------------------------------------------------
def TestFunModificarParametro():
    directorioPadre = os.path.dirname(os.getcwd())
    directorioConTextos = "Recursos"

    directorioObjetivo = os.path.join(directorioPadre,directorioConTextos)
    nombreDocumento = "TestDocument.txt"
    lineaACambiar = 7
    nuevoParametro ="C 1.0 2.0 4.0"

    valorObtenido = FunModificarParametro(directorioObjetivo, nombreDocumento, lineaACambiar, nuevoParametro)
    valorEsperado = "Esta es una lista de cosas para un test:\n\n1. La tarea\n2. La comida\n3. El termo\n\n!La coordenada\n" + nuevoParametro 

    if(valorObtenido) == valorEsperado:
        print("Prueba pasada")
        return True
    else:
        print("Prueba fallada")
        return False

#TestFunModificarParametro()

#-------------------------------------TESTS EjecutarComandos---------------------------------------------------------
def TestEjecutarComando():
    valorObtenido = FunEjecutarComando(r"/mnt/c/users/ipanr/desktop/calculoscastep/tesis1/BPE1A",r"./castep.serial","Fe")
    valorEsperado = 1
    
    if(valorObtenido) == valorEsperado:
        print("Prueba pasada")
        return True
    else:
        print("Prueba fallada")
        return False

#TestEjecutarComando()

#-------------------------------------TESTS DuplicarYRenombrarDirectorios---------------------------------------------------------
def TestDuplicarDirectoriosCorrecto():
    valorObtenido = DuplicarDirectorio("C:/users/ipanr/desktop/AutomatizarPES/Recursos","DirectorioACopiar", "TestCrearDirectorio", 2)
    valorEsperado = True

    if(valorObtenido) == valorEsperado:
        print("Prueba pasada")
        return True
    else:
        print("Prueba fallada")
        return False

def TestDuplicarDirectoriosDistitosArchivosEsperados():
    archivosEsperados = 3
    valorObtenido = DuplicarDirectorio("C:/users/ipanr/desktop/AutomatizarPES/Recursos","DirectorioACopiar", "TestCrearDirectorio", archivosEsperados)
    valorEsperado = False

    if(valorObtenido) == valorEsperado:
        print("Prueba pasada")
        return True
    else:
        print("Prueba fallada")
        return False

def TestDuplicarDirectoriosNoExisteDireccionACopiar():
    archivosEsperados = 2
    valorObtenido = DuplicarDirectorio("C:/users/ipanr/desktop/AutomatizarPES/Recursos","DirectorioACopiarNoExistente", "TestCrearDirectorio", archivosEsperados)
    valorEsperado = False

    if(valorObtenido) == valorEsperado:
        print("Prueba pasada")
        return True
    else:
        print("Prueba fallada")
        return False

def TestDuplicarDirectoriosNoExisteDireccionPadre():
    archivosEsperados = 2
    valorObtenido = DuplicarDirectorio("C:/users/ipanr/desktop/AutomatizarPES/RecursosInventados","DirectorioACopiar", "TestCrearDirectorio", archivosEsperados)
    valorEsperado = False

    if(valorObtenido) == valorEsperado:
        print("Prueba pasada")
        return True
    else:
        print("Prueba fallada")
        return False

#TestDuplicarDirectoriosCorrecto()

#-------------------------------------TESTS DefinirCoordenadas---------------------------------------------------------
def TestDefinirCoordenadasNoVector3():
    valorObtenido = DefinirCoordenadas(1,1,1)
    valorEsperado = True

    if(valorObtenido) == valorEsperado:
        print("Prueba pasada")
        return True
    else:
        print("Prueba fallada")
        return False

def TestDefinirCoordenadas():
    base1 = Vector3(0,1,0) #aXb tiene que ser anti paralelo a la base 3 para que esto funcione
    base2 = Vector3(1,0,0)
    base3 = Vector3(0,0,1)
    alturaVacio = 5
    porcentajeRecorrido = Vector3(1,1,1)
    
    valorObtenido = DefinirCoordenadas(base1,base2, base3, alturaVacio, porcentajeRecorrido)
    valorEsperado = Vector3(1,1,6)

    if(valorObtenido.x == valorEsperado.x and valorObtenido.y == valorEsperado.y and valorObtenido.z == valorEsperado.z):
        print("Prueba pasada")
        return True
    else:
        print("Prueba fallada")
        return False

def TestDefinirCoordenadasNaCl():
    base1 = Vector3(2.6489433, 2.6489433, 0)
    base2 = Vector3(2.6489433,0,2.6489433)
    base3 = Vector3(0,2.6489433,2.6489433)
    alturaVacio = 5
    porcentajeRecorrido = Vector3(0,0,1)
    
    valorObtenido = DefinirCoordenadas(base1,base2, base3, alturaVacio, porcentajeRecorrido)
    valorEsperado = Vector3(-2.8867513459481287, 5.535694645948128, 5.535694645948128)

    if(valorObtenido.x == valorEsperado.x and valorObtenido.y == valorEsperado.y and valorObtenido.z == valorEsperado.z):
        print("Prueba pasada")
        return True
    else:
        print("Prueba fallada")
        return False

TestDefinirCoordenadasNaCl()

def TestDefinirCoordenadasCuFeO2():
    base1 = Vector3(0, 0, 10.229842  )
    base2 = Vector3(5.263626, -5.263626, 0)
    base3 = Vector3(2.653012307109,  2.6530122003210064,  0 )
    alturaVacio = 1
    porcentajeRecorrido = Vector3(1, 1, 1)
    puntoAEvaluar = DefinirCoordenadas(base1, base2, base3, alturaVacio, porcentajeRecorrido)#
    textoPuntoAEvaluar = "C " + str(puntoAEvaluar.x) + " " + str(puntoAEvaluar.y) + " " + str(puntoAEvaluar.z)
    print(textoPuntoAEvaluar)
    
    valorObtenido = DefinirCoordenadas(base1,base2, base3, alturaVacio, porcentajeRecorrido)
    valorEsperado = Vector3(-2.8867513459481287, 5.535694645948128, 5.535694645948128)

    #print (valorObtenido.x , valorObtenido.y , valorObtenido.z)

    if(valorObtenido.x == valorEsperado.x and valorObtenido.y == valorEsperado.y and valorObtenido.z == valorEsperado.z):
        print("Prueba pasada")
        return True
    else:
        print("Prueba fallada")
        return False

#TestDefinirCoordenadasCuFeO2()

def TestDuplicarDirectoriosCLinux():
    directorioPadre = r"/home/isaac/Desktop/Resultados Tesis/CuFeO2/Energias Superficiales no OG/CuFeO2 (0 0 6)"
    valorObtenido = DuplicarDirectorio(directorioPadre,directorioPadre + "/Base", directorioPadre + "TestCrearDirectorio", 7)
    valorEsperado = True

    if(valorObtenido) == valorEsperado:
        print("Prueba pasada")
        return True
    else:
        print("Prueba fallada")
        return False

#TestDuplicarDirectoriosCLinux()
