"""
Register-Module
Fernando Tomás
261329
Descripción: Módulo de registro de hábitos saludables

"""

# Agregar usuario (consola)
def agregar_usuario():
    nombre = input("Ingrese nombre: ")
    edad = int(input("Ingrese edad: "))
    return crear_usuario(nombre, edad)


# Inicialización del usuario
def crear_usuario(nombre, edad):
    usuario = {
        "nombre": nombre,
        "edad": edad,
        "habitos": {
            "sueno": [],
            "alimentacion": [],
            "ejercicio": [],
            "bienestar": []
        }
    }
    return usuario


# Validacion
def validar_rango(valor, minimo, maximo):
    return minimo <= valor <= maximo


# Registrar sueno
def registrar_sueno(usuario, horas, calidad, despierta, pantalla):
    if validar_rango(horas, 0, 24) and validar_rango(calidad, 1, 5):
        registro = {"horas": horas, "calidad": calidad, "despierta": despierta, "pantalla": pantalla}
        usuario["habitos"]["sueno"].append(registro)
        return True
    return False


# Registrar alimentacion
def registrar_alimentacion(usuario, comidas, agua, frutas, comida_rapida):
    if comidas >= 0 and agua >= 0 and frutas >= 0:
        registro = {"comidas": comidas, "agua": agua, "frutas": frutas, "comida_rapida": comida_rapida}
        usuario["habitos"]["alimentacion"].append(registro)
        return True
    return False


# Registrar ejercicio
def registrar_ejercicio(usuario, minutos, tipo, intensidad):
    if minutos >= 0:
        registro = {"minutos": minutos, "tipo": tipo, "intensidad": intensidad}
        usuario["habitos"]["ejercicio"].append(registro)
        return True
    return False


# Registrar bienestar
def registrar_bienestar(usuario, pantalla_horas, estres):
    if pantalla_horas >= 0 and validar_rango(estres, 1, 5):
        registro = {"pantalla_horas": pantalla_horas, "estres": estres}
        usuario["habitos"]["bienestar"].append(registro)
        return True
    return False


# Menu de registro (consola)
def menu_registro(usuario):
    while True:
        print("\n--- REGISTRO ---")
        print("1. Sueno  2. Alimentacion  3. Ejercicio  4. Bienestar  5. Salir")
        opcion = input("Opcion: ")

        if opcion == "1":
            horas = float(input("Horas de sueno: "))
            calidad = int(input("Calidad (1-5): "))
            despierta = input("Te despertaste? (s/n): ").lower() == "s"
            pantalla = input("Pantallas antes de dormir? (s/n): ").lower() == "s"
            print("Guardado" if registrar_sueno(usuario, horas, calidad, despierta, pantalla) else "Dato invalido")

        elif opcion == "2":
            comidas = int(input("Comidas saludables: "))
            agua = int(input("Vasos de agua: "))
            frutas = int(input("Frutas/verduras: "))
            rapida = input("Comida rapida? (s/n): ").lower() == "s"
            print("Guardado" if registrar_alimentacion(usuario, comidas, agua, frutas, rapida) else "Dato invalido")

        elif opcion == "3":
            minutos = int(input("Minutos de ejercicio: "))
            tipo = input("Tipo (caminar/correr/deporte/gimnasio/ninguno): ")
            intensidad = input("Intensidad (baja/media/alta): ")
            print("Guardado" if registrar_ejercicio(usuario, minutos, tipo, intensidad) else "Dato invalido")

        elif opcion == "4":
            horas_pantalla = float(input("Horas de pantalla: "))
            estres = int(input("Estres (1-5): "))
            print("Guardado" if registrar_bienestar(usuario, horas_pantalla, estres) else "Dato invalido")

        elif opcion == "5":
            break
        else:
            print("Opcion invalida")