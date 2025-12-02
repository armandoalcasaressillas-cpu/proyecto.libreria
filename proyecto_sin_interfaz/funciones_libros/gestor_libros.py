"""
Módulo que gestiona el inventario de libros del sistema.
"""

import json
import os
from typing import List, Optional
from .libro import Libro
from algoritmos_ordenamiento.ordenamiento import Ordenamiento

class GestorLibros:
    """
    Clase que gestiona el inventario de libros del sistema.
    Mantiene dos listas: Inventario General (desordenado) e Inventario Ordenado (por ISBN).
    
    Atributos:
        inventario_general: Lista desordenada de objetos Libro
        inventario_ordenado: Lista ordenada por ISBN de objetos Libro
        archivo: Ruta del archivo JSON donde se persiste el inventario
    """
    
    def __init__(self, archivo: str = "libros.json"):
        """
        Inicializa el gestor de libros y carga el inventario desde archivo.
        
        Args:
            archivo: Ruta del archivo JSON con el inventario
        """
        self.archivo = archivo
        self.inventario_general: List[Libro] = []
        self.inventario_ordenado: List[Libro] = []
        self.ordenamiento = Ordenamiento()
        self.cargar_inventario()
    
    def cargar_inventario(self) -> None:
        """
        Carga el inventario desde el archivo JSON y actualiza ambas listas.
        """
        try:
            # Obtener el directorio del script actual
            dir_actual = os.path.dirname(os.path.abspath(__file__))
            dir_proyecto = os.path.dirname(dir_actual)
            ruta_archivo = os.path.join(dir_proyecto, self.archivo)
            
            if not os.path.exists(ruta_archivo):
                # Si el archivo no existe, crear uno vacío
                with open(ruta_archivo, "w", encoding="utf-8") as f:
                    json.dump([], f, indent=4, ensure_ascii=False)
                self.inventario_general = []
                self.inventario_ordenado = []
                return
            
            with open(ruta_archivo, "r", encoding="utf-8") as f:
                datos = json.load(f)
            
            self.inventario_general = [Libro.from_dict(libro) for libro in datos]
            # Ordenar el inventario ordenado por ISBN usando ordenamiento por inserción
            self.inventario_ordenado = self.ordenamiento.ordenamiento_insercion(
                [libro for libro in self.inventario_general]
            )
        except Exception as e:
            print(f"Error al cargar inventario: {e}")
            self.inventario_general = []
            self.inventario_ordenado = []
    
    def guardar_inventario(self) -> None:
        """Guarda el inventario general en el archivo JSON."""
        try:
            # Obtener el directorio del script actual
            dir_actual = os.path.dirname(os.path.abspath(__file__))
            dir_proyecto = os.path.dirname(dir_actual)
            ruta_archivo = os.path.join(dir_proyecto, self.archivo)
            
            datos = [libro.to_dict() for libro in self.inventario_general]
            with open(ruta_archivo, "w", encoding="utf-8") as f:
                json.dump(datos, f, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"Error al guardar inventario: {e}")
    
    def agregar_libro(self, libro: Libro) -> bool:
        """
        Agrega un nuevo libro al inventario.
        Usa ordenamiento por inserción para mantener el inventario ordenado.
        
        Args:
            libro: Objeto Libro a agregar
            
        Returns:
            True si se agregó correctamente, False si el ISBN ya existe
        """
        # Verificar si el ISBN ya existe
        if self.buscar_por_isbn_binaria(libro.isbn) is not None:
            return False
        
        # Agregar al inventario general (desordenado)
        self.inventario_general.append(libro)
        
        # Agregar al inventario ordenado usando ordenamiento por inserción
        self.inventario_ordenado = self.ordenamiento.ordenamiento_insercion(
            [libro for libro in self.inventario_general]
        )
        
        self.guardar_inventario()
        return True
    
    def cargar_libro_manual(self, isbn: str, titulo: str, autor: str, 
                           peso: float, valor: int, cantidad: int) -> Libro:
        """
        Crea un objeto Libro con los datos proporcionados.
        
        Args:
            isbn: ISBN del libro
            titulo: Título del libro
            autor: Autor del libro
            peso: Peso en kilogramos
            valor: Valor en pesos colombianos
            cantidad: Cantidad de ejemplares
            
        Returns:
            Objeto Libro creado
        """
        return Libro(isbn, titulo, autor, peso, valor, cantidad)
    
    def buscar_por_isbn_binaria(self, isbn: str) -> Optional[Libro]:
        """
        Busca un libro por ISBN usando búsqueda binaria en el inventario ordenado.
        
        Args:
            isbn: ISBN a buscar
            
        Returns:
            Objeto Libro si se encuentra, None en caso contrario
        """
        from algoritmos_busqueda.busqueda import Busqueda
        busqueda = Busqueda()
        posicion = busqueda.busqueda_binaria(self.inventario_ordenado, isbn)
        
        if posicion is not None:
            return self.inventario_ordenado[posicion]
        return None
    
    def buscar_por_titulo_autor(self, termino: str) -> List[Libro]:
        """
        Busca libros por título o autor usando búsqueda lineal en el inventario general.
        
        Args:
            termino: Término de búsqueda (título o autor)
            
        Returns:
            Lista de objetos Libro que coinciden con el término
        """
        from algoritmos_busqueda.busqueda import Busqueda
        busqueda = Busqueda()
        return busqueda.busqueda_lineal(self.inventario_general, termino)
    
    def obtener_inventario_ordenado(self) -> List[Libro]:
        """
        Retorna el inventario ordenado por ISBN.
        
        Returns:
            Lista ordenada de objetos Libro
        """
        return self.inventario_ordenado
    
    def obtener_inventario_general(self) -> List[Libro]:
        """
        Retorna el inventario general (desordenado).
        
        Returns:
            Lista desordenada de objetos Libro
        """
        return self.inventario_general
    
    def eliminar_libro(self, isbn: str) -> bool:
        """
        Elimina un libro del inventario.
        
        Args:
            isbn: ISBN del libro a eliminar
            
        Returns:
            True si se eliminó, False si no se encontró
        """
        libro = self.buscar_por_isbn_binaria(isbn)
        if libro:
            self.inventario_general.remove(libro)
            self.inventario_ordenado = self.ordenamiento.ordenamiento_insercion(
                [libro for libro in self.inventario_general]
            )
            self.guardar_inventario()
            return True
        return False
