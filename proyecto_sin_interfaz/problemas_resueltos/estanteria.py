"""
Módulo que gestiona los algoritmos de resolución de problemas para estanterías.
Implementa Fuerza Bruta y Backtracking.
"""

from typing import List, Tuple
from funciones_libros.libro import Libro

class Estanteria:
    """
    Clase que gestiona los algoritmos de resolución de problemas para estanterías.
    Implementa Fuerza Bruta y Backtracking.
    """
    
    def __init__(self, capacidad_maxima: float = 8.0):
        """
        Inicializa la estantería con una capacidad máxima.
        
        Args:
            capacidad_maxima: Peso máximo que soporta un estante en kilogramos
        """
        self.capacidad_maxima = capacidad_maxima
    
    def fuerza_bruta_estanteria_deficiente(self, libros: List[Libro]) -> List[List[Libro]]:
        """
        Encuentra todas las combinaciones posibles de cuatro libros que superen
        el umbral de riesgo (8 Kg) usando fuerza bruta.
        Explora exhaustivamente todas las combinaciones.
        
        Args:
            libros: Lista de objetos Libro
            
        Returns:
            Lista de listas con las combinaciones que superan el umbral
        """
        combinaciones_riesgo = []
        n = len(libros)
        
        # Explorar todas las combinaciones de 4 libros
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    for l in range(k + 1, n):
                        combinacion = [libros[i], libros[j], libros[k], libros[l]]
                        peso_total = sum(libro.peso for libro in combinacion)
                        
                        if peso_total > self.capacidad_maxima:
                            combinaciones_riesgo.append(combinacion)
        
        return combinaciones_riesgo
    
    def backtracking_estanteria_optima(self, libros: List[Libro]) -> Tuple[List[Libro], float, int]:
        """
        Encuentra la combinación de libros que maximiza el valor total sin exceder
        la capacidad máxima de peso usando backtracking.
        Demuestra la exploración y ejecución del algoritmo.
        
        Args:
            libros: Lista de objetos Libro disponibles
            
        Returns:
            Tupla con (mejor_combinacion, mejor_valor, mejor_peso)
        """
        mejor_combinacion = []
        mejor_valor = 0
        mejor_peso = 0
        
        def backtrack(combinacion_actual: List[Libro], indice: int, peso_actual: float, valor_actual: int):
            """
            Función recursiva de backtracking que explora todas las combinaciones.
            
            Args:
                combinacion_actual: Lista actual de libros seleccionados
                indice: Índice del libro actual a considerar
                peso_actual: Peso total de la combinación actual
                valor_actual: Valor total de la combinación actual
            """
            nonlocal mejor_combinacion, mejor_valor, mejor_peso
            
            # Caso base: se han considerado todos los libros
            if indice >= len(libros):
                # Actualizar mejor solución si es necesario
                if valor_actual > mejor_valor:
                    mejor_combinacion = combinacion_actual.copy()
                    mejor_valor = valor_actual
                    mejor_peso = peso_actual
                return
            
            # Opción 1: No incluir el libro actual
            backtrack(combinacion_actual, indice + 1, peso_actual, valor_actual)
            
            # Opción 2: Incluir el libro actual (si cabe)
            libro_actual = libros[indice]
            nuevo_peso = peso_actual + libro_actual.peso
            
            if nuevo_peso <= self.capacidad_maxima:
                combinacion_actual.append(libro_actual)
                backtrack(combinacion_actual, indice + 1, nuevo_peso, 
                         valor_actual + libro_actual.valor)
                combinacion_actual.pop()  # Backtrack: deshacer la selección
        
        # Iniciar la exploración
        backtrack([], 0, 0.0, 0)
        
        return mejor_combinacion, mejor_valor, mejor_peso

