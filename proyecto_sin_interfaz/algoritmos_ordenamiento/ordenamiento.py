"""
Módulo que contiene los algoritmos de ordenamiento requeridos:
- Ordenamiento por Inserción
- Merge Sort
"""

from typing import List
from funciones_libros.libro import Libro

class Ordenamiento:
    """
    Clase que contiene los algoritmos de ordenamiento requeridos.
    """
    
    def ordenamiento_insercion(self, lista: List[Libro]) -> List[Libro]:
        """
        Ordena una lista de libros por ISBN usando el algoritmo de ordenamiento por inserción.
        Este algoritmo mantiene el inventario ordenado cada vez que se agrega un nuevo libro.
        
        Args:
            lista: Lista de objetos Libro a ordenar
            
        Returns:
            Lista de objetos Libro ordenada por ISBN en orden ascendente
        """
        lista_ordenada = lista.copy()
        
        for i in range(1, len(lista_ordenada)):
            libro_actual = lista_ordenada[i]
            j = i - 1
            
            # Mover elementos mayores que el ISBN actual una posición adelante
            # Normalizar ISBNs para comparación (eliminar guiones y espacios)
            isbn_actual = libro_actual.isbn.replace("-", "").replace(" ", "")
            try:
                isbn_actual_int = int(isbn_actual)
            except ValueError:
                isbn_actual_int = 0
            
            while j >= 0:
                isbn_j = lista_ordenada[j].isbn.replace("-", "").replace(" ", "")
                try:
                    isbn_j_int = int(isbn_j)
                except ValueError:
                    isbn_j_int = 0
                
                if isbn_j_int > isbn_actual_int:
                    lista_ordenada[j + 1] = lista_ordenada[j]
                    j -= 1
                else:
                    break
            
            lista_ordenada[j + 1] = libro_actual
        
        return lista_ordenada
    
    def merge_sort_por_valor(self, lista: List[Libro]) -> List[Libro]:
        """
        Ordena una lista de libros por Valor usando el algoritmo Merge Sort.
        Genera un reporte global de inventario ordenado por valor.
        
        Args:
            lista: Lista de objetos Libro a ordenar
            
        Returns:
            Lista de objetos Libro ordenada por Valor en orden ascendente
        """
        if len(lista) <= 1:
            return lista
        
        # Dividir la lista en dos mitades
        medio = len(lista) // 2
        izquierda = lista[:medio]
        derecha = lista[medio:]
        
        # Ordenar recursivamente ambas mitades
        izquierda = self.merge_sort_por_valor(izquierda)
        derecha = self.merge_sort_por_valor(derecha)
        
        # Combinar las mitades ordenadas
        return self._merge(izquierda, derecha)
    
    def _merge(self, izquierda: List[Libro], derecha: List[Libro]) -> List[Libro]:
        """
        Combina dos listas ordenadas en una sola lista ordenada.
        
        Args:
            izquierda: Lista ordenada de libros
            derecha: Lista ordenada de libros
            
        Returns:
            Lista combinada y ordenada
        """
        resultado = []
        i = j = 0
        
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i].valor <= derecha[j].valor:
                resultado.append(izquierda[i])
                i += 1
            else:
                resultado.append(derecha[j])
                j += 1
        
        # Agregar los elementos restantes
        resultado.extend(izquierda[i:])
        resultado.extend(derecha[j:])
        
        return resultado
    
    def generar_reporte_por_valor(self, inventario: List[Libro], archivo: str = "reporte_por_valor.json") -> None:
        """
        Genera un reporte del inventario ordenado por valor y lo guarda en un archivo.
        
        Args:
            inventario: Lista de objetos Libro
            archivo: Nombre del archivo donde se guardará el reporte
        """
        import json
        import os
        
        inventario_ordenado = self.merge_sort_por_valor(inventario)
        datos = [libro.to_dict() for libro in inventario_ordenado]
        
        try:
            # Obtener el directorio del script actual
            dir_actual = os.path.dirname(os.path.abspath(__file__))
            dir_proyecto = os.path.dirname(dir_actual)
            ruta_archivo = os.path.join(dir_proyecto, archivo)
            
            with open(ruta_archivo, "w", encoding="utf-8") as f:
                json.dump(datos, f, indent=4, ensure_ascii=False)
            print(f"\nReporte generado exitosamente en {archivo}")
        except Exception as e:
            print(f"Error al generar reporte: {e}")

