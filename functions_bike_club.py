import os
def mostrar_bienvenida():
    print("Bienvenido a ... ")
    print("""

     ______  _________ _        _______    _______  _                 ______  
    (  ___ \ \__   __/| \    /\(  ____ \  (  ____ \( \      |\     /|(  ___ \ 
    | (   ) )   ) (   |  \  / /| (    \/  | (    \/| (      | )   ( || (   ) )
    | (__/ /    | |   |  (_/ / | (__      | |      | |      | |   | || (__/ / 
    |  __ (     | |   |   _ (  |  __)     | |      | |      | |   | ||  __ (  
    | (  \ \    | |   |  ( \ \ | (        | |      | |      | |   | || (  \ \ 
    | )___) )___) (___|  /  \ \| (____/\  | (____/\| (____/\| (___) || )___) )
    |/ \___/ \_______/|_/    \/(_______/  (_______/(_______/(_______)|/ \___/ 


    """)
def obtener_nombre():
    nombre = input("Para empezar, dime como te llamas. ")
    return nombre

def obtener_edad():
    agno = int(input("Para preparar tu perfil, dime en qué año naciste. "))
    return 2022 - agno


def obtener_estatura():
    estatura = float(input("Cuéntame más de ti, para agregarlo a tu perfil. ¿Cuánto mides? Dámelo en metros. "))
    metros = int(estatura)
    centimetros = int( (estatura - metros)*100 )
    return (metros, centimetros)



def obtener_sexo():
    sexo = input("Por favor, ingresa tu sexo (M=Masculino, F=Femenino): ")
    while sexo != 'M' and sexo != 'm' and sexo != 'F' and sexo != 'f':
        print("Opcion incorrecta")
        print("...................................................................")
        sexo = input("Por favor, ingresa tu sexo  (M = Masculino,  F = Femenino): ")
    return sexo

def obtener_lista_amigos():
    linea = input("Muy bien. Finalmente, escribe una lista con los nombres de tus amigos, separados por una ',': ")
    amigos = linea.split(",")
    return amigos


def datos(nombre, edad, estatura_m, estatura_cm, sexo, amigos):
    print("Estos son sus datos de perfil")
    print("--------------------------------------------------")
    print("Nombre:  ", nombre)
    print("Edad:    ", edad, "años")
    print("Estatura:", estatura_m, "metros y", estatura_cm, "centímetros")
    print("Sexo: ", sexo)
    print("Amigos:   ", len(amigos))
    print("--------------------------------------------------")

def menu():

    print("Por favor seleccione una opcion del siguiente menu")
    print("  1. Escribir un mensaje")
    print("  2. Mostrar mi muro")
    print("  3. Mostrar los datos de perfil")
    print("  4. Actualizar el perfil de usuario")
    print("  0. Salir")
    opcion = int(input("Ingresa una opción: "))
    while opcion < 0 or opcion > 5:
        print("No conozco la opción que has ingresado. Inténtalo otra vez.")
        opcion = int(input("Ingresa una opción: "))
    return opcion


def obtener_mensaje():
    mensaje = input("Ahora vamos a publicar una ruta. ¿A donde vas hoy? ")
    return mensaje

def mostrar_mensaje(origen, mensaje):
    print("--------------------------------------------------")
    print(origen+":", mensaje)
    print("--------------------------------------------------")


#Muestra los mensajes recibidos
def mostrar_muro(muro):
     print("------ MURO ("+str(len(muro))+" mensajes) ---------")
     for mensaje in muro:
         print(mensaje)
     print("--------------------------------------------------")

#Publica un mensaje en el timeline personal y en el de los amigos
def publicar_mensaje(origen, amigos, mensaje, muro):
    print("--------------------------------------------------")
    print(origen, "dice:", mensaje)
    print("--------------------------------------------------")
    #Agrega el mensaje al final del timeline local
    muro.append(mensaje)
    #Agrega, al final del archivo de cada amigo, el mensaje publicado
    for amigo in amigos:
        if existe_archivo(amigo+".user"):
            archivo = open(amigo+".user","a")
            archivo.write(origen+":"+mensaje+"\n")
            archivo.close()

def existe_archivo(ruta):
    return os.path.isfile(ruta)

def leer_usuario(nombre):
    archivo_usuario = open(nombre+".user","r")
    nombre = archivo_usuario.readline().rstrip()
    edad = int(archivo_usuario.readline())
    estatura = float(archivo_usuario.readline())
    estatura_m = int(estatura)
    estatura_cm = int( (estatura - estatura_m)*100 )
    sexo = archivo_usuario.readline().rstrip()
    amigos = archivo_usuario.readline().rstrip().split(",")
    estado = archivo_usuario.readline().rstrip()
    #Lee el 'muro'. Esto es, todos los mensajes que han sido publicados en el timeline del usuario.
    muro = []
    mensaje = archivo_usuario.readline().rstrip()
    while mensaje != "":
        muro.append(mensaje)
        mensaje = archivo_usuario.readline().rstrip()
    #Una vez que hemos leido los datos del usuario no debemos olvidar cerrar el archivo
    archivo_usuario.close()
    return(nombre, edad, estatura_m, estatura_cm, sexo,amigos, estado, muro)

def escribir_usuario(nombre, edad, estatura_m, estatura_cm, sexo, amigos, estado, muro):
    archivo_usuario = open(nombre+".user","w")
    archivo_usuario.write(nombre+"\n")
    archivo_usuario.write(str(edad)+"\n")
    archivo_usuario.write(str(estatura_m + estatura_cm/100)+"\n")
    archivo_usuario.write(sexo+"\n")
    archivo_usuario.write(",".join(amigos)+"\n")
    archivo_usuario.write(estado+"\n")
    #Escribe el 'timeline' en el archivo, a continuaciÃ³n del Ãºltimo estado
    for mensaje in muro:
        archivo_usuario.write(mensaje+"\n")
    #Una vez que hemos escrito todos los datos del usuario en el archivo, no debemos olvidar cerrarlo
    archivo_usuario.close()