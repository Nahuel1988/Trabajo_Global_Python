from clases import Detector
while True:  # Bucle que se reinicia en caso de error
    ADN = []  # Reinicia la lista de ADN

    for i in range(1, 7):
        fila = input(f"Ingrese la fila número {i} de su ADN (escribir de corrido y sin espacios, solo con A, T, C, G): ").upper()
        # Verificamos que solo contenga letras válidas
        if all(nucleotido in "ATCG" for nucleotido in fila) and len(fila) == 6:
            ADN.append(list(fila))
        else:
            print("Error: La secuencia ingresada contiene caracteres no válidos. Empezando desde cero.")
            break  # Sale del bucle actual y reinicia todo el proceso
    else:
        # Si todas las filas fueron ingresadas correctamente, terminamos el bucle
        break

print("\nSecuencia de ADN:")
for fila in ADN:
    print("  ".join(fila))

consulta = int(input("\nIngrese que tipo de operación desea realizar: \n1-Detectar mutaciones\n2-Mutarlo\n3-Sanarlo:\n"))

detector_obj = Detector(ADN=ADN,cant_letras=4)
if consulta == 1:
    es_mutante = detector_obj.detectar_mutantes()
    print("¿Es mutante?", es_mutante)
elif consulta == 2:
    pass
elif consulta == 3:
    pass
else:
    print("Operación no implementada")
    