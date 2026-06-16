import os
import time

#lista
productos =[]

def limpiar():
    os.system("cls")

def pausar():
    time.sleep(2)

#validaciones
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

#agregar cosas
def agregar_producto(producto):
    while True:
        nombre= input("Ingrese nombre del producto:\n")
        if validar_str(nombre):
            break

def agregar_stock(stock):
    while True:
        cantidad = int(input("Ingrese stock del producto:\n"))
        if validar_entero(cantidad):
            break


