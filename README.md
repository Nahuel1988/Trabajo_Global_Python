# Integrantes del trabajo: Fausto Chirino, Nahuel Morales, Neyen Bianchi , Leo Gomez
# Trabajo_Global_Python

#Explicación de como usar:

1. Ingresar una secuencia de ADN
Al iniciar el programa, se te pedirá que ingreses una secuencia de ADN de 6 filas, cada una con 6 caracteres. Los caracteres deben ser A, T, C, o G, y no debe haber espacios entre ellos. Ejemplo de una secuencia válida:

ATCGAT
GCTGGC
ATCGGA
CGTATC
TGCATG
ATGCGT

Pasos:

El programa te pedirá que ingreses una fila a la vez.
Si introduces una fila incorrecta (por ejemplo, con caracteres fuera de A, T, C, G, o con una longitud incorrecta), el programa te informará de un error y te pedirá que comiences desde el principio.
Una vez que las 6 filas de ADN sean ingresadas correctamente, el programa las mostrará y procederá al siguiente paso.

2. Elegir una operación a realizar
Una vez ingresado el ADN, el programa te ofrece un menú de opciones para operar sobre la secuencia de ADN:

1-Detectar mutaciones
2-Mutar el ADN
3-Sanar el ADN
4-Salir del programa
Debes ingresar el número correspondiente a la operación que deseas realizar:

1 - Detectar mutaciones: Esta opción verifica si el ADN es un "mutante" (según algún criterio definido en la clase Detector). El resultado será un mensaje que te indica si el ADN es mutante o no.

2 - Mutar el ADN: Puedes elegir entre dos tipos de mutadores:

Radiación (horizontal o vertical): Te pedirá que elijas una base nitrogenada (A, T, C, G), una posición inicial (fila y columna), y la orientación de la mutación (horizontal o vertical). Luego, mutará la secuencia de ADN según los parámetros ingresados.
Virus (diagonal): De nuevo, te pedirá que elijas una base nitrogenada, una posición inicial, y la dirección de la mutación (ascendente o descendente). Se aplicará una mutación diagonal en el ADN.
Después de realizar la mutación, se mostrará el ADN modificado.

3 - Sanar el ADN: Si el ADN ha sido mutado, puedes usar esta opción para "sanarlo". El programa aplicará alguna lógica de sanación para restaurar el ADN original.

4 - Salir del programa: Finaliza la ejecución del programa.

3. Realizar una nueva operación o salir
Después de cada operación, se te preguntará si deseas realizar otra operación. Si eliges sí (respondiendo "s"), el programa te permitirá realizar otra operación. Si eliges no (respondiendo "n"), el programa se cerrará.detector_obj** se crea para instanciar el objeto Detector en el cual se le pasan dos argumentos:
ADN: La matriz de ADN.
cant_letras=4: Cantidad de letras iguales consecutivas necesarias para definir una mutación.

Con un if si variable consulta es = 1, se llama al método detectar_mutantes() de detector_obj para verificar si el ADN tiene una mutación. El resultado sera una impresion que diga ¿Es mutante? y un dato booleano sea True o False segun lo que el metodo detectar_mutantes haya detectado

