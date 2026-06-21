import os
import time

#lista
productos =[]

def limpiar():
    os.system("clear")

def pausar():
    time.sleep(2)
#menu
def mostrar_menu():
    print("====MENÚ PRINCIPAL====")
    print("1.Agregar producto")
    print("2.Buscar producto")
    print("3.Eliminar producto")
    print("4.Actualizar disponibilidad")
    print("5.Mostrar productos")
    print("6.Salir")

#opciones
def leer_opcion():
    try:
        opcion= int(input("Ingrese opcion:\n"))
        if opcion >= 1 and opcion <= 6:
            return opcion
        else:
            print("Opcion ingresada no existe.")
    except:
        print("El valor ingresado debe ser numerico")

#validacione
def validar_lista():
    if len(productos) <= 0:
        print("No se han registrado productos.")
        return False
    else:
        return True

def validar_entero(entero):
    if entero >= 0:
        return True
    else:
        print("El valor del producto no puede ser menor o igual a 0.")

def validar_str(string):
    if len(string) > 0:
        return True
    else:
        print("El campo no puede venir vacio.")

def validar_float(decimal):
    if isinstance(decimal,float) and decimal >= 0:
        return True
    else:
        print("El precio no puede ser menor que 0.")
#agregar cosas (opcion 1)
def agregar_producto():
    print("====Agregar Producto====")
    #nombre del producto
    while True:
        nombre= input("Ingrese nombre del producto:\n").strip()
        if validar_str(nombre):
            break
    #stock del producto
    while True:
        try:
            stock = int(input("Ingrese stock del producto:\n"))
            if validar_entero(stock):
                break
        except:
            print("El valor ingresado debe ser numerico.")
    #precio del producto
    while True:
        try:
            precio = float(input("Ingrede precio del producto:\n"))
            if validar_float(precio):
                break
        except:
            print("El valor ingresado debe ser numerico.")
    producto = {"nombre" : nombre,
                "stock" : stock,
                "precio" : precio,
                "disponible" : False

    }
    productos.append(producto)
    print("Producto agregado de manera exitosa.")
    pausar()
#Print estado producto
def estado(estado):
    if estado == True:
        print("Estado producto: DISPONIBLE.")
    else:
        print("Estado producto: SIN STOCK.")

#buscar producto (opcion 2)
def buscar_producto(buscar):
    for p in range (len(productos)): #de esta forma p tiene un valor numerico y no de todo el diccionario
        if productos[p]["nombre"] == buscar:
            return p
    return -1

def print_buscar(posicion):
    if posicion == -1:
        print("El producto buscado no se encuentra registrado")
    else: 
        print(f"Nombre producto: {productos[posicion]["nombre"]}")
        print(f"Stock disponible: {productos[posicion]["stock"]}")
        print(f"Precio producto: {productos[posicion]["precio"]}")
        estado(productos[posicion]["disponible"]) #utilizar el true o false de disponible con la funcion estado
#eliminar producto (opcion 3)
def eliminar_producto(posicion): 
    if posicion == -1:
        return True #para despues utilizar el nombre del producto en main
    else:
        productos.remove(productos[posicion])
        print("El producto ha sido eliminado.")
    

#actualizar disponibilidad (opcion 4)

def actualizar_disponibilidad():
    for p in productos:
        if p["stock"] > 0:
            p["disponible"] = True
        else:
            p["disponible"] = False


#lista de productos (opcion 5)
def mostrar_productos():
    actualizar_disponibilidad()
    for p in productos:
        print(f"Nombre producto: {p["nombre"]}")
        print(f"Stock disponible: {p["stock"]}")
        print(f"Precio producto: {p["precio"]}")
        estado(p["disponible"])
        print("*************************")
    pausar()
