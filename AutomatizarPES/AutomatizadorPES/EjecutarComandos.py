import os

def FunEjecutarComando(directorio, comando, accion):
    comandoAEjecutar = comando + " " + accion

    if (os.path.exists(directorio) == False):
        print("*****************NO EXISTE EL DIRECTORIO PADRE******************")
        return False

    os.chdir(directorio)
    
    os.system(comandoAEjecutar)
    return False
