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

# Clase Mutador: Representa un mutador con una base nitrogenada y un tipo de mutación
class Mutador:
    def __init__(self, tipo_mutacion):
        self.tipo_mutacion = tipo_mutacion

class Radiacion(Mutador):
    def __init__(self, base_nitrogenada, tipo_mutacion):
        super().__init__(tipo_mutacion)
        self.base_nitrogenada = base_nitrogenada

    def crear_mutante(self, adn, posicion_inicial, orientacion):
        try:
            fila, columna = posicion_inicial
            fila -= 1  # Ajustamos índices a base 0
            columna -= 1
            if orientacion == "H":
                for i in range(4):
                    adn[fila][columna + i] = self.base_nitrogenada
            elif orientacion == "V":
                for i in range(4):
                    adn[fila + i][columna] = self.base_nitrogenada
            else:
                raise ValueError("Orientación inválida. Use 'H' o 'V'.")
            return adn
        except IndexError:
            print("Error: La mutación excede los límites de la matriz.")
        except Exception as e:
            print(f"Error inesperado: {e}")
class Virus(Mutador):
    def __init__(self, base_nitrogenada, tipo_mutacion="diagonal"):
        super().__init__(tipo_mutacion)
        self.base_nitrogenada = base_nitrogenada
        self.longitud_mutacion = 4  # Longitud de la mutación en bases nitrogenadas

    def crear_mutante(self, adn, posicion_inicial, direccion="D"):
        try:
            fila, columna = posicion_inicial
            fila -= 1  # Ajustar índice a base 0
            columna -= 1

            # Validar que la mutación no exceda los límites de la matriz
            if direccion == "D":
                if fila + self.longitud_mutacion > len(adn) or columna + self.longitud_mutacion > len(adn[0]):
                    raise IndexError("La mutación excede los límites de la matriz en diagonal descendente.")
                for i in range(self.longitud_mutacion):
                    adn[fila + i][columna + i] = self.base_nitrogenada
            elif direccion == "A":
                if fila - self.longitud_mutacion < -1 or columna + self.longitud_mutacion > len(adn[0]):
                    raise IndexError("La mutación excede los límites de la matriz en diagonal ascendente.")
                for i in range(self.longitud_mutacion):
                    adn[fila - i][columna + i] = self.base_nitrogenada
            else:
                raise ValueError("Dirección inválida. Use 'D' para descendente o 'A' para ascendente.")
            
            return adn
        except IndexError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")

class Sanador:
    def __init__(self, cant_letras=4):
        self.cant_letras = cant_letras  # Cantidad de letras iguales para considerarse mutación

    def sanar_mutantes(self, adn):
        detector = Detector(adn, self.cant_letras)
        if detector.detectar_mutantes():
            print("Se detectaron mutaciones. Corrigiéndolas...")
            # Busca y corrige todas las mutaciones
            for i in range(len(adn)):
                for j in range(len(adn[i])):
                    if self.es_parte_de_mutacion(adn, i, j):
                        adn[i][j] = self.obtener_nueva_base(adn, i, j)
        else:
            print("El ADN original no tenía mutaciones.")
        return adn

    def es_parte_de_mutacion(self, adn, fila, columna):
        """
        Verifica si una posición específica es parte de una mutación
        (horizontal, vertical o diagonal).
        """
        return (
            self.detectar_mutacion_horizontal(adn, fila, columna) or
            self.detectar_mutacion_vertical(adn, fila, columna) or
            self.detectar_mutacion_diagonal(adn, fila, columna)
        )

    def detectar_mutacion_horizontal(self, adn, fila, columna):
        """
        Detecta si hay una mutación horizontal a partir de la posición dada.
        """
        try:
            # Verifica si las próximas `cant_letras` bases son iguales
            secuencia = [adn[fila][columna + k] for k in range(self.cant_letras)]
            return len(set(secuencia)) == 1  # Todas las bases son iguales
        except IndexError:
            return False

    def detectar_mutacion_vertical(self, adn, fila, columna):
        """
        Detecta si hay una mutación vertical a partir de la posición dada.
        """
        try:
            secuencia = [adn[fila + k][columna] for k in range(self.cant_letras)]
            return len(set(secuencia)) == 1  # Todas las bases son iguales
        except IndexError:
            return False

    def detectar_mutacion_diagonal(self, adn, fila, columna):
        """
        Detecta si hay una mutación diagonal (principal o inversa) a partir de la posición dada.
        """
        try:
            # Diagonal principal
            secuencia_principal = [adn[fila + k][columna + k] for k in range(self.cant_letras)]
            if len(set(secuencia_principal)) == 1:
                return True
        except IndexError:
            pass

        try:
            # Diagonal inversa
            secuencia_inversa = [adn[fila + k][columna - k] for k in range(self.cant_letras)]
            if len(set(secuencia_inversa)) == 1:
                return True
        except IndexError:
            pass

        return False

    def obtener_nueva_base(self, adn, fila, columna):
        """
        Genera una nueva base nitrogenada válida que no cree una nueva mutación.
        """
        bases_posibles = {"A", "T", "C", "G"}
        bases_vecinas = set()

        # Recoge las bases vecinas para evitar repeticiones
        for i in range(max(0, fila - 1), min(len(adn), fila + 2)):
            for j in range(max(0, columna - 1), min(len(adn[i]), columna + 2)):
                if (i, j) != (fila, columna):
                    bases_vecinas.add(adn[i][j])

        # Selecciona una base válida que no sea igual a las vecinas
        base_nueva = (bases_posibles - bases_vecinas).pop()
        return base_nueva
