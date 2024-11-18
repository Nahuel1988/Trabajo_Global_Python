# Integrantes del trabajo: Fausto Chirino, Nahuel Morales, Neyen Bianchi , Leo Gomez
# Trabajo_Global_Python
Explicación:

Archivo ejecutable.py:
en este archivo se crea una lista con el nombre **ADN** el cual se ira llenando fila por fila con lo que ingresa el usuario en la variable fila, simulando asi una matriz, esto se logra gracias a un bucle for que itera en rango de 1 a 7.

Al finalizar el bucle for se imprime la matriz de ADN ingresada por el usuario, con cada carácter separado por un espacio para mayor claridad.

Luego en variable consulta se le pide al usuario que ingrese un numero para seleccionar la acción que desea realizar:
1-Detectar mutación
2-Mutarlo
3-Sanarlo

En la variable **detector_obj** se crea para instanciar el objeto Detector en el cual se le pasan dos argumentos:
ADN: La matriz de ADN.
cant_letras=4: Cantidad de letras iguales consecutivas necesarias para definir una mutación.

Con un if si variable consulta es = 1, se llama al método detectar_mutantes() de detector_obj para verificar si el ADN tiene una mutación. El resultado sera una impresion que diga ¿Es mutante? y un dato booleano sea True o False segun lo que el metodo detectar_mutantes haya detectado

