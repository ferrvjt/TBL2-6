from modules.RegisterModule import (
    agregar_usuario, menu_registro,
    registrar_sueno, registrar_alimentacion,
    registrar_ejercicio, registrar_bienestar
)
from modules.StatModule import evaluar_usuario
from modules.RecommendationModule import recomendaciones, retroalimentacion

# Crear usuario
usuario = agregar_usuario()

# Cuestionario inicial
print("\n=== CUESTIONARIO INICIAL ===")
print("Responde estas preguntas sobre tu estilo de vida actual.\n")

print("--- SUEÑO ---")
horas = float(input("Cuantas horas duermes normalmente? "))
calidad = int(input("Calidad del sueño (1-5): "))
despierta = input("Te despiertas durante la noche? (s/n): ").lower() == "s"
pantalla = input("Usas pantallas antes de dormir? (s/n): ").lower() == "s"
registrar_sueno(usuario, horas, calidad, despierta, pantalla)

print("\n--- ALIMENTACIÓN ---")
comidas = int(input("Cuantas comidas saludables al dia? "))
agua = int(input("Cuantos vasos de agua al dia? "))
frutas = int(input("Porciones de frutas/verduras al dia? "))
comida_rapida = input("Comes comida rapida frecuentemente? (s/n): ").lower() == "s"
registrar_alimentacion(usuario, comidas, agua, frutas, comida_rapida)

print("\n--- EJERCICIO ---")
minutos = int(input("Minutos de ejercicio al dia? "))
print("Tipos: caminar, correr, deporte, gimnasio, otro, ninguno")
tipo = input("Tipo de actividad: ")
print("Intensidades: baja, media, alta")
intensidad = input("Intensidad: ")
registrar_ejercicio(usuario, minutos, tipo, intensidad)

print("\n--- BIENESTAR ---")
pantalla_horas = float(input("Horas frente a pantalla al dia? "))
estres = int(input("Nivel de estres (1-5): "))
registrar_bienestar(usuario, pantalla_horas, estres)

print("\nGracias! Aqui esta tu primer reporte:")
evaluar_usuario(usuario)
recomendaciones(usuario)

# Menú principal
op = 1
while op != 5:
    print("\n--- MENU PRINCIPAL ---")
    print("1. Agregar actualización diaria")
    print("2. Ver evaluación")
    print("3. Recomendaciones")
    print("4. Retroalimentación")
    print("5. Salir")
    op = int(input("Ingrese una opción: "))
    if op == 1:
        menu_registro(usuario)
    elif op == 2:
        evaluar_usuario(usuario)
    elif op == 3:
        recomendaciones(usuario)
    elif op == 4:
        retroalimentacion(usuario)
    elif op == 5:
        print("Feliz dia", usuario["nombre"], ":D")
        break
    else:
        print("Opcion invalida")