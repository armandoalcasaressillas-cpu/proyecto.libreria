"""
Módulo que gestiona los préstamos y devoluciones de libros.
"""

from datetime import datetime
from typing import Optional, Tuple
from estructuras_datos.pila import Pila
from estructuras_datos.cola import Cola
from funciones_libros.gestor_libros import GestorLibros
from algoritmos_busqueda.busqueda import Busqueda

class GestorPrestamos:
    """
    Clase que gestiona los préstamos y devoluciones de libros.
    Utiliza pilas para el historial y colas para las reservas.
    
    Atributos:
        gestor_libros: Instancia del gestor de libros
        historial: Pila que almacena el historial de préstamos
        reservas: Cola que almacena las reservas de libros agotados
        busqueda: Instancia de la clase de búsqueda
    """
    
    def __init__(self, gestor_libros: GestorLibros):
        """
        Inicializa el gestor de préstamos.
        
        Args:
            gestor_libros: Instancia del gestor de libros
        """
        self.gestor_libros = gestor_libros
        self.historial = Pila()
        self.reservas = Cola()
        self.busqueda = Busqueda()
    
    def prestar_libro(self, isbn: str, usuario: str) -> Tuple[bool, str]:
        """
        Presta un libro a un usuario.
        Si el libro no está disponible, se agrega a la cola de reservas.
        
        Args:
            isbn: ISBN del libro a prestar
            usuario: Nombre del usuario
            
        Returns:
            Tupla (éxito, mensaje)
        """
        # Buscar el libro usando búsqueda binaria (crítica)
        libro = self.gestor_libros.buscar_por_isbn_binaria(isbn)
        
        if libro is None:
            return (False, f"Libro con ISBN {isbn} no encontrado.")
        
        if libro.esta_disponible():
            # Prestar el libro
            libro.prestar()
            fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Apilar en el historial (Pila LIFO)
            self.historial.apilar(isbn, fecha, usuario)
            
            # Guardar cambios en el inventario
            self.gestor_libros.guardar_inventario()
            
            return (True, f"Libro '{libro.titulo}' prestado exitosamente a {usuario}.")
        else:
            # Agregar a la cola de reservas (Cola FIFO)
            self.reservas.encolar(isbn, usuario)
            return (False, f"Libro '{libro.titulo}' no disponible. Se agregó a la lista de espera.")
    
    def devolver_libro(self, isbn: str, usuario: str) -> Tuple[bool, str]:
        """
        Devuelve un libro al inventario.
        Verifica si hay reservas pendientes usando búsqueda binaria.
        
        Args:
            isbn: ISBN del libro a devolver
            usuario: Nombre del usuario
            
        Returns:
            Tupla (éxito, mensaje)
        """
        # Buscar el libro usando búsqueda binaria (crítica)
        libro = self.gestor_libros.buscar_por_isbn_binaria(isbn)
        
        if libro is None:
            return (False, f"Libro con ISBN {isbn} no encontrado.")
        
        # Devolver el libro
        libro.devolver()
        
        # Verificar si hay reservas pendientes para este ISBN
        reservas_isbn = self.reservas.obtener_reservas_isbn(isbn)
        
        mensaje = f"Libro '{libro.titulo}' devuelto exitosamente."
        
        if reservas_isbn:
            # Asignar a la primera persona en la cola (FIFO)
            reserva = self.reservas.desencolar()
            mensaje += f"\nSe asignó automáticamente a {reserva['Usuario']} (reserva pendiente)."
            
            # Prestar inmediatamente al usuario de la reserva
            self.prestar_libro(isbn, reserva['Usuario'])
        
        # Guardar cambios
        self.gestor_libros.guardar_inventario()
        return (True, mensaje)
    
    def obtener_historial_usuario(self, usuario: str) -> list:
        """
        Obtiene el historial de préstamos de un usuario.
        
        Args:
            usuario: Nombre del usuario
            
        Returns:
            Lista de diccionarios con el historial
        """
        return self.historial.obtener_historial_usuario(usuario)
    
    def obtener_reservas_pendientes(self) -> list:
        """
        Obtiene todas las reservas pendientes.
        
        Returns:
            Lista de diccionarios con las reservas
        """
        return self.reservas.elementos

