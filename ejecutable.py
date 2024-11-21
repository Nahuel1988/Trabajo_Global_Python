from clases import Detector, Radiacion, Virus, Sanador
ADN = []
while True:  # Bucle principal
      # Reinicia la lista de ADN
    print("\n------Bienvenido al Programa de deteccion de mutaciones------\n\n\n"
             
                "Para iniciar necesita una muestra de ADN... \n"
                "1-ingresar una muestra manualmente\n"
                "2-usar la muestra pre-guardada\n")
    
    while True:
            opcion=input()
            if opcion=="1":
                ADN = []
                print("(escribir de corrido y sin espacios, solo con A, T, C, G)")
                for i in range(1, 7):
                    while True:  # Repite hasta que se ingrese una fila válida
                        fila = input(f"Ingrese la fila número {i} de su ADN : \n").upper()
                        if all(adn in "ATCG" for adn in fila) and len(fila) == 6:
                            ADN.append(list(fila))  # Convierte la fila en lista y la agrega al ADN
                            break  # Salir del bucle si la fila es válida
                        else:
                            print("Error: La secuencia ingresada contiene caracteres no válidos o no tiene la longitud correcta. Intente nuevamente.")
                break
            
            elif opcion=="2":
                ADN=["AAAATG","CGTAGT","TGAGTC","CACAGT","AGTCGT","CTGATC"]
                break
            else:
                    print("opcion invalida, por favor una de las siguientes opciones...\n"
                        "1-ingresar una muestra manualmente\n"
                        "2-usar la muestra pre-guardada\n")
                
   
    print("\nSecuencia de ADN:")
    for fila in ADN:
        print("  ".join(fila))
        
    break  # Salir del bucle después de ingresar todo el ADN correctamente
     
while True:
        while True:
            try:
                consulta = int(input("\nIngrese qué tipo de operación desea realizar: \n1-Detectar mutaciones\n2-Mutarlo\n3-Sanarlo\n4-Salir:\n"))
                break
            except Exception: print("Caracter no valido, por favor intente nuevamente...")
        
        if consulta == 1:
            detector_obj = Detector(ADN=ADN, cant_letras=4)
            es_mutante = detector_obj.detectar_mutantes()
            print("¿Es mutante?", es_mutante)
        elif consulta == 2:
            tipo_mutador = input("Seleccione el tipo de mutador:\n1-Radiación (horizontal o vertical)\n2-Virus (diagonal):\n")
            if tipo_mutador == "1":
                # Radiación 
                
                while True:
                    base_nitrogenada = input("Ingrese la base nitrogenada para la mutación (A, T, C, G): ").upper()
                    if base_nitrogenada not in "ATCG":
                        print("Error: La base nitrogenada no es válida. Debe ser: A, T, C o G. \n")
                    else: break

                while True:
                    try:
                        fila_inicial=    int(input("Ingrese la fila inicial (1-6): "))
                        columna_inicial=    int(input("Ingrese la columna inicial (1-6): "))
                        
                        if not (0 < fila_inicial <= 7) or not (1 <= columna_inicial <= 6): 
                            raise ValueError
                             
                        else:
                            posicion_inicial = (fila_inicial -1, columna_inicial -1) # Ajuste a índice de 0 
                            break 
                    except ValueError:
                        print("Error: La posición inicial no es válida. Debe estar en el rango de 1 a 6.")
                    
                while True:
                        orientacion = input("Ingrese la orientación de la mutación ('H' para horizontal, 'V' para vertical): ").upper()
                        if orientacion not in ["H", "V"]:
                            print("Error: La orientación no es válida. Debe ser 'H' o 'V'.")
                        else:break

                radiacion_obj = Radiacion(base_nitrogenada=base_nitrogenada, tipo_mutacion="inserción")
                adn_mutado = radiacion_obj.crear_mutante(ADN, posicion_inicial, orientacion)
                
                if adn_mutado:
                    print("\nADN después de la mutación:")
                    for fila in adn_mutado:
                            print("  ".join(fila))

                    #break

            elif tipo_mutador == "2":
                # Virus
                while True:
                    base_nitrogenada = input("Ingrese la base nitrogenada para la mutación (A, T, C, G): ").upper()
                    if base_nitrogenada not in "ATCG":
                        print("Error: La base nitrogenada no es válida. Debe ser: A, T, C o G. \n")
                    else: break

                while True:
                    try:
                        fila_inicial=    int(input("Ingrese la fila inicial (1-6): "))
                        columna_inicial=    int(input("Ingrese la columna inicial (1-6): "))
                        
                        if not (0 < fila_inicial <= 7) or not (1 <= columna_inicial <= 6): 
                            raise ValueError
                             
                        else:
                            posicion_inicial = (fila_inicial -1, columna_inicial -1) # Ajuste a índice de 0 
                            break 
                    except ValueError:
                        print("Error: La posición inicial no es válida. Debe estar en el rango de 1 a 6.")

                while True:
                        
                        direccion = input("Ingrese la dirección de la mutación ('D' para descendente, 'A' para ascendente): ").upper()
                        if direccion not in ["D", "A"]:
                            print("Error: La dirección no es válida. Debe ser 'D' o 'A'.")
                        else:break 

                virus_obj = Virus(base_nitrogenada=base_nitrogenada, tipo_mutacion="diagonal")
                adn_mutado = virus_obj.crear_mutante(ADN, posicion_inicial, direccion)

                if adn_mutado:
                    print("\nADN después de la mutación:")
                    for fila in adn_mutado:
                            print("  ".join(fila))

            else:print("opcion ingresada invalida...")

        elif consulta == 3:
            sanador = Sanador(nombre="Curador Supremo", nivel_sanacion=5)
            adn_sanado = sanador.sanar_mutantes(ADN, lambda adn: Detector(ADN=adn, cant_letras=4).detectar_mutantes())
            if adn_sanado:
                ADN = adn_sanado  # Actualiza ADN con el ADN sanado
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