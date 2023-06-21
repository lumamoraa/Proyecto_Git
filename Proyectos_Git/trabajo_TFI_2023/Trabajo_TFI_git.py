import random
import json  

pelicula={}
peliculas=[] 
genero=["Aventuras","Acción","Animación","Comedia","Drama","Ciencia ficción","Terror","Suspenso","Romántica"]
clasificacion=["ATP","PG","PG-13","R","NC-17"]

def cargar_listado_pelicula(peliculas_json): #profe, lin.9 col.28 me dice que el parentes.No esta cerrao,porque?
    with open("peliculas.json", "r") as peliculas:
        peliculas= json.load(peliculas_json)
        peliculas=cargar_listado_pelicula("peliculas.json")
    return peliculas

def menu_principal():
    print("CINEMA+")
    print("1. ABM de películas")
    print("2. Calificación de títulos")
    print("3. Reportes y estadísticas")
    print("4. Salir")

def submenu_abm_peliculas():
    print("CINEMA+")
    print("Alta, Baja y modificación de películas")
    print("1. Alta de nueva película")
    print("2. Baja de película (eliminar)")
    print("3. Modificación de película existente")
    print("4. Volver")

def submenu_baja_pelicula(): 
    print("CINEMA+")
    print("Eliminar una película existente")
    print("1. Buscar por id")
    print("2. Buscar por título")
    print("3. Volver")

def submenu_modificacion_pelicula():
    print("CINEMA+")
    print("Modificar película existente")
    print("1. Buscar por id")
    print("2. Buscar por título")
    print("3. Volver")

def alta_nueva_pelicula():
    print("1. Alta de nueva película")
    id_pelicula = int(input("Ingrese el ID de la película: "))
    titulo = input("Ingrese el título de la película: ")
    genero= input("Ingrese el género de la película: Aventuras,Acción,Animación,Comedia,Drama,Ciencia ficción,Terror,Suspenso,Romántica: " )
    duracion = FloatingPointError(input("Ingrese la duración en minutos: "))
    sinopsis = input("Ingrese la sinopsis de la película: ")
    pais = input("Ingrese el país de origen: ")
    idioma = input("Ingrese el idioma: ")
    clasificacion =input("Ingrese una clasificación ATP – PG – PG-13 – R – NC-17 : ").lower()
    calificacion = float(input("Ingrese la calificación: "))
    disponible = input("La película está disponible (s/n): ").lower()

    pelicula = { 
        'id': id_pelicula,
        'titulo': titulo,
        'genero':genero,
        'duracion': duracion,
        'sinopsis': sinopsis,
        'pais': pais,
        'idioma': idioma,
        'clasificacion': clasificacion,
        'calificacion': calificacion,
        'disponible': disponible
    }
    peliculas.append(pelicula)
    
    with open("peliculas.json", "w") as pelicula:
         json.dump(peliculas,pelicula)
    print("La película se ha registrado exitosamente.")
    
    peliculas=alta_nueva_pelicula("peliculas.json")
        
    print(alta_nueva_pelicula)
 
def mostrar_datos_pelicula(pelicula):
    print("ID:", pelicula['id'])
    print("Título:", pelicula['titulo'])
    print("Género:", pelicula['genero'])
    print("Duración:", pelicula['duracion'], "minutos")
    print("Sinopsis:", pelicula['sinopsis'])
    print("País de origen:", pelicula['pais'])
    print("Idioma:", pelicula['idioma'])
    print("Clasificación:", pelicula['clasificacion'])
    print("Calificación:", pelicula['calificacion'])
    print("Disponible:", "Sí" if pelicula['disponible'] else "No")

def mostra_reporte_estadistica():
    print("Reportes y estadísticas")
    print("1. Listado de películas")
    print("2. Películas de mayor puntaje")
    print("3. Volver")
    print("4. Menu Principal")
    opcion = input("Ingrese la opción deseada: \n")
    if opcion == '1':
        listar_peliculas()
    elif opcion == '2':
        mostrar_peliculas_mayor_puntaje()
    elif opcion == '3':
        return
    elif opcion == '4':
        return menu_principal()
    else:
        print("Opción inválida\n")


def modificar_pelicula(): 
    print("3. Modificación de película existente")
    opcion = input("¿Desea buscar por id o por título? \n ingrese la opcion deseada (id/título): ")
    if opcion == 'id':
        id_pelicula = int(input("Ingrese el ID de la película a modificar: "))
        pelicula = buscar_pelicula_por_id (id_pelicula)
        if pelicula:
            mostrar_datos_pelicula(pelicula)
            pelicula['titulo'] = input("Ingrese el nuevo título de la película: ")
            pelicula['genero'] = input("Ingrese el nuevo género de la película: ")
            pelicula['duracion'] = int(input("Ingrese la nueva duración en minutos: "))
            pelicula['sinopsis'] = input("Ingrese la nueva sinopsis de la película: ")
            pelicula['pais'] = input("Ingrese el nuevo país de origen: ")
            pelicula['idioma'] = input("Ingrese el nuevo idioma: ")
            pelicula['clasificacion'] = input("Ingrese una clasificación ATP – PG – PG-13 – R – NC-17 : ").lower()
            pelicula['calificacion'] = int(input("Ingrese la calificación: "))
            pelicula['disponible'] = bool(input("La película está disponible (s/n): ")).lower() == input
            print("La película se ha modificado exitosamente.")
        else:
            print("No se encontró ninguna película con ese ID.")
    elif opcion == 'título':
        titulo_pelicula = input("Ingrese el título de la película a modificar: ")
        pelicula = buscar_pelicula_por_titulo(titulo_pelicula)
        if pelicula:
            mostrar_datos_pelicula(pelicula)# OPC1: en pelicula[] tiene que llevar un letra s verdad? porque es lista.
            #OPC2: OH, esta bien?/PQ el valor del input se almazena en titulo que esta dentro de una lista llamada PELICULAS
            pelicula['titulo'] = input("Ingrese el nuevo título de la película: ")
            pelicula['genero'] = input("Ingrese el nuevo género de la película: ")
            pelicula['duracion'] = int(input("Ingrese la nueva duración en minutos: "))
            pelicula['sinopsis'] = input("Ingrese la nueva sinopsis de la película: ")
            pelicula['pais'] = input("Ingrese el nuevo país de origen: ")
            pelicula['idioma'] = input("Ingrese el nuevo idioma: ")
            pelicula['clasificacion'] = input("Ingrese la nueva clasificación: ")
            pelicula['calificacion'] = float(input("Ingrese la nueva calificación: "))
            pelicula['disponible'] = input("La película está disponible (s/n): ").lower() == 's'
            print("La película se ha modificado exitosamente.")
        else:
            print("No se encontró ninguna película con ese título.")
    else:
        print("Opción inválida.")

# RTA: AL COMENTARIO 5, 
# Usted me dice si estoy equivocado.
# LAS FUNCIONES QUE DEBO LLEVAR ASI ARRIBA SON: las que no resiven parametro ni condiciones (modulos).? es decir:
# funciones que solo contienen print.?
# ** Comentario 5: Todas las funciones deben estar definidas al principio del programa **#
def submenu_baja_pelicula(): # Aca hay un modulo anidado y en su COMENTARIO Nº6. RTA: En cual de todas las clases :)
    print("2. Baja de película")
    opcion = input("¿Desea buscar por id o por título de Pelicula?\nIngrese una Respuesta (id/título): ")
    if opcion == 'id':
        id_pelicula = int(input("Ingrese el ID de la película a eliminar:  "))
        pelicula = buscar_pelicula_por_id(id_pelicula)
        if pelicula:
            mostrar_datos_pelicula(pelicula)
            peliculas.remove(pelicula)
            print("La película se ha eliminado exitosamente.")
        else:
            print("No se encontró ninguna película con ese ID.")
    elif opcion == 'título':
        titulo_pelicula = input("Ingrese el título de la película a eliminar: ")
        pelicula = buscar_pelicula_por_titulo(titulo_pelicula)
        #** Comentario 6: Deberías en peliculas trabajar cómo vimos en clase por si hay varias peliculas con titulos similares, para elegir entre una de las que se elijan**#
        if pelicula:
            mostrar_datos_pelicula(pelicula)
            peliculas.remove(pelicula) # porque remove me aparece en color blanco.(yo tengo como extencion prettier)
            print("La película se ha eliminado exitosamente.")
        else:
            print("No se encontró ninguna película con ese título.")
    else:
        print("Opción inválida.")

def buscar_pelicula_por_id(id_pelicula): 
    for pelicula in peliculas:
        if pelicula['id'] == id_pelicula: #** Comentario 7: Acá estás usando peliculas y debe ser pelicula. #**
            #** pelicula['id']  -------------> Si la "s" final, porque estás accediendo a un elemento. **#
            return pelicula
    return None 

def buscar_pelicula_por_titulo(titulo_pelicula):
    for pelicula in peliculas:
        if pelicula['titulo'].lower() == titulo_pelicula.lower():
            return pelicula
    return None 

def calificar_titulos():
    print("Calificación de títulos")
    num_iteraciones = 0
    peliculas_random = random.sample(peliculas, num_iteraciones)
    for pelicula in peliculas_random:
        mostrar_datos_pelicula(pelicula)
        calificacion = input("Ingrese la calificación para esta película (1-10) o 's' para saltar: ")
        if calificacion == 's':
            continue
        try:
            calificacion = float(calificacion)
            if calificacion < 0 or calificacion > 10: # aca puse de cero a diez. haciendo alusion,a una calif. de mal a excelente.
                print("Calificación inválida. Se saltará esta película.")
                continue
            pelicula['calificacion'] = calificacion
            print("La calificación se ha registrado exitosamente.")
        except ValueError:
            print("Calificación inválida. Se saltará esta película.")


def listar_peliculas():
    print("Listado de películas")
    peliculas_ordenadas = sorted(peliculas, key=lambda pelicula: pelicula['titulo'])
    for pelicula in peliculas_ordenadas:
        print("Título:", pelicula['titulo'])
        #print("Género(s):", pelicula['genero'])
        #print("Calificación:", pelicula['calificacion'])
        print()

def mostrar_peliculas_mayor_puntaje():
    print("Películas de mayor puntaje")
    peliculas_ordenadas = sorted(peliculas, key=lambda pelicula: pelicula['calificacion'], reverse=True)
    for pelicula in peliculas_ordenadas:
        print("Título:", pelicula['titulo'])
        print("Calificación:", pelicula['calificacion'])
        print()

def imprimir_histograma_porcentaje_disponibilidad():
    total_peliculas = len(peliculas)
    disponibles = sum(pelicula['disponible'] for pelicula in peliculas)
    no_disponibles = total_peliculas - disponibles
    porcentaje_disponibles = disponibles / total_peliculas * 100
    porcentaje_no_disponibles = no_disponibles / total_peliculas * 100

    print("Porcentaje de películas disponibles:")
    print("Disponibles: " + "*" * int(porcentaje_disponibles))
    print("No disponibles: " + "*" * int(porcentaje_no_disponibles))
    print()

def salir():
    opcion = input("¿Está seguro de que desea salir? (s/n): ")
    if opcion.lower() == 's':
        print("Gracias por usar CINEMA+. ¡Hasta luego!")
        return True
    return False

#with open("peliculas.json", "w") as pelicula:# es solo un ej x
#   peliculas = json.load(pelicula)
# print(peliculas)

#          ---ACA COMIEZA LA EJECUCION DEL PROGRAMA--- 
def ejecutar_cinema_plus():
    while True:
        menu_principal()
        opcion_principal = input("Ingrese la opción deseada: \n")
        if opcion_principal == '1':

            while True:
                submenu_abm_peliculas()
                opcion_abm = input("Ingrese la opción deseada: \n")
                if opcion_abm == '1':
                    alta_nueva_pelicula()
                elif opcion_abm == '2':
                    submenu_baja_pelicula()
                elif opcion_abm == '3':
                    modificar_pelicula()
                elif opcion_abm == '4':
                    break
                else:
                    print("Opción inválida.")

        elif opcion_principal == '2':
            calificar_titulos()
        elif opcion_principal == '3':
            while True: 
                mostra_reporte_estadistica()
                opcion_reportes = input("Ingrese la opción deseada: \n")
                if opcion_reportes == '1':
                    print:(listar_peliculas())
                    print("\n")
                elif opcion_reportes == '2':
                    mostrar_peliculas_mayor_puntaje()
                elif opcion_reportes == '3':
                    break
                elif opcion_reportes == '4':
                    menu_principal()
                else:
                    print("Opción inválida.")
        elif opcion_principal == '4':
            if salir():
                break
        else:
            print("Opción inválida.")

ejecutar_cinema_plus()
