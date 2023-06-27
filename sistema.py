import funciones as fu

while True:
    fu.limpiarpantalla()
    fu.printv("""
    1) VER EDIFICIO
    2) COMPRAR EDIFICIO
    3) BUSCAR DUEÑO
    4) TOTAL DE GANACIAS
    5) SALIR
    """)
    opcion = int(input("Seleccione una opción: "))

    if opcion == 5:
        break
    elif opcion == 1:
        fu.mostraredificio()
    elif opcion == 2:
        fu.comprar()
    elif opcion == 3:
        rut = int(input("Ingrese el RUT del cliente a buscar: "))
        cliente = fu.buscar_cliente(rut)
        if cliente:
            print(f"Cliente encontrado - RUT: {cliente['rut']}, Nombre: {cliente['nombre']}, Piso: {cliente['piso']}, Número: {cliente['numero']}")
        else:
            fu.printr("Cliente no encontrado.")
    elif opcion == 4:
        fu.mostrar_ganancias()
    else:
        fu.printr("Opcion NO VALIDA")
