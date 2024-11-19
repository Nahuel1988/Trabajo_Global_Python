from clases import Detector, Radiacion, Virus, Sanador

while True:  # Bucle principal
    ADN = []  # Reinicia la lista de ADN

    for i in range(1, 7):
        while True:  # Repite hasta que se ingrese una fila válida
            fila = input(f"Ingrese la fila número {i} de su ADN (escribir de corrido y sin espacios, solo con A, T, C, G): ").upper()
            if all(adn in "ATCG" for adn in fila) and len(fila) == 6:
                ADN.append(list(fila))  # Convierte la fila en lista y la agrega al ADN
                break  # Salir del bucle si la fila es válida
            else:
                print("Error: La secuencia ingresada contiene caracteres no válidos o no tiene la longitud correcta. Intente nuevamente.")

    print("\nSecuencia de ADN:")
    for fila in ADN:
        print("  ".join(fila))
    break  # Salir del bucle después de ingresar todo el ADN correctamente

while True:
    consulta = int(input("\nIngrese qué tipo de operación desea realizar: \n1-Detectar mutaciones\n2-Mutarlo\n3-Sanarlo\n4-Salir:\n"))

    if consulta == 1:
        detector_obj = Detector(ADN=ADN, cant_letras=4)
        es_mutante = detector_obj.detectar_mutantes()
        print("¿Es mutante?", es_mutante)
    elif consulta == 2:
        tipo_mutador = input("Seleccione el tipo de mutador:\n1-Radiación (horizontal o vertical)\n2-Virus (diagonal):\n")
        if tipo_mutador == "1":
    # Radiación
            base_nitrogenada = input("Ingrese la base nitrogenada para la mutación (A, T, C, G): ").upper()
            if base_nitrogenada not in "ATCG":
                print("Error: La base nitrogenada no es válida. Debe ser: A, T, C o G.")
            else:
                posicion_inicial = (
                    int(input("Ingrese la fila inicial (1-6): ")),
                    int(input("Ingrese la columna inicial (1-6): "))
                )
                orientacion = input("Ingrese la orientación de la mutación ('H' para horizontal, 'V' para vertical): ").upper()
                if orientacion not in ["H", "V"]:
                    print("Error: La orientación no es válida. Debe ser 'H' o 'V'.")
                else:
                    radiacion_obj = Radiacion(base_nitrogenada=base_nitrogenada, tipo_mutacion="inserción")
                    adn_mutado = radiacion_obj.crear_mutante(ADN, posicion_inicial, orientacion)

                    if adn_mutado:
                        print("\nADN después de la mutación:")
                        for fila in adn_mutado:
                            print("  ".join(fila))
        elif tipo_mutador == "2":
            # Virus
            base_nitrogenada = input("Ingrese la base nitrogenada para la mutación (A, T, C, G): ").upper()
            if base_nitrogenada not in "ATCG":
                print("Error: La base nitrogenada no es válida. Debe ser: A, T, C o G.")
            else:
                posicion_inicial = (
                    int(input("Ingrese la fila inicial (1-6): ")),
                    int(input("Ingrese la columna inicial (1-6): "))
                )
                direccion = input("Ingrese la dirección de la mutación ('D' para descendente, 'A' para ascendente): ").upper()
                if direccion not in ["D", "A"]:
                    print("Error: La dirección no es válida. Debe ser 'D' o 'A'.")
                else:
                    virus_obj = Virus(base_nitrogenada=base_nitrogenada, tipo_mutacion="diagonal")
                    adn_mutado = virus_obj.crear_mutante(ADN, posicion_inicial, direccion)

                    if adn_mutado:
                        print("\nADN después de la mutación:")
                        for fila in adn_mutado:
                            print("  ".join(fila))

    elif consulta == 3:  # Opción de sanar el ADN
        sanador = Sanador(nombre="Curador Supremo", nivel_sanacion=5)
        adn_sanado = sanador.sanar_mutantes(ADN, lambda adn: Detector(ADN=adn, cant_letras=4).detectar_mutantes())
        if adn_sanado:  # Si se genera un ADN sanado
            ADN = adn_sanado  # Actualizamos el ADN principal con el sanado
            print("\nADN después de ser sanado:")
            for fila in ADN:
                print("  ".join(fila))

    elif consulta == 4:
        print("Saliendo del programa...")
        break  # Sale del bucle de operaciones y termina el programa
    else:
        print("Opción no válida. Intente nuevamente.")
    
    # Preguntar si desea realizar otra operación
    continuar = input("\n¿Desea realizar otra operación? (s/n): ").lower()
    if continuar == 'n':
        print("Saliendo del programa...")
        break  # Sale del bucle de operaciones y termina el programa
if ADN:
    print("\nADN Final:")
    for fila in ADN:
        print('  '.join(fila))
    print("\nGracias por utilizar el programa. ¡Esperamos que vuelva pronto!")
else:
    print("\nNo se ingresó un ADN válido al final del programa.")