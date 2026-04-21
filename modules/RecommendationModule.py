"""
Recommendation-Module
Nery de la Cruz
261233
Descripción: Módulo de recomendación de hábitos saludables

"""

from modules.StatModule import evaluar_alimentacion, evaluar_ejercicio, evaluar_sueno

# Funcion de recomendaciones y retroalimentacion
def recomendaciones(usuario):
    print("\n--- RECOMENDACIONES ---")

    puntos_sueno = evaluar_sueno(usuario)
    puntos_alimentacion = evaluar_alimentacion(usuario)
    puntos_ejercicio = evaluar_ejercicio(usuario)

    if puntos_sueno < 60:
        print("Sueño: Debes dormir más horas.")
    else:
        print("Sueño: Vas bien.")

    if puntos_alimentacion < 60:
        print("Alimentacion: Mejora tus comidas saludables.")
    else:
        print("Alimentacion: Buen trabajo.")

    if puntos_ejercicio < 60:
        print("Ejercicio: Necesitas hacer más actividad física.")
    else:
        print("Ejercicio: Buen nivel de actividad.")

def retroalimentacion(usuario):
    print("\n--- RETROALIMENTACION ---")

    puntos_sueno = evaluar_sueno(usuario)
    puntos_alimentacion = evaluar_alimentacion(usuario)
    puntos_ejercicio = evaluar_ejercicio(usuario)

    promedio = (puntos_sueno + puntos_alimentacion + puntos_ejercicio) / 3

    if promedio >= 80:
        print("Estas llevando un estilo de vida saludable.")
    elif promedio >= 60:
        print("Vas bien, pero puedes mejorar.")
    elif promedio >= 40:
        print("Necesitas mejorar tus habitos.")
    else:
        print("Debes hacer cambios importantes en tu estilo de vida.")