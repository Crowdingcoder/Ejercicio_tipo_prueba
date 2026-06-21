from functions import *
limpiar()
banderita = True

print("Bienvenido a nuestro programiregistrador de productos.\n")
while banderita:
    mostrar_menu()
    opcion = leer_opcion()
    if opcion == 1:
        agregar_producto()
    elif opcion == 2:
        print("====Buscar Producto====\n")
        if validar_lista():
            buscar = input("Ingrese producto a buscar:\n").strip()
            posicion = buscar_producto(buscar)
            print_buscar(posicion)
    elif opcion == 3:
        print("====Eliminar Producto====")
        if validar_lista():
            eliminar = input("Ingrese producto a eliminar:\n").strip()
            posicion = buscar_producto(eliminar)
            eliminar_producto(posicion)
            if eliminar_producto(posicion): #si es verdadero se realiza esto
                print(f"El producto {eliminar} no se encuentra registrado.") #asi podemos decir el nmbre del producto a buscar
            pausar()
    elif opcion == 4:
        print("====Actualizar Disponibilidad====")
        if validar_lista():
            actualizar_disponibilidad()
            print("Disponibilidad actualizada.")
        pausar()
    elif opcion == 5:
        print("====Mostrar Productos")
        if validar_lista():
            mostrar_productos()
    elif opcion == 6:
        banderita = False
        limpiar()
        print("Gracias por usar el sistema. Vuelva Pronto.")
