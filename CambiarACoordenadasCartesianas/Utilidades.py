
def TransformarCoordenadasACartesianasImp(coordenadas, vectoresBase):
    nuevasCoordenada =[]

    for coordenada in coordenadas:
        coordenadaX = (vectoresBase[0][0] + vectoresBase[1][0] + vectoresBase[2][0])*(coordenada[0])
        coordenadaY = (vectoresBase[0][1] + vectoresBase[1][1] + vectoresBase[2][1])*(coordenada[1])
        coordenadaZ = (vectoresBase[0][2] + vectoresBase[1][2] + vectoresBase[2][2])*(coordenada[2])

        nuevaCoordenada = [coordenadaX, coordenadaY, coordenadaZ]
        nuevasCoordenada.append(nuevaCoordenada)

    return nuevasCoordenada
