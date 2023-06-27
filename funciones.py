import numpy as np
import colorama
from colorama import Style, Fore, Back
import os
import msvcrt

edificio = np.empty([10, 4], dtype=object)
edificio[edificio == None] = "DISPONIBLE"

clientes = []

def limpiarpantalla():
    print(Fore.RED + "<<<PRESIONE UNA TECLA PARA CONTINUAR>>>")
    msvcrt.getch()
    os.system("cls")

def printcolor(texto):
    print(Fore.LIGHTGREEN_EX + Style.BRIGHT + texto + Back.BLACK + Fore.RESET + Style.RESET_ALL)

def printv(texto):
    print(Fore.GREEN + Style.BRIGHT + texto + Back.BLACK + Fore.RESET + Style.RESET_ALL)

def printr(texto):
    print(Fore.RED + Style.BRIGHT + texto + Back.BLACK + Fore.RESET + Style.RESET_ALL)

def mostraredificio():
    print(edificio)

def comprar():
    while True:
        piso = int(input("Ingrese el piso que desea: "))
        numero = int(input("Ingrese el numero de departamento: "))
        
        if piso >= 8:
            precio = 200
        elif piso < 8:
            precio = 150
        
        rut = int(input("Ingrese su RUT para continuar con la compra: "))
        nombre = input("Ingrese su Nombre: ")
        
        if edificio[piso][numero] == "VENDIDO":
            piso += 1
            numero += 1
            printr("El edificio seleccionado ya se encuentra ocupado")
        else:
            edificio[piso][numero] = "VENDIDO"
            clientes.append({"piso": piso, "numero": numero, "rut": rut, "nombre": nombre})
            mostraredificio()
            printv("Edificio comprado exitosamente")
            break

def buscar_cliente(rut):
    for cliente in clientes:
        if cliente["rut"] == rut:
            return cliente
    return None

def mostrar_clientes():
    if len(clientes) > 0:
        print("Lista de clientes:")
        for cliente in clientes:
            print(f"RUT: {cliente['rut']}, Nombre: {cliente['nombre']}, Piso: {cliente['piso']}, Número: {cliente['numero']}")
    else:
        printr("No hay clientes registrados.")

def ganancias():
    total_ganancias = 0
    for i in range(10):
        for j in range(4):
            piso = edificio[i, j]
            if piso == "VENDIDO":
                if i >= 8:
                    total_ganancias += 200
                else:
                    total_ganancias += 150
    return total_ganancias

def mostrar_ganancias():
    total = ganancias()
    printcolor(f"Ganancias totales: {total} Millones")
