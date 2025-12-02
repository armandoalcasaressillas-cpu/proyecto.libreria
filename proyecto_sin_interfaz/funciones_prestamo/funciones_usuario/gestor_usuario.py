"""
Módulo que gestiona los usuarios del sistema.
"""

from typing import List, Optional

class Usuario:
    """
    Clase que representa un usuario del sistema.
    
    Atributos:
        nombre: Nombre del usuario
        identificacion: Identificación única del usuario
    """
    
    def __init__(self, nombre: str, identificacion: str):
        """
        Inicializa un usuario.
        
        Args:
            nombre: Nombre del usuario
            identificacion: Identificación única
        """
        self.nombre = nombre
        self.identificacion = identificacion
    
    def __str__(self) -> str:
        """Retorna una representación en string del usuario."""
        return f"Usuario: {self.nombre} (ID: {self.identificacion})"

class GestorUsuario:
    """
    Clase que gestiona los usuarios del sistema.
    """
    
    def __init__(self):
        """Inicializa el gestor de usuarios."""
        self.usuarios: List[Usuario] = []
    
    def agregar_usuario(self, nombre: str, identificacion: str) -> Usuario:
        """
        Agrega un nuevo usuario al sistema.
        
        Args:
            nombre: Nombre del usuario
            identificacion: Identificación única
            
        Returns:
            Objeto Usuario creado
        """
        usuario = Usuario(nombre, identificacion)
        self.usuarios.append(usuario)
        return usuario
    
    def buscar_usuario(self, identificacion: str) -> Optional[Usuario]:
        """
        Busca un usuario por identificación.
        
        Args:
            identificacion: Identificación del usuario
            
        Returns:
            Objeto Usuario si se encuentra, None en caso contrario
        """
        for usuario in self.usuarios:
            if usuario.identificacion == identificacion:
                return usuario
        return None

