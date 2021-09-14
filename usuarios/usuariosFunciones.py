import usuarios.usuariosModel as usuarioModelo

def buscar(email):    
    search = usuarioModelo.Usuario.buscar(email)
    return search


def registrarUsuario():
    print('\n-----Datos de usuaio --------')
    nombre = input('Digita tu nombre:   ')
    apellidos = input('Digita tus apellidos:   ')
    email = input('Digita tu email:   ')
    password = input('Digita tu contraseña:   ')

    search = buscar(email)
    
    if len(search)!=0:
        return 'Este e-mail no está disponible'
    else:
        try:
            usuario = usuarioModelo.Usuario(nombre,apellidos,email,password)
            guardar = usuario.guardar()
            return guardar
        except:
            return 'Error al registrar usuario en la bd'

def login():
    print('\n-----Datos de usuaio--------')
    email = input('Escribe tu email:   ')
    password = input('Escribe tu contraseña:   ')
    
    search = buscar(email)

    if len(search)==0:
        return 'Error de credenciales'
    else:
        passwordBD = search[0][4]
        if passwordBD!=password:
            return ['Error de credenciales','']
        else:
            return [True,search[0][1],search[0][0]]