def generar_varias_tablas():
    tabla_actual = 1
    cantidad_tablas = int(input("\nCuantas tablas deseas generar: "))

    while tabla_actual <= cantidad_tablas:
        multiplicador = 10
        while multiplicador >= 1:
            print(f"{tabla_actual} x {multiplicador} = {tabla_actual * multiplicador}")
            multiplicador -= 1
        input("Pulse enter para continuar")
        tabla_actual += 1


def generar_tabla_especifica():
    multiplicador = 1
    numero = int(input("\nDigite un numero para generar su tabla de multiplicar: "))

    while multiplicador <= 12:
        print(f"{numero} x {multiplicador} = {numero * multiplicador}")
        multiplicador += 1

    input("Pulse enter para continuar")


# Llamada directa a las funciones
generar_varias_tablas()
generar_tabla_especifica()