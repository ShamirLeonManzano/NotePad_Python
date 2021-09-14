import notas.notasModel as notaModelo

def search(titulo):
    buscar = notaModelo.Nota.buscar(titulo)
    return buscar



def registrarNota(idUser):
    titulo = input('Titulo:  ')
    descripcion = input('Descripcion:  ')

    buscando = search(titulo)
    if len(buscando)!=0:
        return 'Ya existe un nota con este titulo'
    else:
        try:
            nota = notaModelo.Nota(idUser,titulo,descripcion)
            guardar = nota.guardar()
            return guardar
        except:
           return 'Error al registrar nota en la base de datos' 

def listar(idUser):
    print('\n------- Notas registradas---------')
    buscando = notaModelo.Nota.listar(idUser)
    return buscando

def eliminarNota(titulo):
    buscando = search(titulo)
    if len(buscando)==0:
        print("¡Mmm..! Esa nonta no existe" )
    else:
        try:
            eliminar = notaModelo.Nota.delete(titulo)
            return eliminar
        except:
            return 'Error al eliminar la nota en la base de datos'