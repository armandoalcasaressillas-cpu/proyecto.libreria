"""
Módulo que contiene los algoritmos de búsqueda requeridos:
- Búsqueda Lineal
- Búsqueda Binaria
"""

from typing import List, Optional
from funciones_libros.libro import Libro

class Busqueda:
    """
    Clase que contiene los algoritmos de búsqueda requeridos.
    """
    
    def busqueda_lineal(self, inventario: List[Libro], termino: str) -> List[Libro]:
        """
        Busca libros por título o autor usando búsqueda lineal en el inventario general.
        
        Args:
            inventario: Lista de objetos Libro (inventario general desordenado)
            termino: Término de búsqueda (puede ser título o autor)
            
        Returns:
            Lista de objetos Libro que coinciden con el término de búsqueda
        """
        resultados = []
        termino_lower = termino.lower()
        
        for libro in inventario:
            if (termino_lower in libro.titulo.lower() or 
                termino_lower in libro.autor.lower()):
                resultados.append(libro)
        
        return resultados
    
    def busqueda_binaria(self, inventario_ordenado: List[Libro], isbn: str) -> Optional[int]:
        """
        Busca un libro por ISBN usando búsqueda binaria en el inventario ordenado.
        Esta función es crítica para verificar reservas pendientes.
        
        Args:
            inventario_ordenado: Lista de objetos Libro ordenada por ISBN
            isbn: ISBN a buscar
            
        Returns:
            Posición del libro en la lista si se encuentra, None en caso contrario
        """
        izquierda = 0
        derecha = len(inventario_ordenado) - 1
        isbn_limpio = isbn.replace("-", "").replace(" ", "")
        
        try:
            isbn_int = int(isbn_limpio)
        except ValueError:
            return None
        
        while izquierda <= derecha:
            medio = (izquierda + derecha) // 2
            isbn_medio_limpio = inventario_ordenado[medio].isbn.replace("-", "").replace(" ", "")
            
            try:
                isbn_medio_int = int(isbn_medio_limpio)
            except ValueError:
                return None
            
            if isbn_medio_int == isbn_int:
                return medio
            elif isbn_medio_int < isbn_int:
                izquierda = medio + 1
            else:
                derecha = medio - 1
        
        return None

