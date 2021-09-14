import usuarios.usuariosFunciones as userFunciones
import notas.notasFunciones as notaFunciones   

def inicio():
    print('Bienvenido a tu plataforma preferida de Notas. ¿Que deseas hacer? ')
    print('- Para registrarte digita "Registrarme" \n- Para Iniciar Sesión digita "Login" '  )

    menu=input()

    if menu!='Login' and menu!='Registrarme':
        print('Digite una opción válida')
    else:
        if menu == 'Registrarme':
            registrarUser = userFunciones.registrarUsuario()
            print(registrarUser)           
        
        else:
            login = userFunciones.login()
            if login[0] != True:
                print(login)
            else:
                idUser = login[2]
                print(f'\n Bienvenido {login[1]} ')
                menu=''
                while menu !='4':
                    print('\n  MENÚ  ')
                    print('  1. Añadir nota ( añadir ) \n  2. Mostrar mis Notas ( mostrar ) \n  3. Eliminar nota (eliminar) \n  4. Salir (salir)')
                    menu = input(' Digite el número correspondiente a la opción que desea realizar ')
                    
                    if menu == '1':
                        registrarNote = notaFunciones.registrarNota(idUser)
                        print(registrarNote)
                    elif menu == '2':
                        notas = notaFunciones.listar(idUser)
                        for nota in notas:
                            print(f' Titulo:  {nota[2]} \n Descripción: {nota[3]}  \n')
                    elif menu == '3':
                        notas = notaFunciones.listar()
                        for nota in notas:
                            print(f'{nota[2]}')
                        notaEliminada = input("¿Cual nota desea eliminar?   ")
                        eliminar = notaFunciones.eliminarNota(notaEliminada)
                        print(eliminar)
                    elif menu == '4':
                        print('Vuelva pronto')
                    else:
                        print('Opción no válida')

inicio()





