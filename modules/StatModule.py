"""
Register-Module
David Morente
261443
Descripción: Módulo de evaluación del estado de usuario

"""

# Función para calcular el promedio
def calcular_promedio(lista, clave):
    if len(lista) == 0:
        return 0

    suma = 0
    for dato in lista:
        suma = suma + dato[clave]

    return suma / len(lista)

# Funciones de evaluación
def evaluar_sueno(usuario):
    promedio = calcular_promedio(usuario["habitos"]["sueno"], "horas")

    if promedio >= 7 and promedio <= 9:
        puntos = 100
    elif promedio >= 6:
        puntos = 80
    elif promedio >= 5:
        puntos = 60
    else:
        puntos = 30

    return puntos

def evaluar_alimentacion(usuario):
    promedio = calcular_promedio(usuario["habitos"]["alimentacion"], "comidas_saludables")

    if promedio >= 3:
        puntos = 100
    elif promedio >= 2:
        puntos = 70
    elif promedio >= 1:
        puntos = 40
    else:
        puntos = 10

    return puntos

def evaluar_ejercicio(usuario):
    promedio = calcular_promedio(usuario["habitos"]["ejercicio"], "minutos")

    if promedio >= 30:
        puntos = 100
    elif promedio >= 20:
        puntos = 80
    elif promedio >= 10:
        puntos = 60
    else:
        puntos = 30

    return puntos

# Función para calcular el rendimiento
def rendimiento(puntos):
    if puntos >= 80:
        return "Excelente"
    elif puntos >= 60:
        return "Bueno"
    elif puntos >= 40:
        return "Regular"
    else:
        return "Deficiente"

# Mostrar la evaluación
def evaluar_usuario(usuario):
    print("\n--- EVALUACION DEL USUARIO ---")

    puntos_sueno = evaluar_sueno(usuario)
    puntos_alimentacion = evaluar_alimentacion(usuario)
    puntos_ejercicio = evaluar_ejercicio(usuario)

    print("Sueño:", puntos_sueno, "-", rendimiento(puntos_sueno))
    print("Alimentacion:", puntos_alimentacion, "-", rendimiento(puntos_alimentacion))
    print("Ejercicio:", puntos_ejercicio, "-", rendimiento(puntos_ejercicio))

    promedio_total = int((puntos_sueno + puntos_alimentacion + puntos_ejercicio) / 3)

    print("Estado general:", promedio_total, "-", rendimiento(promedio_total))