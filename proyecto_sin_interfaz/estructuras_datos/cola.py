"""
Módulo que implementa la estructura de datos Cola (FIFO - First In First Out)
para gestionar la lista de espera de reservas de libros agotados.
"""

import json
from typing import List, Dict, Any

class Cola:
    """
    Implementación de una estructura de datos Cola (FIFO - First In First Out)
    para gestionar la lista de espera de reservas de libros agotados.
    
    Atributos:
        elementos: Lista que almacena los elementos de la cola
        archivo: Nombre del archivo JSON donde se persiste la cola
    """
    
    def __init__(self, archivo: str = "reservas.json"):
        """
        Inicializa una cola vacía o carga desde archivo si existe.
        
        Args:
            archivo: Ruta del archivo JSON para persistencia
        """
        self.archivo = archivo
        self.elementos: List[Dict[str, Any]] = []
        self.cargar_desde_archivo()
    
    def encolar(self, isbn: str, usuario: str) -> None:
        """
        Agrega un elemento al final de la cola.
        
        Args:
            isbn: ISBN del libro reservado
            usuario: Nombre del usuario que solicita la reserva
        """
        elemento = {
            "ISBN": isbn,
            "Usuario": usuario
        }
        self.elementos.append(elemento)
        self.guardar_en_archivo()
    
    def desencolar(self) -> Dict[str, Any]:
        """
        Elimina y retorna el elemento del frente de la cola.
        
        Returns:
            Diccionario con la información de la reserva más antigua
            
        Raises:
            IndexError: Si la cola está vacía
        """
        if self.esta_vacia():
            raise IndexError("La cola está vacía")
        elemento = self.elementos.pop(0)
        self.guardar_en_archivo()
        return elemento
    
    def frente(self) -> Dict[str, Any]:
        """
        Retorna el elemento del frente sin eliminarlo.
        
        Returns:
            Diccionario con la información de la reserva más antigua
        """
        if self.esta_vacia():
            return None
        return self.elementos[0]
    
    def esta_vacia(self) -> bool:
        """
        Verifica si la cola está vacía.
        
        Returns:
            True si la cola está vacía, False en caso contrario
        """
        return len(self.elementos) == 0
    
    def tamanio(self) -> int:
        """
        Retorna el número de elementos en la cola.
        
        Returns:
            Número de elementos en la cola
        """
        return len(self.elementos)
    
    def obtener_reservas_isbn(self, isbn: str) -> List[Dict[str, Any]]:
        """
        Obtiene todas las reservas pendientes para un ISBN específico.
        
        Args:
            isbn: ISBN del libro
            
        Returns:
            Lista de diccionarios con las reservas del ISBN
        """
        return [elem for elem in self.elementos if elem["ISBN"] == isbn]
    
    def eliminar_reserva(self, isbn: str, usuario: str) -> bool:
        """
        Elimina una reserva específica de la cola.
        
        Args:
            isbn: ISBN del libro
            usuario: Nombre del usuario
            
        Returns:
            True si se eliminó la reserva, False si no se encontró
        """
        for i, elem in enumerate(self.elementos):
            if elem["ISBN"] == isbn and elem["Usuario"] == usuario:
                self.elementos.pop(i)
                self.guardar_en_archivo()
                return True
        return False
    
    def guardar_en_archivo(self) -> None:
        """Guarda el estado actual de la cola en un archivo JSON."""
        try:
            import os
            # Obtener el directorio del script actual
            dir_actual = os.path.dirname(os.path.abspath(__file__))
            dir_proyecto = os.path.dirname(dir_actual)
            ruta_archivo = os.path.join(dir_proyecto, self.archivo)
            with open(ruta_archivo, "w", encoding="utf-8") as f:
                json.dump(self.elementos, f, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"Error al guardar en archivo: {e}")
    
    def cargar_desde_archivo(self) -> None:
        """Carga el estado de la cola desde un archivo JSON si existe."""
        try:
            import os
            # Obtener el directorio del script actual
            dir_actual = os.path.dirname(os.path.abspath(__file__))
            dir_proyecto = os.path.dirname(dir_actual)
            ruta_archivo = os.path.join(dir_proyecto, self.archivo)
            with open(ruta_archivo, "r", encoding="utf-8") as f:
                self.elementos = json.load(f)
        except FileNotFoundError:
            self.elementos = []
        except Exception as e:
            print(f"Error al cargar desde archivo: {e}")
            self.elementos = []

