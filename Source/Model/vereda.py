# Model/vereda.py
"""
Definición de la clase Vereda para representar una vereda.
"""

class Vereda:
    """
    Clase que representa una vereda.
    """
    def __init__(self, id, nombre, coordenadas):
        """
        Inicializa una nueva vereda.
        
        Parámetros:
        -----------
        id : int
            ID de la vereda.
        nombre : str
            Nombre de la vereda.
        coordenadas : tuple
            Coordenadas de la vereda (latitud, longitud).
        """
        self.id = id
        self.nombre = nombre
        self.coordenadas = coordenadas
