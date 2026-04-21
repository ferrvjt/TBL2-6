from modules.RegisterModule import agregar_usuario, menu_registro
from modules.StatModule import evaluar_usuario

op = 1

usuario = agregar_usuario()

while op != "3":
    print("\n--- MENU PRINCIPAL ---")
    print("1. Registrar hábitos")
    print("2. Evaluar usuario")
    print("3. Salir")
    op = input("Ingrese una opción: ")
    if op == "1":
        menu_registro(usuario)
    elif op == "2":
        evaluar_usuario(usuario)
    elif op == "3":
        print("Feliz día", usuario["nombre"], ":D")
        break
    else:
        print("Opcion invalida")