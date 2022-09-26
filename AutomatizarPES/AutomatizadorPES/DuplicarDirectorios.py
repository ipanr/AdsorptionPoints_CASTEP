import os
import shutil

def DuplicarDirectorio(directorioPadre, directorioACopiar, directorioReceptor, numeroDeArchivosEsperados):

    if (os.path.exists(directorioPadre) == False):
        print("*****************NO EXISTE EL DIRECTORIO PADRE******************")
        return False

    os.chdir(directorioPadre)
    direccionReceptora = os.path.join(directorioPadre , directorioReceptor)
    direccionCopiada = os.path.join(directorioPadre , directorioACopiar)
    
    if (os.path.exists(direccionCopiada) == False):
        print("*****************NO EXISTE EL DIRECTORIO A COPIAR******************")
        return False

    listaArchivosACopiar = os.listdir(direccionCopiada)

    if (len(listaArchivosACopiar) != numeroDeArchivosEsperados):
        print("*****************EL DIRECTORIO NO TIENE EL NUMERO ESPERADO DE ARCHIVOS******************")
        return False

    if (os.path.exists(direccionReceptora) == False):
       os.mkdir(directorioReceptor)

    for i in range(0, numeroDeArchivosEsperados):
        direccionDelArchivoCopiado = os.path.join(direccionCopiada, listaArchivosACopiar[i])
        shutil.copy(direccionDelArchivoCopiado, direccionReceptora)

    return True
