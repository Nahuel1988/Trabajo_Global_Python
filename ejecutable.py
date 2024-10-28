from clases import Detector
ADN=[]
for i in range(1,7):
    fila = input(f"Ingrese la fila numero {i} de su ADN: ").upper()
    ADN.append(list(fila))

print("\nSecuencia de ADN:")
for fila in ADN:
    print(" ".join(fila))

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
    