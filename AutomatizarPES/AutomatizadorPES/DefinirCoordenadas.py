from math import sqrt

class Vector3:
    def __init__(self, x0, y0, z0):
        self.x = x0
        self.y = y0
        self.z = z0

def DefinirCoordenadas(base1, base2, vectorElevacion, alturaVacio, PorcentajeRecorrido):
    if ((type(base1) != Vector3) or (type(base2) != Vector3) or (type(vectorElevacion) != Vector3) or (type(PorcentajeRecorrido) != Vector3)) :
        print("**************Las bases agregadas no son vectores3**************")
        return False

    vectorNormal = ObtenerProductoPunto(base1,base2)

    mapeoSobreBase1 = Vector3(PorcentajeRecorrido.x * base1.x, PorcentajeRecorrido.x * base1.y, PorcentajeRecorrido.x * base1.z)
    mapeoSobreBase2 = Vector3(PorcentajeRecorrido.y * base2.x, PorcentajeRecorrido.y * base2.y, PorcentajeRecorrido.y * base2.z)
    mapeoSobreBaseZ = Vector3(vectorElevacion.x + alturaVacio *vectorNormal.x *(1 - PorcentajeRecorrido.z), vectorElevacion.y + alturaVacio* vectorNormal.y *(1 - PorcentajeRecorrido.z), vectorElevacion.z + alturaVacio* vectorNormal.z *(1 - PorcentajeRecorrido.z))

    puntoAEvaluar = Vector3(mapeoSobreBaseZ.x + mapeoSobreBase1.x + mapeoSobreBase2.x, mapeoSobreBaseZ.y + mapeoSobreBase1.y + mapeoSobreBase2.y, mapeoSobreBaseZ.z + mapeoSobreBase1.z + mapeoSobreBase2.z)

    return puntoAEvaluar

def DefinirCoordenadasAtomosSecundarios(base1, base2, baseC, coordenadaCentro, porcentajeBases):
    if ((type(base1) != Vector3) or (type(base2) != Vector3) or (type(baseC) != Vector3)):
        print("**************Las bases agregadas no son vectores3**************")
        return False

    direccionElemento = Vector3(coordenadaCentro.x + base1.x*porcentajeBases.x + base2.x*porcentajeBases.y + baseC.x*porcentajeBases.z,
                                coordenadaCentro.y + base1.y*porcentajeBases.x + base2.y*porcentajeBases.y + baseC.y*porcentajeBases.z,
                                coordenadaCentro.z + base1.z*porcentajeBases.x + base2.z*porcentajeBases.y + baseC.z*porcentajeBases.z)

    puntoAEvaluar = direccionElemento

    return puntoAEvaluar

def ObtenerProductoPunto(vector1, vector2):
    x = vector1.y*vector2.z - vector1.z*vector2.y
    y = -(vector1.x*vector2.z - vector1.z*vector2.x)
    z = (vector1.x*vector2.y - vector1.y*vector2.x)

    norma = sqrt(x**2 + y**2 + z**2)
    xNormal = x/norma
    yNormal = y/norma
    zNormal = z/norma

    vectorNormal = Vector3(xNormal, yNormal, zNormal)

    return vectorNormal
