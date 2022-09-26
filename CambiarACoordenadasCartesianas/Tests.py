import Utilidades

vectorA = [2,2,0]
vectorB = [0,2,2]
vectorC = [2,0,2]

vectoresBase = [vectorA, vectorB, vectorC]

listaCoordenadas = [[0, 0.5, 0.75], [1, 0.5, 0.75]]

def TestTransformarCoordenadasExitoso():
    valorEsperado = [[0, 2.0, 3.0], [4, 2.0, 3.0]]
    valorObtenido =Utilidades.TransformarCoordenadasACartesianasImp(listaCoordenadas, vectoresBase)
    return (valorEsperado == valorObtenido)

def RunTest(test):    
    if(test == True):
        print("Test Exitoso")
    else:
        print("xxxxxxxxxx Test Fallado xxxxxxxxxx")

RunTest(TestTransformarCoordenadasExitoso())
