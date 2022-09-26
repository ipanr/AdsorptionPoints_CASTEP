import os

directorioPadre = r"C:\Users\Ipanr\Desktop\Programas suplementarios\ConstruirSuperCelda\UtilidadesTest"
archivoObjetivo = "CuFeO2006Test.cell"
bloqueObjetivo = "LATTICE_CART"

def SustraerBloque(directorioPadre, archivoObjetivo, nombreBloque):
    os.chdir(directorioPadre)
    archivo = open(archivoObjetivo, "r")
    lineasArchivo = archivo.readlines() 
    extraerDatos = False

    bloqueARegresar = []

    for posicion in range(len(lineasArchivo)):
        if "%BLOCK " + nombreBloque in lineasArchivo[posicion]:
            extraerDatos = True

        if r"%ENDBLOCK " + nombreBloque in lineasArchivo[posicion]:
            extraerDatos = False
            break

        if(extraerDatos):
             bloqueARegresar.append(lineasArchivo[posicion])

    bloqueARegresar.remove(bloqueARegresar[0])

    return bloqueARegresar

def SepararVectores3EnString(stringASeparar, desfase):
    vectorADevolver = []

    for elemento in stringASeparar:
        componentesVectoriales = str(elemento).split(" ")
        vectorADevolver.append([float(componentesVectoriales[0 + desfase]), float(componentesVectoriales[1 + desfase]), float(componentesVectoriales[2 + desfase])])
    
    return vectorADevolver

def ConstruirSuperCelda(baseVectorial, posicionesAtomicas, a, b, c):
    nuevaBaseVectorial = [[], [], []]
    nuevasPosicionesAtomicas = []

    nuevaBaseVectorial[0] = [a*baseVectorial[0][0] , a*baseVectorial[0][1], a*baseVectorial[0][2]] 
    nuevaBaseVectorial[1] = [b*baseVectorial[1][0] , b*baseVectorial[1][1], b*baseVectorial[1][2]] 
    nuevaBaseVectorial[2] = [c*baseVectorial[2][0] , c*baseVectorial[2][1], c*baseVectorial[2][2]] 

    return nuevaBaseVectorial

def TestSustraerBloqueExitoso():
    valorObtenido = SustraerBloque(directorioPadre, archivoObjetivo, bloqueObjetivo)
    valorEsperado = ['3.06315384 -1.41664193687138e-009 -1.02112648413154e-007 \n', '0 5.75042792327473 1.77965459422918 \n', '6.36887482812275e-007 -5.93821906169843 19.1876001206308 \n']
    return valorEsperado == valorObtenido

def TestSustraerVectores3EnStringVectorBase():
    valorEsperado = [[3.06315384, -1.41664193687138e-009, -1.02112648413154e-007], [3.06315384, -1.41664193687138e-009, -1.02112648413154e-007]]
    valorObtenido = SepararVectores3EnString(['3.06315384 -1.41664193687138e-009 -1.02112648413154e-007 \n', '3.06315384 -1.41664193687138e-009 -1.02112648413154e-007 \n'],0)
    return valorEsperado == valorObtenido

def TestSustraerVectores3EnStringPosicionAtomica():
    valorEsperado = [[3.06315384, -1.41664193687138e-009, -1.02112648413154e-007], [3.06315384, -1.41664193687138e-009, -1.02112648413154e-007]]
    valorObtenido = SepararVectores3EnString(['Fe 3.06315384 -1.41664193687138e-009 -1.02112648413154e-007 \n', 'Fe 3.06315384 -1.41664193687138e-009 -1.02112648413154e-007 \n'],1)
    return valorEsperado == valorObtenido

def TestConstruirSuperCelda():
    valorEsperado = [[2,0,0], [0,2,0], [0,0,1]]
    valorObtenido = ConstruirSuperCelda([[1,0,0],[0,1,0], [0,0,1]], "", 2,2,1)
    return valorEsperado == valorObtenido

print(TestConstruirSuperCelda())

# print(TestSustraerBloqueExitoso())
# print(TestSustraerVectores3EnStringVectorBase())
# print(TestSustraerVectores3EnStringPosicionAtomica())