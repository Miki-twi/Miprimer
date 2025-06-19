# PROYECTO FINAL

historial_prestamos = []

while True:
    print("\nGestion de Prestamos")
    print("1. Registrar un nuevo prestamo")
    print("2. Ver historial de prestamos")
    print("3. Buscar prestamos por nombre")
    print("4. Marcar prestamo como pagado")
    print("5. Salir")

    opcion = input("Selecciona: ")

    if opcion == "1":
        cliente = input("Nombre del cliente: ")
        monto = float(input("Monto del prestamo: "))
        interes = float(input("Tasa de interes: "))
        plazo = int(input("Plazo en meses: "))

        prestamo = {
            "cliente": cliente,
            "monto": monto,
            "interes": interes,
            "plazo": plazo,
            "pagado": False
        }

        historial_prestamos.append(prestamo)
        print("¡Prestamo registrado!")

    elif opcion == "2":
        if not historial_prestamos:
            print("No hay prestamos registrados.")
        else:
            print("\nHistorial de prestamos:")
            for i, prestamo in enumerate(historial_prestamos, start=1):
                print(f"{i}. Cliente: {prestamo['cliente']}, Monto: {prestamo['monto']}, Interes: {prestamo['interes']}, Plazo: {prestamo['plazo']} meses, Pagado: {prestamo['pagado']}")

    elif opcion == "3":
        nombre_buscar = input("Ingrese el nombre del cliente a buscar: ")
        encontrados = False

        for i, prestamo in enumerate(historial_prestamos, start=1):
            if prestamo["cliente"].lower() == nombre_buscar.lower():
                print(f"{i}. Cliente: {prestamo['cliente']}, Monto: {prestamo['monto']}, Interes: {prestamo['interes']}, Plazo: {prestamo['plazo']} meses, Pagado: {prestamo['pagado']}")
                encontrados = True

        if not encontrados:
            print("No se encontraron prestamos para ese cliente.")

    elif opcion == "4":
        if not historial_prestamos:
            print("No hay prestamos registrados.")
        else:
            print("\nPrestamos disponibles:")
            for i, prestamo in enumerate(historial_prestamos, start=1):
                estado = "✅ Pagado" if prestamo["pagado"] else "No pagado"
                print(f"{i}. Cliente: {prestamo['cliente']}, Monto: {prestamo['monto']}, Estado: {estado}")

            try:
                seleccion = int(input("Escribir el numero del prestamo que deseas marcar como pagado: "))
                if 1 <= seleccion <= len(historial_prestamos):
                    historial_prestamos[seleccion - 1]["pagado"] = True
                    print("¡Prestamo marcado como pagado!")
                else:
                    print("Numero invalido.")
            except ValueError:
                print("Entrada no valida. Por favor escribe un numero.")

    elif opcion == "5":
        print("¡Gracias!")
        break

    else:
        print("Opción no valida. Intenta de nuevo.")
