import numpy
import colorama
from colorama import Style,Fore,Back

def printv(texto):
    print(f"{Fore.GREEN}{Style.BRIGHT}{texto}{Back.BLACK}{Fore.RESET}{Style.RESET_ALL}")

def printr(texto):
    print(f"{Fore.RED}{Style.BRIGHT}{texto}{Back.BLACK}{Fore.RESET}{Style.RESET_ALL}")

edificio=numpy.empty([10,4],object)

def mostraredificio(edificio):
    print(edificio)

def comprar():
    while True:
        piso=int(input("Ingrese el piso que desea : "))
        numero=int(input("Ingrese el numero de departamento : "))

        if edificio[piso][numero]=="X":
            printr(f"El edificio seleccionado ya se encuentra ocupado")
        else:
            edificio[piso][numero]=="X"
            mostraredificio(edificio)
            printv(f"Edificio comprado exitosamente")