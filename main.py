from modules.RegisterModule import agregar_usuario, menu_registro
from modules.StatModule import evaluar_usuario
from modules.RecommendationModule import recomendaciones, retroalimentacion

op = 1

usuario = agregar_usuario()

while op != 5:
    print("\n--- MENU PRINCIPAL ---")
    print("1. Registrar hábitos")
    print("2. Evaluar usuario")
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
        print("Feliz día", usuario["nombre"], ":D")
        break
    else:
        print("Opcion invalida")