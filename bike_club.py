import functions_bike_club as fbc

import os
fbc.mostrar_bienvenida()
nombre = fbc.obtener_nombre()




print("Hola ", nombre, ", bienvenido a Bike club")
print()

#Verificamos si el archivo existe
if fbc.existe_archivo(nombre+".user"):
    print("Leyendo datos de usuario", nombre, "desde archivo.")
    (nombre, edad, estatura_m, estatura_cm, sexo, amigos, estado, muro) = fbc.leer_usuario(nombre)

else:
    #En caso que el usuario no exista, consultamos por sus datos tal como lo hacÃ­amos antes
    print()
    edad = fbc.obtener_edad()
    (estatura_m, estatura_cm) = fbc.obtener_estatura()
    sexo = fbc.obtener_sexo()
    amigos = fbc.obtener_lista_amigos()
    estado = ""
    muro = []

#En ambos casos, al llegar aquÃ­ ya conocemos los datos del usuario
print("Muy bien. Estos son los datos de tu perfil.")
fbc.datos(nombre, edad, estatura_m, estatura_cm, sexo, amigos)
fbc.mostrar_mensaje(nombre, estado)

#Ahora podemos mostrar el menu y consultar las opciones
opcion = -1
while opcion != 0:
    opcion = fbc.menu()
    if opcion == 1:
        estado = fbc.obtener_mensaje()
        fbc.publicar_mensaje(nombre, amigos, estado, muro)
    elif opcion == 2:
        fbc.mostrar_muro(muro)
    elif opcion == 3:
        fbc.datos(nombre, edad, estatura_m, estatura_cm, sexo, amigos)
    elif opcion == 4:
        edad = fbc.obtener_edad()
        (estatura_m, estatura_cm) = fbc.obtener_estatura()
        sexo = fbc.obtener_sexo()
        amigos = fbc.obtener_lista_amigos()
        fbc.datos(nombre, edad, estatura_m, estatura_cm, sexo, amigos)
    elif opcion == 0:
        print("Has decidido salir. Guardando perfil en ",nombre+".user")
        fbc.escribir_usuario(nombre, edad, estatura_m, estatura_cm, sexo,  amigos, estado,muro)
        print("Archivo",nombre+".user","guardado")

print("Gracias por usar Bike Club ¡Hasta pronto!")

