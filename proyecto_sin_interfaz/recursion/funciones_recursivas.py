"""
Módulo que contiene las funciones recursivas requeridas.
"""

from typing import List
from funciones_libros.libro import Libro

class FuncionesRecursivas:
    """
    Clase que contiene las funciones recursivas requeridas.
    """
    
    def valor_total_autor_recursivo_pila(self, libros: List[Libro], autor: str, indice: int = 0) -> int:
        """
        Calcula el valor total de todos los libros de un autor específico usando recursión de pila.
        La recursión de pila acumula el resultado en el retorno de las llamadas recursivas.
        
        Args:
            libros: Lista de objetos Libro
            autor: Nombre del autor a buscar
            indice: Índice actual en la lista (para recursión)
            
        Returns:
            Valor total en pesos colombianos de los libros del autor
        """
        # Caso base: se han procesado todos los libros
        if indice >= len(libros):
            return 0
        
        # Verificar si el libro actual es del autor buscado
        valor_actual = 0
        if libros[indice].autor.lower() == autor.lower():
            valor_actual = libros[indice].valor
        
        # Llamada recursiva (recursión de pila)
        return valor_actual + self.valor_total_autor_recursivo_pila(libros, autor, indice + 1)
    
    def peso_promedio_autor_recursivo_cola(self, libros: List[Libro], autor: str, 
                                           indice: int = 0, suma_pesos: float = 0.0, 
                                           cantidad: int = 0) -> float:
        """
        Calcula el peso promedio de la colección de un autor usando recursión de cola.
        La recursión de cola pasa los resultados acumulados como parámetros.
        
        Args:
            libros: Lista de objetos Libro
            autor: Nombre del autor a buscar
            indice: Índice actual en la lista (para recursión)
            suma_pesos: Suma acumulada de pesos (parámetro de acumulación)
            cantidad: Cantidad de libros encontrados (parámetro de acumulación)
            
        Returns:
            Peso promedio de los libros del autor, o 0 si no hay libros
        """
        # Caso base: se han procesado todos los libros
        if indice >= len(libros):
            if cantidad == 0:
                return 0.0
            return suma_pesos / cantidad
        
        # Verificar si el libro actual es del autor buscado
        if libros[indice].autor.lower() == autor.lower():
            nuevo_suma = suma_pesos + libros[indice].peso
            nueva_cantidad = cantidad + 1
        else:
            nuevo_suma = suma_pesos
            nueva_cantidad = cantidad
        
        # Llamada recursiva (recursión de cola)
        return self.peso_promedio_autor_recursivo_cola(libros, autor, indice + 1, 
                                                       nuevo_suma, nueva_cantidad)

