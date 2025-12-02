"""
Módulo que define la clase Libro para representar un libro en el sistema.
"""

from typing import Dict, Any

class Libro:
    """
    Clase que representa un libro en el sistema de gestión de bibliotecas.
    
    Atributos:
        isbn: Identificador único del libro
        titulo: Título del libro
        autor: Autor del libro
        peso: Peso del libro en kilogramos
        valor: Valor del libro en pesos colombianos
        cantidad: Cantidad total de ejemplares
        cantidad_presente: Cantidad de ejemplares disponibles actualmente
    """
    
    def __init__(self, isbn: str, titulo: str, autor: str, peso: float, 
                 valor: int, cantidad: int, cantidad_presente: int = None):
        """
        Inicializa un objeto Libro.
        
        Args:
            isbn: Identificador único del libro
            titulo: Título del libro
            autor: Autor del libro
            peso: Peso del libro en kilogramos
            valor: Valor del libro en pesos colombianos
            cantidad: Cantidad total de ejemplares
            cantidad_presente: Cantidad de ejemplares disponibles (por defecto igual a cantidad)
        """
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.peso = peso
        self.valor = valor
        self.cantidad = cantidad
        self.cantidad_presente = cantidad_presente if cantidad_presente is not None else cantidad
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Convierte el objeto Libro a un diccionario.
        
        Returns:
            Diccionario con todos los atributos del libro
        """
        return {
            "ISBN": self.isbn,
            "Título": self.titulo,
            "Autor": self.autor,
            "Peso": self.peso,
            "Valor": self.valor,
            "Cantidad": self.cantidad,
            "Cantidad_presente": self.cantidad_presente
        }
    
    @classmethod
    def from_dict(cls, datos: Dict[str, Any]) -> 'Libro':
        """
        Crea un objeto Libro desde un diccionario.
        
        Args:
            datos: Diccionario con los datos del libro
            
        Returns:
            Instancia de Libro
        """
        return cls(
            isbn=str(datos.get("ISBN", "")),
            titulo=datos.get("Título", ""),
            autor=datos.get("Autor", ""),
            peso=float(datos.get("Peso", 0)),
            valor=int(datos.get("Valor", 0)),
            cantidad=int(datos.get("Cantidad", 0)),
            cantidad_presente=int(datos.get("Cantidad_presente", datos.get("Cantidad", 0)))
        )
    
    def esta_disponible(self) -> bool:
        """
        Verifica si el libro tiene ejemplares disponibles.
        
        Returns:
            True si hay ejemplares disponibles, False en caso contrario
        """
        return self.cantidad_presente > 0
    
    def prestar(self) -> bool:
        """
        Presta un ejemplar del libro.
        
        Returns:
            True si se pudo prestar, False si no hay ejemplares disponibles
        """
        if self.cantidad_presente > 0:
            self.cantidad_presente -= 1
            return True
        return False
    
    def devolver(self) -> None:
        """Devuelve un ejemplar del libro al inventario."""
        if self.cantidad_presente < self.cantidad:
            self.cantidad_presente += 1
    
    def __str__(self) -> str:
        """Retorna una representación en string del libro."""
        return f"ISBN: {self.isbn}, Título: {self.titulo}, Autor: {self.autor}"
    
    def __repr__(self) -> str:
        """Retorna una representación técnica del libro."""
        return f"Libro(isbn='{self.isbn}', titulo='{self.titulo}', autor='{self.autor}')"

