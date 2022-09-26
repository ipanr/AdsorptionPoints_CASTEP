import os

def AislarElementoXSD(nombreArchivo, elementoXSD):
    archivo = open(nombreArchivo, "r")
    lineasDelArchivo = archivo.readlines()
    elementoAislado = []
    iniciarExtraccionDeDatos = False

    for posicion in range(len(lineasDelArchivo)):
        if "<" + elementoXSD in lineasDelArchivo[posicion]:
            iniciarExtraccionDeDatos = True

        if "/" + elementoXSD in lineasDelArchivo[posicion]:
            iniciarExtraccionDeDatos = False
            break

        if iniciarExtraccionDeDatos:
            elementoAislado.append(lineasDelArchivo[posicion])
    return elementoAislado

def SustraerCoordenadas(elementoXSD):
    listaCoordenadas = []
    stringsSeparados = []

    for elemento in elementoXSD:

        if "Atom3d" in elemento:
            stringsSeparados = str(elemento).split('" ')
            elementoQuimico = ""
            coordenada = ""
            StringCoordenada = ""

            for propiedad in stringsSeparados:

                if "XYZ=" in propiedad:
                    stringCoordenadaRAW = str(propiedad).split('="')
                    coordenada =  stringCoordenadaRAW[1]

                if "Components=" in propiedad:
                    stringComponenteRAW = str(propiedad).split('="')
                    stringElementoQuimico = str(stringComponenteRAW[1]).split('"')
                    elementoQuimico = stringElementoQuimico[0]
            
            StringCoordenada = elementoQuimico + " " + coordenada
            listaCoordenadas.append(StringCoordenada)

    return listaCoordenadas

def SustraerBaseVectorial(elementoXSD):

    for elemento in elementoXSD:

        if "SpaceGroup" in elemento:
            stringsSeparados = str(elemento).split('" ')
            stringVectorA = ""
            stringVectorB = ""
            stringVectorC = ""

            for propiedad in stringsSeparados:
                if "AVector" in propiedad:
                    stringVectorA = str(propiedad).split('="')
                if "BVector" in propiedad:
                    stringVectorB = str(propiedad).split('="')
                if "CVector" in propiedad:
                    stringVectorC = str(propiedad).split('="')

            baseVectorial = [stringVectorA[1], stringVectorB[1], stringVectorC[1]]

    return baseVectorial

def ModificarBloqueEnDocumento(directorioObjetivo, nombreArchivo, bloqueACambiar, valoresModificados):
    os.chdir(directorioObjetivo)

    archivo = open(nombreArchivo,"r")
    contenido = []
    listaContenido = archivo.readlines()

    if len(listaContenido) == 0:
        print("*************************ERROR, DOCUMENTO VACIO*******************************************")
        return 

    for elemento in range (0,len(listaContenido)):
        if r"%BLOCK " + bloqueACambiar in listaContenido[elemento]:
            i=1
            for valor in valoresModificados:
                listaContenido.insert(elemento + i, valor + "\n")
                i+=1

    contenido = "".join(listaContenido)
    
    archivo.close()
    archivo = open(nombreArchivo, "w")
    archivo.write(contenido)
    archivo.close()

    return

def DarFormatoAElementos(listaElementos):
    elementos =[]
    strings = []

    for elemento in listaElementos:
        elementos = str(elemento).split(",")

        for i in range( len(elementos)):
            elementos[i] += " "

        string = "".join(elementos)
        strings.append(string)
    
    return strings

def TransformarCoordenadasACartesianas(coordenadas, vectoresBase):
    nuevasCoordenada =[]

    for coordenada in coordenadas:
        coordenadaX = str( vectoresBase[0][0]*coordenada[0] + vectoresBase[1][0]*coordenada[1] + vectoresBase[2][0]*coordenada[2]) + " "
        coordenadaY = str( vectoresBase[0][1]*coordenada[0] + vectoresBase[1][1]*coordenada[1] + vectoresBase[2][1]*coordenada[2]) + " "
        coordenadaZ = str( vectoresBase[0][2]*coordenada[0] + vectoresBase[1][2]*coordenada[1] + vectoresBase[2][2]*coordenada[2]) + " "

        nuevaCoordenada = [coordenadaX, coordenadaY, coordenadaZ]

        nuevasCoordenada.append(nuevaCoordenada)

    return nuevasCoordenada

def ExtraerCoordenadasNumericas(stringCASTEP, desfase):
    listaCoordenadasNumericas = []

    for elemento in stringCASTEP:
        coordenadasCASTEP = str(elemento).split(" ")
        coordenadaNumerica = [float(coordenadasCASTEP[0 + desfase]), float(coordenadasCASTEP[1 + desfase]), float(coordenadasCASTEP[2 + desfase])]
        listaCoordenadasNumericas.append(coordenadaNumerica)

    return listaCoordenadasNumericas

def FormatearCoordenadasCartesianas(coordenadasXSD, coordenadasCartesianas):
    stringXSD = str(coordenadasXSD).split(" ")
    stringsCartesianas = []

    for i in range(0, len(coordenadasCartesianas)):
        stringConElElemento = str(stringXSD[5*i]).split("'")
        elemento = stringConElElemento[1]
        coordenadaCASTEP = elemento + " " + str(coordenadasCartesianas[i][0]) + " " + str(coordenadasCartesianas[i][1]) + " " + str(coordenadasCartesianas[i][2])
        stringsCartesianas.append(coordenadaCASTEP)

    return stringsCartesianas
