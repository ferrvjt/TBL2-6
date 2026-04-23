"""
Recommendation-Module
Nery de la Cruz
261233
Descripción: Módulo de recomendación de hábitos saludables

"""

from modules.StatModule import (
    evaluar_sueno, evaluar_alimentacion, evaluar_ejercicio,
    evaluar_bienestar, evaluar_general, calcular_promedio,
    contar_true, rendimiento
)


# Obtener recomendaciones segun los datos del usuario
def obtener_recomendaciones(usuario):
    lista = []

    # Sueno
    reg_s = usuario["habitos"]["sueno"]
    if len(reg_s) > 0:
        if calcular_promedio(reg_s, "horas") < 7:
            lista.append({"categoria": "Sueno", "mensaje": "Intenta dormir entre 7 y 9 horas diarias.", "tipo": "warning"})
        else:
            lista.append({"categoria": "Sueno", "mensaje": "Tus horas de sueno estan en buen rango.", "tipo": "success"})
        if calcular_promedio(reg_s, "calidad") < 3:
            lista.append({"categoria": "Sueno", "mensaje": "Tu calidad de sueno es baja. Crea una rutina relajante antes de dormir.", "tipo": "warning"})
        if contar_true(reg_s, "despierta") > len(reg_s) / 2:
            lista.append({"categoria": "Sueno", "mensaje": "Te despiertas mucho en la noche. Evita cafeina despues de las 2 PM.", "tipo": "warning"})
        if contar_true(reg_s, "pantalla") > len(reg_s) / 2:
            lista.append({"categoria": "Sueno", "mensaje": "Evita usar pantallas al menos 1 hora antes de dormir.", "tipo": "warning"})

    # Alimentacion
    reg_a = usuario["habitos"]["alimentacion"]
    if len(reg_a) > 0:
        if calcular_promedio(reg_a, "comidas") < 3:
            lista.append({"categoria": "Alimentacion", "mensaje": "Come al menos 3 comidas saludables al dia.", "tipo": "warning"})
        else:
            lista.append({"categoria": "Alimentacion", "mensaje": "Buen numero de comidas saludables.", "tipo": "success"})
        if calcular_promedio(reg_a, "agua") < 8:
            lista.append({"categoria": "Alimentacion", "mensaje": "Toma al menos 8 vasos de agua al dia.", "tipo": "warning"})
        if calcular_promedio(reg_a, "frutas") < 3:
            lista.append({"categoria": "Alimentacion", "mensaje": "Incluye mas frutas y verduras (al menos 3 porciones).", "tipo": "warning"})
        if contar_true(reg_a, "comida_rapida") > len(reg_a) / 2:
            lista.append({"categoria": "Alimentacion", "mensaje": "Reduce la comida rapida. Cocina en casa cuando puedas.", "tipo": "warning"})

    # Ejercicio
    reg_e = usuario["habitos"]["ejercicio"]
    if len(reg_e) > 0:
        if calcular_promedio(reg_e, "minutos") < 30:
            lista.append({"categoria": "Ejercicio", "mensaje": "Haz al menos 30 minutos de actividad fisica al dia.", "tipo": "warning"})
        else:
            lista.append({"categoria": "Ejercicio", "mensaje": "Buen nivel de actividad fisica.", "tipo": "success"})
        ultimo = reg_e[len(reg_e) - 1]
        if ultimo["tipo"] == "ninguno":
            lista.append({"categoria": "Ejercicio", "mensaje": "Prueba caminar, correr, deporte o gimnasio.", "tipo": "warning"})

    # Bienestar
    reg_b = usuario["habitos"]["bienestar"]
    if len(reg_b) > 0:
        if calcular_promedio(reg_b, "pantalla_horas") > 6:
            lista.append({"categoria": "Bienestar", "mensaje": "Muchas horas de pantalla. Toma descansos cada 30 minutos.", "tipo": "warning"})
        if calcular_promedio(reg_b, "estres") > 3:
            lista.append({"categoria": "Bienestar", "mensaje": "Tu estres es alto. Prueba tecnicas de relajacion.", "tipo": "warning"})
        elif calcular_promedio(reg_b, "estres") <= 2:
            lista.append({"categoria": "Bienestar", "mensaje": "Buen manejo del estres.", "tipo": "success"})

    return lista


# Retroalimentacion general
def obtener_retroalimentacion(usuario):
    puntos_sueno = evaluar_sueno(usuario)
    puntos_alimentacion = evaluar_alimentacion(usuario)
    puntos_ejercicio = evaluar_ejercicio(usuario)
    puntos_bienestar = evaluar_bienestar(usuario)
    promedio = evaluar_general(usuario)

    if promedio >= 80:
        mensaje = "Excelente! Llevas un estilo de vida muy saludable."
        nivel = "excelente"
    elif promedio >= 60:
        mensaje = "Vas por buen camino, pero puedes mejorar."
        nivel = "bueno"
    elif promedio >= 40:
        mensaje = "Necesitas mejorar tus habitos."
        nivel = "regular"
    else:
        mensaje = "Es importante hacer cambios en tu estilo de vida."
        nivel = "deficiente"

    return {"sueno": puntos_sueno, "alimentacion": puntos_alimentacion, "ejercicio": puntos_ejercicio, "bienestar": puntos_bienestar,
            "promedio": promedio, "nivel": nivel, "mensaje": mensaje}


# Funciones para consola (compatibilidad con main.py)
def recomendaciones(usuario):
    print("\n--- RECOMENDACIONES ---")
    lista = obtener_recomendaciones(usuario)

    if len(lista) == 0:
        print("No hay datos suficientes para recomendaciones.")
        return

    for rec in lista:
        if rec["tipo"] == "warning":
            print("! " + rec["categoria"] + ": " + rec["mensaje"])
        else:
            print("+ " + rec["categoria"] + ": " + rec["mensaje"])


def retroalimentacion(usuario):
    print("\n--- RETROALIMENTACIÓN ---")
    retro = obtener_retroalimentacion(usuario)

    print("Sueño:", retro["sueno"], "pts -", rendimiento(retro["sueno"]))
    print("Alimentación:", retro["alimentacion"], "pts -", rendimiento(retro["alimentacion"]))
    print("Ejercicio:", retro["ejercicio"], "pts -", rendimiento(retro["ejercicio"]))
    print("Bienestar:", retro["bienestar"], "pts -", rendimiento(retro["bienestar"]))
    print("\nEstado general:", retro["promedio"], "pts -", retro["nivel"].upper())
    print(retro["mensaje"])