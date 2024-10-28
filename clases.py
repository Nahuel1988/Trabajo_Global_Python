class Detector:
    def __init__(self, ADN, cant_letras=4):
        
        self.ADN = ADN  #Lista de listas que representa la matriz de ADN.
        self.cant_letras = cant_letras #Número mínimo de letras iguales consecutivas para detectar una mutación.

    def detectar_mutantes(self):
        return (
            self._detectar_horizontal() or
            self._detectar_vertical() or
            self._detectar_diagonal()
        )

    def _detectar_horizontal(self):
        for fila in self.ADN:
            if self._tiene_mutacion(fila):
                return True
        return False
    
    def _detectar_vertical(self):
        for col in range (len(self.ADN[0])):
            columna= [fila[col] for fila in self.ADN]
            if self._tiene_mutacion(columna):
                return True
        return False

    def _detectar_diagonal(self):
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
        contador = 1
        for i in range(1, len(linea)):
            if linea[i] == linea[i - 1]:
                contador += 1
                if contador >= self.cant_letras:
                    return True
            else:
                contador = 1
        return False
