"""
Stat-Module
David Morente
261443
Descripción: Módulo de evaluación del estado de usuario

"""

# Función para calcular el promedio de un campo numérico
def calcular_promedio(lista, clave):
    if len(lista) == 0:
        return 0

    suma = 0
    for dato in lista:
        suma = suma + dato[clave]

    return suma / len(lista)


# Contar cuantos True hay en una lista
def contar_true(lista, clave):
    cantidad = 0
    for dato in lista:
        if dato[clave] == True:
            cantidad = cantidad + 1
    return cantidad


# Evaluación de sueño (max 100 puntos)
def evaluar_sueno(usuario):
    registros = usuario["habitos"]["sueno"]
    if len(registros) == 0:
        return 0

    puntos = 0

    # Horas de sueño (max 30)
    prom_horas = calcular_promedio(registros, "horas")
    if prom_horas >= 7 and prom_horas <= 9:
        puntos = puntos + 30
    elif prom_horas >= 6:
        puntos = puntos + 20
    elif prom_horas >= 5:
        puntos = puntos + 10

    # Calidad del sueño (max 30)
    prom_calidad = calcular_promedio(registros, "calidad")
    if prom_calidad >= 4:
        puntos = puntos + 30
    elif prom_calidad >= 3:
        puntos = puntos + 20
    elif prom_calidad >= 2:
        puntos = puntos + 10

    # No despertarse (max 20)
    veces_despierta = contar_true(registros, "despierta")
    if veces_despierta == 0:
        puntos = puntos + 20
    elif veces_despierta <= len(registros) / 2:
        puntos = puntos + 10

    # No usar pantallas (max 20)
    veces_pantalla = contar_true(registros, "pantalla")
    if veces_pantalla == 0:
        puntos = puntos + 20
    elif veces_pantalla <= len(registros) / 2:
        puntos = puntos + 10

    return puntos


# Evaluación de alimentación (max 100 puntos)
def evaluar_alimentacion(usuario):
    registros = usuario["habitos"]["alimentacion"]
    if len(registros) == 0:
        return 0

    puntos = 0

    # Comidas saludables (max 30)
    prom_comidas = calcular_promedio(registros, "comidas")
    if prom_comidas >= 3:
        puntos = puntos + 30
    elif prom_comidas >= 2:
        puntos = puntos + 20
    elif prom_comidas >= 1:
        puntos = puntos + 10

    # Agua (max 25)
    prom_agua = calcular_promedio(registros, "agua")
    if prom_agua >= 8:
        puntos = puntos + 25
    elif prom_agua >= 5:
        puntos = puntos + 15
    elif prom_agua >= 3:
        puntos = puntos + 5

    # Frutas y verduras (max 25)
    prom_frutas = calcular_promedio(registros, "frutas")
    if prom_frutas >= 5:
        puntos = puntos + 25
    elif prom_frutas >= 3:
        puntos = puntos + 15
    elif prom_frutas >= 1:
        puntos = puntos + 5

    # No comida rapida (max 20)
    veces_rapida = contar_true(registros, "comida_rapida")
    if veces_rapida == 0:
        puntos = puntos + 20
    elif veces_rapida <= len(registros) / 2:
        puntos = puntos + 10

    return puntos


# Evaluación de ejercicio (max 100 puntos)
def evaluar_ejercicio(usuario):
    registros = usuario["habitos"]["ejercicio"]
    if len(registros) == 0:
        return 0

    puntos = 0

    # Minutos de ejercicio (max 40)
    prom_minutos = calcular_promedio(registros, "minutos")
    if prom_minutos >= 30:
        puntos = puntos + 40
    elif prom_minutos >= 20:
        puntos = puntos + 25
    elif prom_minutos >= 10:
        puntos = puntos + 15

    # Intensidad del ultimo registro (max 30)
    ultimo_registro = registros[len(registros) - 1]
    if ultimo_registro["intensidad"] == "alta":
        puntos = puntos + 30
    elif ultimo_registro["intensidad"] == "media":
        puntos = puntos + 20
    elif ultimo_registro["intensidad"] == "baja":
        puntos = puntos + 10

    # Tipo de actividad (max 30)
    if ultimo_registro["tipo"] != "ninguno":
        puntos = puntos + 30

    return puntos


# Evaluación de bienestar (max 100 puntos)
def evaluar_bienestar(usuario):
    registros = usuario["habitos"]["bienestar"]
    if len(registros) == 0:
        return 0

    puntos = 0

    # Horas de pantalla - menos es mejor (max 50)
    prom_pantalla = calcular_promedio(registros, "pantalla_horas")
    if prom_pantalla <= 2:
        puntos = puntos + 50
    elif prom_pantalla <= 4:
        puntos = puntos + 35
    elif prom_pantalla <= 6:
        puntos = puntos + 20
    elif prom_pantalla <= 8:
        puntos = puntos + 10

    # Estrés - menos es mejor (max 50)
    prom_estres = calcular_promedio(registros, "estres")
    if prom_estres <= 1:
        puntos = puntos + 50
    elif prom_estres <= 2:
        puntos = puntos + 40
    elif prom_estres <= 3:
        puntos = puntos + 25
    elif prom_estres <= 4:
        puntos = puntos + 10

    return puntos


# Rendimiento (retorna texto, no imprime)
def rendimiento(puntos):
    if puntos >= 80:
        return "Excelente"
    elif puntos >= 60:
        return "Bueno"
    elif puntos >= 40:
        return "Regular"
    else:
        return "Deficiente"


# Evaluacion general con cruce de categorias
def evaluar_general(usuario):
    puntos_sueno = evaluar_sueno(usuario)
    puntos_alimentacion = evaluar_alimentacion(usuario)
    puntos_ejercicio = evaluar_ejercicio(usuario)
    puntos_bienestar = evaluar_bienestar(usuario)

    promedio = (puntos_sueno + puntos_alimentacion + puntos_ejercicio + puntos_bienestar) / 4

    # Penalizacion si sueno y ejercicio son bajos
    if puntos_sueno < 40 and puntos_ejercicio < 40:
        promedio = promedio - 5

    # Penalizacion si alimentacion y bienestar son bajos
    if puntos_alimentacion < 40 and puntos_bienestar < 40:
        promedio = promedio - 5

    if promedio < 0:
        promedio = 0

    return round(promedio)


# Mostrar evaluación (consola)
def evaluar_usuario(usuario):
    print("\n--- EVALUACION DEL USUARIO ---")

    puntos_sueno = evaluar_sueno(usuario)
    puntos_alimentacion = evaluar_alimentacion(usuario)
    puntos_ejercicio = evaluar_ejercicio(usuario)
    puntos_bienestar = evaluar_bienestar(usuario)

    print("Sueño:", puntos_sueno, "-", rendimiento(puntos_sueno))
    print("Alimentación:", puntos_alimentacion, "-", rendimiento(puntos_alimentacion))
    print("Ejercicio:", puntos_ejercicio, "-", rendimiento(puntos_ejercicio))
    print("Bienestar:", puntos_bienestar, "-", rendimiento(puntos_bienestar))

    promedio = evaluar_general(usuario)
    print("Estado general:", promedio, "-", rendimiento(promedio))