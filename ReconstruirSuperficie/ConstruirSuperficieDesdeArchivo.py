import os
import Utilidades

#Cambia lor archivos XSD obtenidos en Materials Studio y los convierte en archivos para CASTEP

directorioPadreSuperficies = r"/home/isaac/Desktop/Resultados Tesis/CuFeO2/Optimizaciones Geométricas/(0 0 6)/5A"
archivoObjetivoSuperficies = "CuFeO2 crystal (0 0 6) 5A CASTEP" + ".xsd"
palabraClaveXSD = "IdentityMapping"

directorioPadreCASTEP = r"/home/isaac/Desktop/Resultados Tesis/CuFeO2/Optimizaciones Geométricas/(0 0 6)/5A"
archivoObjetivoCASTEP = "CuFeO2" + ".cell"
palabraClaveCASTEP = "LATTICE_CART"

os.chdir(directorioPadreSuperficies)

#Coordenadas fraccionales
elementoXSD = Utilidades.AislarElementoXSD(archivoObjetivoSuperficies, palabraClaveXSD)
coordenadas = Utilidades.DarFormatoAElementos(Utilidades.SustraerCoordenadas(elementoXSD))
baseVectorial = Utilidades.DarFormatoAElementos(Utilidades.SustraerBaseVectorial(elementoXSD))

#Coordenadas absolutas
coordenadasNumericas = Utilidades.ExtraerCoordenadasNumericas(coordenadas, 1)
baseVectorialNumerica = Utilidades.ExtraerCoordenadasNumericas(baseVectorial,0)
floatCoordenadasCartesianas = Utilidades.TransformarCoordenadasACartesianas(coordenadasNumericas,baseVectorialNumerica)
stringCoordenadasCartesianas = Utilidades.FormatearCoordenadasCartesianas(coordenadas, floatCoordenadasCartesianas)

Utilidades.ModificarBloqueEnDocumento(directorioPadreCASTEP, archivoObjetivoCASTEP,"LATTICE_CART", baseVectorial)
Utilidades.ModificarBloqueEnDocumento(directorioPadreCASTEP, archivoObjetivoCASTEP,"POSITIONS_ABS", stringCoordenadasCartesianas)
