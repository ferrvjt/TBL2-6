"""
Register-Module
Fernando Tomás
261329
Descripción: Módulo de registro de hábitos saludables

"""

# Agregar usuario
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
            "ejercicio": []
        }
    }
    return usuario


#Validaciones
def validar_horas_sueno(horas):
    return 0 <= horas <= 24


def validar_numero(valor):
    return valor >= 0


# Funciones de registro
def registrar_sueno(usuario, horas):
    if validar_horas_sueno(horas):
        registro = {
            "horas": horas
        }
        usuario["habitos"]["sueno"].append(registro)
        return True
    return False


def registrar_alimentacion(usuario, comidas_saludables):
    if validar_numero(comidas_saludables):
        registro = {
            "comidas_saludables": comidas_saludables
        }
        usuario["habitos"]["alimentacion"].append(registro)
        return True
    return False


def registrar_ejercicio(usuario, minutos):
    if validar_numero(minutos):
        registro = {
            "minutos": minutos
        }
        usuario["habitos"]["ejercicio"].append(registro)
        return True
    return False


# Ver registros
def mostrar_registros(usuario):
    print(f"\nHistorial de {usuario['nombre']}")

    for tipo, registros in usuario["habitos"].items():
        print(f"\n{tipo.upper()}:")

        if len(registros) == 0:
            print("  Sin registros")
        else:
            for i, dato in enumerate(registros):
                print(f"  Día {i+1}: {dato}")


# Select del registro
def menu_registro(usuario):
    while True:
        print("\n--- REGISTRO DE HÁBITOS ---")
        print("1. Registrar sueño")
        print("2. Registrar alimentación")
        print("3. Registrar ejercicio")
        print("4. Ver registros")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            horas = float(input("Ingrese horas de sueño: "))
            if registrar_sueno(usuario, horas):
                print("Registro guardado")
            else:
                print("Dato inválido")

        elif opcion == "2":
            comidas = int(input("Número de comidas saludables: "))
            if registrar_alimentacion(usuario, comidas):
                print("Registro guardado")
            else:
                print("Dato inválido")

        elif opcion == "3":
            minutos = int(input("Minutos de ejercicio: "))
            if registrar_ejercicio(usuario, minutos):
                print("Registro guardado")
            else:
                print("Dato inválido")

        elif opcion == "4":
            mostrar_registros(usuario)

        elif opcion == "5":
            print("Saliendo del registro...")
            break

        else:
            print("Opción inválida")