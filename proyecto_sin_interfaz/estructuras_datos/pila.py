"""
Módulo que implementa la estructura de datos Pila (LIFO - Last In First Out)
para gestionar el historial de préstamos por usuario.
"""

import json
from datetime import datetime
from typing import List, Dict, Any

class Pila:
    """
    Implementación de una estructura de datos Pila (LIFO - Last In First Out)
    para gestionar el historial de préstamos por usuario.
    
    Atributos:
        elementos: Lista que almacena los elementos de la pila
        archivo: Nombre del archivo JSON donde se persiste la pila
    """
    
    def __init__(self, archivo: str = "historial_prestamos.json"):
        """
        Inicializa una pila vacía o carga desde archivo si existe.
        
        Args:
            archivo: Ruta del archivo JSON para persistencia
        """
        self.archivo = archivo
        self.elementos: List[Dict[str, Any]] = []
        self.cargar_desde_archivo()
    
    def apilar(self, isbn: str, fecha_prestamo: str, usuario: str) -> None:
        """
        Agrega un elemento a la cima de la pila.
        
        Args:
            isbn: ISBN del libro prestado
            fecha_prestamo: Fecha del préstamo en formato string
            usuario: Nombre del usuario que realiza el préstamo
        """
        elemento = {
            "ISBN": isbn,
            "Fecha": fecha_prestamo,
            "Usuario": usuario
        }
        self.elementos.append(elemento)
        self.guardar_en_archivo()
    
    def desapilar(self) -> Dict[str, Any]:
        """
        Elimina y retorna el elemento de la cima de la pila.
        
        Returns:
            Diccionario con la información del préstamo más reciente
            
        Raises:
            IndexError: Si la pila está vacía
        """
        if self.esta_vacia():
            raise IndexError("La pila está vacía")
        elemento = self.elementos.pop()
        self.guardar_en_archivo()
        return elemento
    
    def cima(self) -> Dict[str, Any]:
        """
        Retorna el elemento de la cima sin eliminarlo.
        
        Returns:
            Diccionario con la información del préstamo más reciente
        """
        if self.esta_vacia():
            return None
        return self.elementos[-1]
    
    def esta_vacia(self) -> bool:
        """
        Verifica si la pila está vacía.
        
        Returns:
            True si la pila está vacía, False en caso contrario
        """
        return len(self.elementos) == 0
    
    def tamanio(self) -> int:
        """
        Retorna el número de elementos en la pila.
        
        Returns:
            Número de elementos en la pila
        """
        return len(self.elementos)
    
    def obtener_historial_usuario(self, usuario: str) -> List[Dict[str, Any]]:
        """
        Obtiene el historial completo de préstamos de un usuario específico.
        
        Args:
            usuario: Nombre del usuario
            
        Returns:
            Lista de diccionarios con los préstamos del usuario
        """
        return [elem for elem in self.elementos if elem["Usuario"] == usuario]
    
    def guardar_en_archivo(self) -> None:
        """Guarda el estado actual de la pila en un archivo JSON."""
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
        """Carga el estado de la pila desde un archivo JSON si existe."""
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

