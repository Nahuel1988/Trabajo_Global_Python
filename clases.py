import random, time
# Clase Detector: Detecta patrones de mutación en una matriz de ADN
class Detector:
    def __init__(self, ADN, cant_letras=4):
        # Inicializa el detector con la matriz de ADN y la cantidad mínima de letras iguales consecutivas para detectar una mutación
        self.ADN = ADN  # Lista de listas que representa la matriz de ADN.
        self.cant_letras = cant_letras  # Número mínimo de letras iguales consecutivas para detectar una mutación.

    def detectar_mutantes(self):
        # Llama a las funciones de detección de mutaciones en las direcciones horizontal, vertical y diagonal
        return (
            self._detectar_horizontal() or
            self._detectar_vertical() or
            self._detectar_diagonal()
        )

    def _detectar_horizontal(self):
        # Recorre cada fila y verifica si contiene una secuencia mutante
        for fila in self.ADN:
            if self._tiene_mutacion(fila):
                return True
        return False

    def _detectar_vertical(self):
        # Recorre cada columna y verifica si contiene una secuencia mutante
        for col in range(len(self.ADN[0])):
            columna = [fila[col] for fila in self.ADN]  # Extrae la columna
            if self._tiene_mutacion(columna):
                return True
        return False

    def _detectar_diagonal(self):
        # Detecta mutaciones en las diagonales (principal y secundaria) de la matriz
        n = len(self.ADN)
        for i in range(n - self.cant_letras + 1):
            for j in range(n - self.cant_letras + 1):
                # Diagonal principal
                if self._tiene_mutacion([self.ADN[i + k][j + k] for k in range(self.cant_letras)]):
                    return True
                # Diagonal secundaria
                if self._tiene_mutacion([self.ADN[i + k][j + self.cant_letras - 1 - k] for k in range(self.cant_letras)]):
                    return True
        return False

    def _tiene_mutacion(self, linea):
        # Verifica si una secuencia tiene una cantidad mínima de letras iguales consecutivas
        contador = 1  # Contador para rastrear letras consecutivas
        for i in range(1, len(linea)):
            if linea[i] == linea[i - 1]:
                contador += 1
                if contador >= self.cant_letras:
                    return True
            else:
                contador = 1  # Reinicia el contador si las letras son diferentes
        return False

class Mutador:
    def __init__(self, tipo_mutacion):
        self.tipo_mutacion = tipo_mutacion

class Radiacion(Mutador):
    def __init__(self, base_nitrogenada, cant_letras=4, tipo_mutacion="horizontal"):
        super().__init__(tipo_mutacion)
        self.base_nitrogenada = base_nitrogenada
        self.cant_letras = cant_letras

    def crear_mutante(self, adn, posicion_inicial, orientacion):
        try:
            fila, columna = posicion_inicial

            if orientacion.upper() == "H":  # Mutación Horizontal
                for i in range(columna, min(columna + self.cant_letras, len(adn[0]))):
                    adn[fila][i] = self.base_nitrogenada  # Cambiar ADN directamente

            elif orientacion.upper() == "V":  # Mutación Vertical
                for i in range(fila, min(fila + self.cant_letras, len(adn))):
                    adn[i][columna] = self.base_nitrogenada  # Cambiar ADN directamente

            else:
                raise ValueError("Orientación inválida. Use 'H' para horizontal o 'V' para vertical.")
            
            return adn

        except IndexError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")




class Virus(Mutador):
    def __init__(self, base_nitrogenada, tipo_mutacion="diagonal"):
        super().__init__(tipo_mutacion)
        self.base_nitrogenada = base_nitrogenada
        self.longitud_mutacion = 4  # Longitud de la mutación en bases nitrogenadas

    def crear_mutante(self, adn, posicion_inicial, direccion):
        try:
            fila, columna = posicion_inicial

            if direccion == "D":  # Diagonal descendente hacia la derecha
                for i in range(self.longitud_mutacion):
                    # Verifica si la columna se excede
                    if columna + i >= len(adn[0]):
                        print(f"Error: La mutación diagonal descendente no puede continuar más allá de la columna {len(adn[0])}.")
                        return None  # Detiene la mutación si la columna se sale del rango

                    if fila + i < len(adn) and columna + i < len(adn[0]):  # Valida los límites
                        adn[fila + i][columna + i] = self.base_nitrogenada
                    else:
                        raise IndexError("La mutación diagonal descendente excede los límites de la matriz.")
            elif direccion == "A":  # Diagonal ascendente hacia la izquierda
                for i in range(self.longitud_mutacion):
                    # Verifica si la fila se sale del rango superior
                    if fila - i < 0:
                        print(f"Error: La mutación diagonal ascendente no puede continuar más allá de la fila 1.")
                        return None  # Detiene la mutación si la fila se sale del rango
                    
                    # Verifica si la columna se excede
                    if columna + i >= len(adn[0]):
                        print(f"Error: La mutación diagonal ascendente no puede continuar más allá de la columna 1.")
                        return None  # Detiene la mutación si la columna se sale del rango
                    
                    adn[fila - i][columna + i] = self.base_nitrogenada
            else:
                raise ValueError("Dirección inválida. Use 'D' para descendente o 'A' para ascendente.")
            return adn
        except IndexError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")




class Sanador:
    def __init__(self, nombre, nivel_sanacion):
        self.nombre = nombre
        self.nivel_sanacion = nivel_sanacion

    def sanar_mutantes(self, adn, detectar_mutante):
        if detectar_mutante(adn):
            print("Se detectectaron mutaciones. Generando nuevo ADN sano...")
            espera()
            
            nuevo_adn = self.generar_adn_sano(len(adn), len(adn[0]), detectar_mutante)
            return nuevo_adn
        else:
            print("No se detectaron mutaciones s. El ADN está sano.")
            return adn

    def generar_adn_sano(self, filas, columnas, detectar_mutante):
        bases = ['A', 'T', 'C', 'G']
        while True:  # Repetir hasta generar un ADN válido
            adn_sano = []

            for i in range(filas):
                fila = []
                for j in range(columnas):
                    base = random.choice(bases)

                    # Asegurar que no haya mutaciones horizontales
                    while j > 0 and base == fila[j - 1]:
                        base = random.choice(bases)

                    # Asegurar que no haya mutaciones verticales
                    if i > 0 and base == adn_sano[i - 1][j]:
                        while base == adn_sano[i - 1][j]:
                            base = random.choice(bases)

                    # Asegurar que no haya mutaciones diagonales (principal)
                    if i > 0 and j > 0 and base == adn_sano[i - 1][j - 1]:
                        while base == adn_sano[i - 1][j - 1]:
                            base = random.choice(bases)

                    # Asegurar que no haya mutaciones diagonales (secundaria)
                    if i > 0 and j < columnas - 1 and base == adn_sano[i - 1][j + 1]:
                        while base == adn_sano[i - 1][j + 1]:
                            base = random.choice(bases)

                    fila.append(base)
                adn_sano.append(fila)

            # Verificar que el ADN generado sea válido
            if not detectar_mutante(adn_sano):
               return adn_sano
def espera():
    for i in range(3):
                for j in range(3):
                    time.sleep(0.5)
                    print(".",end="",flush=True)
                #time.sleep(0.5)
                print(" ",end="",flush=True)